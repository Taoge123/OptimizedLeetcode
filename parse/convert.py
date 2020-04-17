
import os


prefix = '/Users/taocheng/.Trash/'
# queue = ['']
# while queue:
#     node = queue.pop(0)
#     newNode = os.listdir(node)

file = '/Users/taocheng/.Trash/test/AD-MACE-Core/src/Common/Utils/EnvironmentDescriptors.cs'

file1 = open('/Users/taocheng/PycharmProjects/parse/test/ID-MACE/src/LinkedInAccountService/LinkedInAccountService.txt', 'rU',  encoding='utf8')
Lines = file1.readlines()

count = 0
stack = []
for line in Lines:
    if line.startswith('test'):
        line = "/".join(line.strip().split('\\'))
        line = prefix + line
        stack.append(line)
        print(line)
    else:
        stack.append(line)
        print(line)
    print(line)

for i, line in enumerate(stack):
    # if
    if line.startswith('/User'):
        file = open(line, 'r')
        temp = file.readlines()
        print(temp)



