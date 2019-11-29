from __future__ import print_function

from webcrawler import WebCrawler
from loggers import VerboseCrawlerLogger
import unittest

class Challenge4Tests(unittest.TestCase):
    def test_challenge(self):
        crawler = WebCrawler(5, VerboseCrawlerLogger)
        crawler.crawl("http://triplebyte.github.io/web-crawler-test-site/test4/", None, True)

        self.assertTrue("https://triplebyte.github.io/web-crawler-test-site/test4/page3" in crawler.graph.nodes)

if __name__ == '__main__':
    unittest.main()
