from __future__ import print_function

from webcrawler import WebCrawler
from loggers import VerboseCrawlerLogger
import unittest

class Challenge2Tests(unittest.TestCase):
    def test_challenge(self):
        crawler = WebCrawler(5, VerboseCrawlerLogger)
        crawler.crawl("http://triplebyte.github.io/web-crawler-test-site/test2", None, True)

        target_url = "http://triplebyte.github.io/web-crawler-test-site/test2/page2.html"

        self.assertIsNotNone(crawler.graph[target_url])

if __name__ == '__main__':
    unittest.main()
