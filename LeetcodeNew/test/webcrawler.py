from __future__ import print_function

import json
import threading
import time

import requests

try:
    import urllib.parse as urlparse
except ImportError:
    import urlparse as urlparse

# html_helper.py contains the logic for parsing HTML and getting useful URLs
# from it
import html_helper

# graph.py contains the class which represents the website graph, with nodes
# and edges.
import graph

# loggers.py defines different Logger objects, which are used to control
# logging behaviors
import loggers


class WebCrawler(object):
    def __init__(self, max_threads, logger_class):
        self._number_of_running_threads = 0
        self.max_threads = max_threads
        self.queue = []
        self.currently_being_explored = set()
        self.graph = graph.WebsiteGraph()
        self.errors = []

        if logger_class:
            self.logger = logger_class(self)
        else:
            self.logger = loggers.SilentCrawlerLogger(self)

    def crawl(self, initial_url, output_file, display_results=True):
        if not initial_url.startswith("http"):
            initial_url = "http://" + initial_url

        print('initial_url', initial_url)

        initial_url_tuple = urlparse.urlparse(initial_url)
        self.domain = urlparse.urlunparse(
            (initial_url_tuple[0], initial_url_tuple[1], "", "", "", ""))

        self.main_thread = threading.current_thread()

        self._enqueue(initial_url)

        while self.queue or self.currently_being_explored:
            time.sleep(1)

        if display_results:
            print("\n\nDone crawling!")

            if not self.errors:
                print("No complaints found!")
            else:
                print("Here are all the complaints found:")
                for error in self.errors:
                    print(error)
            print("")

        if output_file:
            with open(output_file, "w") as f:
                json.dump(self.graph, f, default= lambda o: o.__dict__, indent=4)

        return self.graph

    def _enqueue(self, url):
        if url in self.graph.nodes:
            return

        self.graph.add_node(url)
        self.logger.enqueue(url)

        if self._number_of_running_threads < self.max_threads:
            self._number_of_running_threads += 1
            self._spawn_crawling_thread(url)
        else:
            self.queue.append(url)

    def _finalize_crawl(self, url):
        self.logger.finalize_crawl(url)
        self.currently_being_explored.remove(url)

        if self.queue:
            url = self.queue.pop()
            self._spawn_crawling_thread(url)
        else:
            self._number_of_running_threads -= 1

    def _spawn_crawling_thread(self, url):
        self.logger.spawn_crawling_thread(url)
        self.currently_being_explored.add(url)

        def crawl_url(url):
            if self.url_should_be_crawled_as_node(url):
                self._crawl_with_get_request(url)
            else:
                self._crawl_with_head_request(url)

        threading.Thread(target=crawl_url, args=(url,)).start()

    def url_should_be_crawled_as_node(self, url):
        url_tuple = urlparse.urlparse(url)
        domain_tuple = urlparse.urlparse(self.domain)

        # The result of urlparse.urlparse(url) is a tuple with the following six elements:
        #  scheme://netloc/path;parameters?query#fragment

        if url_tuple[1] != domain_tuple[1]:
            return False

        # prevent you from starting to crawl FTP if you're looking at HTTP
        if url_tuple[0] != domain_tuple[0]:
            return False

        filetype_list = ["pdf", "jpg", "gif", "js", "css", "png"]

        if url.split(".")[-1] in filetype_list:
            return False

        return True

    def _crawl_with_get_request(self, url):
        self.logger.crawl_with_get_request(url)

        node = self.graph.nodes[url]
        node.request_type = "get"
        print(node.request_type, 'request_type', 'get')

        try:
            # timeout after 10 seconds
            res = requests.get(url, timeout=10)
        except Exception as e:
            node.status = "failure"
            node.error = e
        else:
            if res.text and res.headers["Content-Type"].split("/")[0] == "text":
                (neighbors, errors) = html_helper.get_neighbors(res.text, res.url)

                self.errors.extend(errors)

                for neighbor_url in neighbors:
                    self.graph.add_neighbor(url, neighbor_url)
                    self._enqueue(neighbor_url)

            data = {"request_type": "get", "status": res.status_code}

            if res.status_code == 301:
                data["headers"] = res.headers

            node.status = "success"
            node.status_code = res.status_code
            node.contents = res.text

        self._finalize_crawl(url)

    def _crawl_with_head_request(self, url):
        self.logger.crawl_with_head_request(url)

        node = self.graph.nodes[url]
        node.request_type = "head"

        try:
            # timeout after 10 seconds
            response = requests.head(url, timeout=10)
        except Exception as e:
            node.status = "failure"
            node.error = e

            self.note_error("When crawling {0}, got a {1})".format(
                url,
                e)
            )
        else:
            node.status = "success"
            node.status_code = response.status_code

            if node.status_code >= 400:
                self.note_error("When crawling {0}, got a {1})".format(
                    url,
                    response.status_code)
                )

            self._finalize_crawl(url)

    def note_error(self, error):
        self.errors.append(error)
        self.logger.note_error(error)



