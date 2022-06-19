class Solution:
    def isValid(self, code: 'str') -> 'bool':
        CDATA_START = '![CDATA['
        CDATA_END = ']]>'
        code_len = len(code)

        # check the start
        if not code or code[0] != '<':
            return False

        tag, tag_len = self.findTag(code, code_len, 0)
        if tag is None or not self.isValidTag(tag, tag_len) or not code.startswith(
                '<' + tag + '>') or not code.endswith('</' + tag + '>'):
            return False

        stack = [tag]
        i = tag_len + 2
        while i < code_len:
            if code[i] == '<':
                tag, tag_len = self.findTag(code, code_len, i)

                if tag is None:
                    return False

                elif tag.startswith(CDATA_START):
                    while i < code_len - 3 and code[i:i + 3] != CDATA_END:
                        i += 1
                    if code[i:i + 3] != CDATA_END:
                        return False
                    i += 2

                elif tag.startswith('/'):
                    if not self.isValidTag(tag[1:], tag_len - 1) or not stack or stack.pop() != tag[1:]:
                        return False
                    i += tag_len + 1

                else:
                    if not self.isValidTag(tag, tag_len):
                        return False
                    stack.append(tag)
                    i += tag_len + 1
            i += 1

        return not stack

    def findTag(self, S, S_len, idx):
        tag, tag_len = None, 0
        for j in range(idx, S_len):
            if S[j] == '>':
                tag, tag_len = S[idx + 1:j], j - (idx + 1)
                break
        return tag, tag_len

    def isValidTag(self, tag, tag_len):
        return 1 <= tag_len <= 9 and all(c.isupper() for c in tag)


    
