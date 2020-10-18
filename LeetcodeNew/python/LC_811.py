
import collections

class Solution:
    def subdomainVisits(self, cpdomains):
        # Use counter for the subdomain counts.
        table = collections.Counter()
        for node in cpdomains:
            # split the count and full domain.
            num, domain = node.split(' ')
            # Break the domain out.
            subs = domain.split('.')
            # For the different subs in our domain, join with all the other subs following it.
            for i in range(len(subs)):
                # Update the counts.
                table['.'.join(subs[i:])] += int(num)
            # Retuen the count and domains.
        return [f'{v} {k}' for k, v in table.items()]


cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
a = Solution()
print(a.subdomainVisits(cpdomains))

