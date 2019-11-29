# graph.py contains the class which represents the website graph, with nodes
# and edges.

from __future__ import print_function


class WebsiteGraph:
    def __init__(self):
        self.nodes = {}
        self.outgoing_links = {}
        self.incoming_links = {}

    def add_node(self, url):
        self.nodes[url] = PageNode(url)

    def __getitem__(self, url):
        return self.nodes.get(url)

    def add_neighbor(self, from_url, to_url):
        if from_url not in self.outgoing_links:
            self.outgoing_links[from_url] = []

        if to_url not in self.incoming_links:
            self.incoming_links[to_url] = []

        self.outgoing_links[from_url].append(to_url)
        self.incoming_links[to_url].append(from_url)

    def parents(self, url):
        return self.incoming_links.get(url, [])


class PageNode:
    def __init__(self, url):
        self.url = url
        self.request_type = None
        self.status = None
        self.status_code = None
        self.contents = None
        self.error = None

    def __repr__(self):
        return "PageNode<{0} {1}, {2}, {3}>".format(
            self.url,
            self.status,
            self.status_code,
            self.request_type)
