from __future__ import print_function

from webcrawler import WebCrawler
from loggers import VerboseCrawlerLogger
import unittest

class Challenge3Tests(unittest.TestCase):
    def test_challenge(self):
        # The bug here is that the crawler will hang. Don't sit around waiting
        # for it to finish!
        crawler = WebCrawler(5, VerboseCrawlerLogger)
        crawler.crawl("http://triplebyte.github.io/web-crawler-test-site/test3/", None, True)

        self.assertIn(
            "http://blah.com:7091",
            crawler.graph.nodes
        )

if __name__ == '__main__':
    unittest.main()
