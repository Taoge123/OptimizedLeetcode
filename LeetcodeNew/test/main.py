from __future__ import print_function

import argparse
from webcrawler import WebCrawler
import loggers

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("target")
    parser.add_argument("--number_of_threads")
    parser.add_argument("--output_file")
    parser.add_argument("--verbose",
                        help="increase output verbosity",
                        action="store_true")

    args = parser.parse_args()

    webcrawler = WebCrawler(args.number_of_threads or 5,
                                  args.verbose and
                                  loggers.VerboseCrawlerLogger or
                                  loggers.SilentCrawlerLogger)

    webcrawler.crawl(args.target, args.output_file)

if __name__ == '__main__':
    main()
