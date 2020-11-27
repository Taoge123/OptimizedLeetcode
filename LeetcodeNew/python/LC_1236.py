import collections

class HtmlParser:
    def getUrls(self, url):
        pass

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser'):
        host = startUrl.split('//')[1].split('/')[0]
        res = set()
        self.dfs(startUrl, htmlParser, host, res)
        return res

    def dfs(self, url, htmlParser, host, res):
        if url in res:
            return
        curr_host = url.split('//')[1].split('/')[0]
        if curr_host == host:
            res.add(url)
        else:
            return
        for u in htmlParser.getUrls(url):
            self.dfs(u, htmlParser, host, res)




class Solution2:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        hostname = startUrl[:startUrl.find('/', startUrl.find('//') + 2)]
        queue = collections.deque()
        queue.append(startUrl)
        res = [startUrl]
        visited = set()
        visited.add(startUrl)
        while queue:
            url = queue.popleft()
            urls = htmlParser.getUrls(url)
            for u in urls:
                if u.find(hostname) >= 0 and u not in visited:
                    visited.add(u)
                    res.append(u)
                    queue.append(u)
        return res


