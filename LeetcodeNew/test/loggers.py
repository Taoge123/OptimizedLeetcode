# loggers.py defines different Logger objects, which are used to control logging
# behaviors

from __future__ import print_function


class SilentCrawlerLogger:
    def __init__(self, crawler):
        self.crawler = crawler

    def enqueue(self, url):
        pass

    def finalize_crawl(self, url):
        pass

    def spawn_crawling_thread(self, url):
        pass

    def crawl_with_head_request(self, url):
        pass

    def crawl_with_get_request(self, url):
        pass

    def note_error(self, error):
        pass


class VerboseCrawlerLogger(SilentCrawlerLogger):
    def enqueue(self, url):
        print("url enqueued: {0}".format(url))

    def finalize_crawl(self, url):
        print("finalize crawl: {0}".format(url))

    def spawn_crawling_thread(self, url):
        print("spawning a crawler to look at: {0}".format(url))

    def crawl_with_head_request(self, url):
        print("crawling with HEAD request: {0}".format(url))

    def crawl_with_get_request(self, url):
        print("crawling with GET request: {0}".format(url))

    def note_error(self, error):
        print("Error! {0}".format(error))
