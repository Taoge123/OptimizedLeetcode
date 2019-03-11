
"""

Given a list accounts, each element accounts[i] is a list of strings,
where the first element accounts[i][0] is a name,
and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts.
Two accounts definitely belong to the same person if there is some email that is common to both accounts.
Note that even if two accounts have the same name,
they may belong to different people as people could have the same name.
A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format:
the first element of each account is the name,
and the rest of the elements are emails in sorted order.
The accounts themselves can be returned in any order.


Example 1:
Input:
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
Explanation:
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.




#Fantastic solution, aslo compared to redundunt connection
http://wulc.me/2017/10/12/LeetCode%20%E8%A7%A3%E9%A2%98%E6%8A%A5%E5%91%8A(684,685,721)-%E5%B9%B6%E6%9F%A5%E9%9B%86%E4%BB%8B%E7%BB%8D%E5%8F%8A%E5%BA%94%E7%94%A8/


http://www.cnblogs.com/grandyang/p/7829169.html
https://www.jianshu.com/p/ccaccc91d58e
https://blog.csdn.net/fuxuemingzhu/article/details/82913712

这个归组类的问题，最典型的就是岛屿问题(例如Number of Islands II)，很适合使用Union Find来做，
LeetCode中有很多道可以使用这个方法来做的题，
比如Friend Circles，Graph Valid Tree，Number of Connected Components in an Undirected Graph，
和Redundant Connection等等

都是要用一个root数组，每个点开始初始化为不同的值，如果两个点属于相同的组，
就将其中一个点的root值赋值为另一个点的位置，这样只要是相同组里的两点，通过find函数得到相同的值。
在这里，由于邮件是字符串不是数字，所以root可以用哈希map来代替，我们还需要一个哈希映射owner，
建立每个邮箱和其所有者姓名之前的映射，另外用一个哈希映射来建立用户和其所有的邮箱之间的映射，也就是合并后的结果。

首先我们遍历每个账户和其中的所有邮箱，先将每个邮箱的root映射为其自身，然后将owner赋值为用户名。
然后开始另一个循环，遍历每一个账号，首先对帐号的第一个邮箱调用find函数，得到其父串p，
然后遍历之后的邮箱，对每个遍历到的邮箱先调用find函数，将其父串的root值赋值为p，
这样做相当于将相同账号内的所有邮箱都链接起来了。我们下来要做的就是再次遍历每个账户内的所有邮箱，
先对该邮箱调用find函数，找到父串，然后将该邮箱加入该父串映射的集合汇总，这样就我们就完成了合并。
最后只需要将集合转为字符串数组，加入结果res中，通过owner映射找到父串的用户名，加入字符串数组的首位置

#BFS
然后我们还需要一个visited数组，来标记某个账户是否已经被遍历过，0表示为未访问，1表示已访问。
在建立好哈希map之后，我们遍历所有的账户，如果账户未被访问过，将其加入队列queue，新建一个集合set，
此时进行队列不为空的while循环，取出队首账户，将该该账户标记已访问1，
此时将该账户的所有邮箱取出来放入数组mails中，然后遍历mails中的每一个邮箱，将遍历到的邮箱加入集合set中，
根据映射来找到该邮箱所属的所有账户，如果该账户未访问，则加入队列中并标记已访问。当while循环结束后，
当前账户的所有合并后的邮箱都保存在集合set中，将其转为字符串数组，并且加上用户名在首位置，
最后加入结果res中即可

"""

"""
这道题目虽然也用到了并查集的数据结构，但是与前面的两道题目又有点不同，主要体现在两个方面

节点不再以数字标识，因此标识 parents 的数据结构要从 array 变为 map
不需要判断是否形成闭环，而要返回最终各个集合内的元素；在这个操作中需要注意的是不能直接利用存储各个节点的 
parent 的 map 直接为每个节点找到其 parent， 因为并非各个节点都进行了 path compression。
对应有两种方法 (1)借助 find 方法找到各个节点的parent (2) 
对存储各个节点的 parent 的 map 再进行一次 path compression, 
然后直接在 map 中找到各个节点的 parent 对应的方法入下
"""
import collections

class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        owners, parents = {}, {}
        for account in accounts:
            owners[account[1]] = account[0]
            for i in range(1, len(account)):
                parents[account[i]] = account[i]

        for account in accounts:
            p = self.find(account[1], parents)
            for i in range(1, len(account)):
                parents[self.find(account[i], parents)] = p

        unions = {}
        for account in accounts:
            for i in range(1, len(account)):
                p = self.find(account[i], parents)
                unions.setdefault(p, set())
                unions[p].add(account[i])

        result = []
        for k, v in unions.items():
            result.append([owners[k]] + sorted(v))
        return result

    def find(self, email, parents):
        if parents[email] != email:
            parents[email] = self.find(parents[email], parents)
        return parents[email]


class Solution2:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        owners, parents = {}, {}
        for account in accounts:
            owners[account[1]] = account[0]
            for i in range(1, len(account)):
                parents[account[i]] = account[i]

        for account in accounts:
            p = self.find(account[1], parents)
            for i in range(1, len(account)):
                parents[self.find(account[i], parents)] = p

        # not all paths are compressed currently
        for k, v in parents.items():
            if k != v:
                parents[k] = self.find(parents[v], parents)

        unions = {}
        for k, v in parents.items():
            if v not in unions:
                unions[v] = set()
            unions[v].add(k)

        result = []
        for k, v in unions.items():
            result.append([owners[k]] + sorted(v))
        return result

    def find(self, email, parents):
        if parents[email] != email:
            parents[email] = self.find(parents[email], parents)
        return parents[email]





class Solution(object):
    def accountsMerge(self, accounts):
        em_to_name = {}
        graph = collections.defaultdict(set)
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                graph[acc[1]].add(email)
                graph[email].add(acc[1])
                em_to_name[email] = name

        seen = set()
        ans = []
        for email in graph:
            if email not in seen:
                seen.add(email)
                stack = [email]
                component = []
                while stack:
                    node = stack.pop()
                    component.append(node)
                    for nei in graph[node]:
                        if nei not in seen:
                            seen.add(nei)
                            stack.append(nei)
                ans.append([em_to_name[email]] + sorted(component))
        return ans


#DFS
# https://leetcode.com/problems/accounts-merge/discuss/109194/Easy-python-solution-dfs

class Account:
    def __init__(self, l):
        self.name = l[0]
        self.emails = l[1:]

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        return self.name == other.name and len(self.emails) == len(other.emails) \
               and set(self.emails) == set(other.emails)

    def accountsMerge(self, accounts):
        accounts = [self.Account(a) for a in accounts]
        email_dict, visited, finalres = collections.defaultdict(set), set(), []

        for acc in accounts:
            for email in acc.emails:
                email_dict[email].add(acc)

        for acc in accounts:
            if acc in visited: continue
            res = set()
            self.dfs(acc, email_dict, visited, res)
            finalres.append([acc.name] + sorted(res))
        return finalres

    def dfs(self, acc, email_dict, visited, res):
        if acc in visited: return
        visited.add(acc)
        for email in acc.emails:
            res.add(email)
            for a in email_dict[email]:
                self.dfs(a, email_dict, visited, res)


