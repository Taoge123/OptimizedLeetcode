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



class SolutionRika:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser'):
        index = startUrl[7:].find('/')  # find index of first'/' in urls without "http://"

        hostname = startUrl[:index]

        visited = set()
        visited.add(startUrl)
        if len(htmlParser.getUrls(startUrl)) != 0:
            self.dfs(startUrl, htmlParser, hostname, visited)
        return list(visited)

    def dfs(self, startUrl, htmlParser, hostname, visited):
        if len(htmlParser.getUrls(startUrl)) == 0:
            return
        for nxtUrl in htmlParser.getUrls(startUrl):
            if hostname in nxtUrl and nxtUrl not in visited:
                visited.add(nxtUrl)
                self.dfs(nxtUrl, htmlParser, hostname, visited)




class Solution2:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser'):
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


