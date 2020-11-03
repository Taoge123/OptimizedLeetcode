class Solution:
    def numUniqueEmails(self, emails) -> int:
        res = set()
        for email in emails:
            local, domain = email.split("@")
            local = "".join(local.split('+')[0].split('.'))
            email = local + '@' + domain
            res.add(email)
        return len(res)



