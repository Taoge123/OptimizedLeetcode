from __future__ import print_function

from webcrawler import WebCrawler
from loggers import VerboseCrawlerLogger
import unittest

class Challenge1Tests(unittest.TestCase):
    def test_challenge(self):
        crawler = WebCrawler(5, VerboseCrawlerLogger)
        crawler.crawl("triplebyte.github.io/web-crawler-test-site/test1",
                      None,
                      True)

        url = "http://triplebyte.github.io/web-crawler-test-site/test1/SVG_logo.svg"
        self.assertEqual(crawler.graph[url].request_type, "head")

if __name__ == '__main__':
    unittest.main()
