



class Solution:
    def removeComments(self, source):

        res, buffer, isOpen = [], '', False
        for line in source:
            i = 0
            while i < len(line):
                char = line[i]
                # "//" -> Line comment.
                if (i + 1) < len(line) and line[i:i + 2] == '//' and not isOpen:
                    break  # Advance pointer to end of current line.
                # "/*" -> Start of block comment.
                elif (i + 1) < len(line) and line[i:i + 2] == '/*' and not isOpen:
                    isOpen = True
                    i += 1
                # "*/" -> End of block comment.
                elif (i + 1) < len(line) and line[i:i + 2] == '*/' and isOpen:
                    isOpen = False
                    i += 1
                # Normal character. Append to buffer if not in block comment.
                elif not isOpen:
                    buffer += char
                i += 1
            if buffer and not isOpen:
                res.append(buffer)
                buffer = ''
        return res




source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
a = Solution()
print(a.removeComments(source))



