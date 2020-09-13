"""
Given a non-empty string s and an integer k, rearrange the string
such that the same characters are at least distance k from each other.

All input strings are given in lowercase letters. If it is not possible to rearrange the string, return an empty string "".

Example 1:

Input: s = "aabbcc", k = 3
Output: "abcabc"
Explanation: The same letters are at least distance 3 from each other.
Example 2:

Input: s = "aaabc", k = 3
Output: ""
Explanation: It is not possible to rearrange the string.
Example 3:

Input: s = "aaadbbcc", k = 2
Output: "abacabcd"
Explanation: The same letters are at least distance 2 from each other.

构建priority_queue<pair<int,char>>q; q的元素表示字符及其频次。注意到priority_queue默认大顶堆，自动按照频次从大到小排列。

        unordered_map<char,int>Map;
        for (int i=0; i<s.size(); i++)
            Map[s[i]]++;

        priority_queue<pair<int,char>>q;
        for (auto a:Map)
            q.push({a.second,a.first});
每次取q中的前K个元素（每个元素代表不同的字符）加入临时数组temp；取完后将这些temp里的元素的个数减一后再放回q中。直至某一回合，如果pq的字符种类个数小于K，但是该轮结束后temp非空，说明我们还需要往result里加字符，这样就会违法K个相邻字符不能有相同字符的规则，返回空。

        while (!pq.empty())
        {
            int n = min(k, (int)pq.size());
            vector<pair<int,char>>temp;

            for (int i=0; i<n; i++)
            {
                int num = pq.top().first;
                int ch = pq.top().second;
                pq.pop();
                result+=ch;
                num--;
                if (num!=0) temp.push_back({num,ch});
            }
            if (n<k && temp.size()>0) return "";
            for (auto a:temp) pq.push(a);
        }
"""

import collections, heapq

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        n = len(s)
        wordCount = collections.Counter(s)
        heap = []
        heapq.heapify(heap)
        res = ""
        for word, count in wordCount.items():
            heapq.heappush(heap, (-count, word))

        while heap:
            loop = min(n, max(1, k))
            used = []
            for i in range(loop):
                if not heap:
                    return ""
                count, word = heapq.heappop(heap)
                res += word
                if -count > 1:
                    used.append((count + 1, word))
                n -= 1
            for use in used:
                heapq.heappush(heap, use)
        return res





