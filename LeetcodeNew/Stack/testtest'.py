# class UseMainCode(object):
#     @classmethod
#     def RangeSize(cls, input1):
#         print(input1)
#         cls.convert(input1)
#
#     @classmethod
#     def convert(self, s):
#         res = 0
#         for i in s:
#             res = res*4 + ord(i)-ord('A')+1
#         print(res)
#         return res
#
# a = UseMainCode()
# a.RangeSize('A1:AA2')
#
#
#
#
class BrowserHistory:
    def __init__(self, homepage: str):
        self.index = 0
        self.queue = [homepage]

    def visit(self, url: str) -> None:
        self.index += 1
        if self.index < len(self.queue):
            self.queue[self.index] = url
            self.queue[self.index + 1:] = []
        else:
            self.queue.append(url)


    def back(self, steps: int) -> str:
        if self.index - steps >= 0:
            self.index -= steps
        return self.queue[self.index]

    def forward(self, steps: int) -> str:
        if self.index + steps < len(self.queue):
            self.index += steps
        return self.queue[self.index]


browserHistory = BrowserHistory("leetcode.com")
browserHistory.visit("google.com");       #// You are in "leetcode.com". Visit "google.com"
browserHistory.visit("facebook.com");     #// You are in "google.com". Visit "facebook.com"
browserHistory.visit("youtube.com");      #// You are in "facebook.com". Visit "youtube.com"
browserHistory.back(1);                   #// You are in "youtube.com", move back to "facebook.com" return "facebook.com"
browserHistory.back(1);                   #// You are in "facebook.com", move back to "google.com" return "google.com"
browserHistory.forward(1);                #// You are in "google.com", move forward to "facebook.com" return "facebook.com"
browserHistory.visit("linkedin.com");     #// You are in "facebook.com". Visit "linkedin.com"
browserHistory.forward(2);                #// You are in "linkedin.com", you cannot move forward any steps.
browserHistory.back(2);                   #// You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
browserHistory.back(7);

