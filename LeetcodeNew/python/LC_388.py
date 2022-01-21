"""

https://leetcode.com/problems/longest-absolute-file-path/discuss/354882/Recursive-solution

Suppose we abstract our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to file in the abstracted file system. If there is no file in the system, return 0.

Note:
The name of a file contains at least a . and an extension.
The name of a directory or sub-directory will not contain a ..
Time complexity required: O(n) where n is the size of the input string.

Notice that a/aa/aaa/file1.txt is not the longest file path, if there is another path aaaaaaaaaaaaaaaaaaaaa/sth.png.
"""


class Solution:
    def lengthLongestPath(self, input: str) -> int:

        table = {}
        res = 0
        fileList = input.split("\n")
        for file in fileList:
            if "." not in file:  # 是文件夹
                key = file.count("\t")  # 是几级文件夹
                value = len(file.replace("\t", ""))  # 除去\t后的长度，是实际长度
                table[key] = value
            else:  # 是文件。
                key = file.count("\t")
                # 　文件的长度：所有目录的长度＋文件的长度＋“\”的数量
                # temp = [table[k] for k in table.keys() if k < key]
                # length = sum([table[k] for k in table.keys() if k < key]) + len(file.replace("\t", "")) + key
                length = 0
                for k in table.keys():
                    if k < key:
                        length += table[k]
                length += len(file.replace("\t", ""))
                length += key
                res = max(res, length)
        return res



input = "dir\n\tsubdi111csdcsdvsvsdfvsdcvsdvdsr1\n\tsubdir2\n\t\tfile.ext"

a = Solution()
print(a.lengthLongestPath(input))


"""
825. Friends Of Appropriate Ages
"""









