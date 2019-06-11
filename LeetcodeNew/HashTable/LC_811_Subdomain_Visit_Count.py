import collections

class SolutionLee:
    def subdomainVisits(self, cpdomains):
        c = collections.Counter()
        for cd in cpdomains:
            n, d = cd.split()
            c[d] += int(n)
            for i in range(len(d)):
                if d[i] == '.':
                    c[d[i + 1:]] += int(n)
        return ["%d %s" % (c[k], k) for k in c]

    def subdomainVisits2(self, cpdomains):
        c = collections.Counter()
        for d in cpdomains:
            n, d = d.split()
            dots = d.count('.')
            for i in range(dots + 1):
                c[d.split('.', i)[i]] += int(n)
        return ["%d %s" % (c[k], k) for k in c]


class Solution2:
    def subdomainVisits(self, cpdomains):
        counter = collections.Counter()
        for cpdomain in cpdomains:
            count, *domains = cpdomain.replace(" ",".").split(".")
            for i in range(len(domains)):
                counter[".".join(domains[i:])] += int(count)
        return [" ".join((str(v), k)) for k, v in counter.items()]


class Solution3:
    def subdomainVisits(self, cpdomains):
        domain_counts = collections.defaultdict(int)
        for cpdomain in cpdomains:
            times, domains = cpdomain.split()
            times = int(times)
            domain_counts[domains] += times
            while '.' in domains:
                domains = domains[domains.index('.') + 1:]
                domain_counts[domains] += times
        return [str(v) + ' ' + d for d, v in domain_counts.items()]

class Solution4:
    def subdomainVisits(self, cpdomains):
        count = collections.Counter()
        for cpdomain in cpdomains:
            times, domain = cpdomain.split(" ")
            times = int(times)
            count[domain] += times
            for i, c in enumerate(domain):
                if c == '.':
                    count[domain[i + 1 : ]] += times
        return [str(times) + " " + domain for domain, times in count.items()]



