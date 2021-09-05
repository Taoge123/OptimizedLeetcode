import collections

"""
{
f : 1
h : 1
i : 1
}

count2
{
f : 0
}

"""

s = "fhilawfncalndcjndfcilbdfnvhbfd"
count1 = {}
count2 = collections.defaultdict(int)

#for ch in s:
#     count1[ch] += 1
#
for ch in s:
    count1[ch] = count1.get(ch, 0) + 1

print(count1)





