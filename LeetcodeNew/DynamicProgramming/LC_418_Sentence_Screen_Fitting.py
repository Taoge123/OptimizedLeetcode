
"""
https://leetcode.com/problems/sentence-screen-fitting/discuss/90869/Python-with-explanation
https://medium.com/@rebeccahezhang/leetcode-418-sentence-screen-fitting-9d6258ce116e


Given a rows x cols screen and a sentence represented by a list of non-empty words, find how many times the given sentence can be fitted on the screen.

Note:

A word cannot be split into two lines.
The order of words in the sentence must remain unchanged.
Two consecutive words in a line must be separated by a single space.
Total words in the sentence won't exceed 100.
Length of each word is greater than 0 and won't exceed 10.
1 ≤ rows, cols ≤ 20,000.
Example 1:

Input:
rows = 2, cols = 8, sentence = ["hello", "world"]

Output:
1

Explanation:
hello---
world---

The character '-' signifies an empty space on the screen.
Example 2:

Input:
rows = 3, cols = 6, sentence = ["a", "bcd", "e"]

Output:
2

Explanation:
a-bcd-
e-a---
bcd-e-

The character '-' signifies an empty space on the screen.
Example 3:

Input:
rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]

Output:
1

Explanation:
I-had
apple
pie-I
had--

The character '-' signifies an empty space on the screen.

"""
"""
Explanation:

Say sentence=["abc", "de", "f], rows=4, and cols=6.
The screen should look like

"abc de"
"f abc "
"de f  "
"abc de"
Consider the following repeating sentence string, with positions of the start character of each row on the screen.

"abc de f abc de f abc de f ..."
 ^      ^     ^    ^      ^
 0      7     13   18     25
Our goal is to find the start position of the row next to the last row on the screen, 
which is 25 here. Since actually it's the length of everything earlier, 
we can get the answer by dividing this number by the length of (non-repeated) sentence string. 
Note that the non-repeated sentence string has a space at the end; it is "abc de f " in this example.

Here is how we find that position. In each iteration, we need to adjust start based on spaces either added or removed.

"abc de f abc de f abc de f ..." // start=0
 012345                          // start=start+cols+adjustment=0+6+1=7 (1 space removed in screen string)
        012345                   // start=7+6+0=13
              012345             // start=13+6-1=18 (1 space added)
                   012345        // start=18+6+1=25 (1 space added)
                          012345
Hope this helps.
"""
"""
/** We can maintain a globe variable "lenSum" to record total length from first line to last line.
 * At the beginning of every iteration, we add total column length to "lenSum", then we can keep putting
 * words in current length.
 * The key step is to check whether last character is a space or an alphabet
 * 1. if it is a space, we do not need to trace back, since we already fill partial sentence in current line
 * 2. if it is an alphabet, we need to trace back to find the most recent space position
 * Overall, "lenSum" represents total effective length (有效长度), if the rest of line does not have enough
 * spots to fill out a word, we need to trace back to decrease the effective length. It means the rest of line
 * is ineffective length, which cannot be counted in "lenSum" */
 """
"""
Didn't realize the start of each row is always one of the words and never a space, until i saw this solution.

My understanding:

Based on the above observation, in the first for loop we compute the number of words 
that can be placed in the row if ith word is used as the starting word. 
This is saved as dp[i]. Note that this value can be greater than n.
In the next for loop we calculate how many words are placed in each row based on dp[i]. 
Imagine placing the 0th word in the row-0, then this row will hold dp[0] words. 
Next, which word will be placed on the start of next row? 
We calculate that using dp[k] % n (Remember dp[i] can be greater than n).
"""
"""
Given [‘AB’, ‘CDE’, ‘F’, …, ‘YZ’]
Width: w

1. join the words with empty space
2. get the index of the end of a screen line w - 1
there are 3 cases:

Case 1:
“AB-CDE-F-….-YZ” (‘-’ denotes a space)
reach to the space before F

Case 2:
“AB-CDE-F-…._YZ” (‘-’ denotes a space)
reach to exactly E

Case 3:
“AB-CDE-F-….-YZ” (‘-’ denotes a space)
reach to D

case 1, I can count one more bit and go to next line
case 2, I can count two more bits and go to next line
case 3, I have to move the cursor back until it reach to some space, and go to next line

When I go through all the rows, how many bits did I counted? Let’s say L, then the answer should be L / length of the string
"""

class Solution1:
    def wordsTyping(self, sentence, rows, cols):
        s = ' '.join(sentence) + ' '
        start = 0
        for i in range(rows):
            start += cols - 1
            if s[start % len(s)] == ' ':
                start += 1
            elif s[(start + 1) % len(s)] == ' ':
                start += 2
            else:
                while start > 0 and s[ (start - 1) % len(s) ] != ' ':
                    start -= 1
        return start / len(s)



class Solution2:
    def wordsTyping(self, sentence, rows, cols):
        s = ' '.join(sentence) + ' '
        start, l = 0, len(s)
        for i in range(rows):
            start += cols
            #means im in mid of some word, need to back to an empty space
            while s[start % l] != ' ':
                start -= 1
            start += 1
        return start / l


"""
Sentence Screen Fitting
> 类型: String
> Time Complexity: O(N)
> Space Complexity: O(1)
这题看了答案，具体操作把代码PO到这个网站跑一边就懂了。

大致就是用start来计算长度，想给Start赋予整个col的长度，然后在把start % len(s)，如果出现空格则对start进行缩减。
"""
class Solution3:
    def wordsTyping(self, sentence, rows, cols):
        s = ' '.join(sentence) + ' '
        start, l = 0, len(s)
        for i in range(rows):
            start += cols
            while s[start % l] != ' ':
                start -= 1
            start += 1
        return start // l


"""
Optimized Solution

- Iterate over every possible row
- Try to fill the row's columns with as many sentence characters as possible.
- Test the next character in sentence after filling cols character. Use modulo operator for this.
- If this is an " " string, then we are good. Otherwise move back till we get a " ".
- Now increment valid_ch_count by 1 to account for this " "
- Run the code for corner cases: s = "abc de " and col = 7. valid_ch_cnt = (0+7) = 7. 
  This points to 7%7 or s[0]. So we move back 1 and valid_ch_cnt becomes 6 
  and will point to last character which is " ". Then we increment to include this charcater.
- Similarly run a case for s = "abc de " and row=2 and col = 6. 
  Notice that "abc de" aligns with the column boundary. 
  But the valid_ch_count is still 7 after first row. 
  In the second row, we have valid_ch_count as 7 + 6 = 13. Finally it turns out to be 14 and 14/7 = 2. 
  Notice we do not take a modulo with cols, but with len(s) and hence get the right answer.
- This artimetic makes sure that valid_ch_count // len(s) gives the right answer.
"""
class Solution4:
    def wordsTyping(self, sentence, rows, cols):

        s, valid_ch_cnt = " ".join(sentence) + " ", 0
        for i in range(rows):
            valid_ch_cnt += cols
            while s[valid_ch_cnt%len(s)] != " ":
                valid_ch_cnt -= 1
            valid_ch_cnt += 1 # Add the empty space to count of valid characters
        return valid_ch_cnt // len(s)


"""
题目大意：
给定一个rows x cols屏幕与一列单词表示的句子，计算屏幕中可以展示多少次完整的句子。

注意：

单词不能拆成两行
单词在句子中的顺序不能调换
两个相邻单词之间必须有一个空格隔开
句子的总单词数不超过100
每个单词的长度不超过10
1 ≤ rows, cols ≤ 20,000.
"""
"""
解题思路：
由于rows和cols的规模可以达到20000，因此朴素的解法会超时（Time Limit Exceeded）

观察测试用例3可以发现，当句子在屏幕上重复展现时，会呈现周期性的规律：

I-had
apple
pie-I
had--
apple
pie-I
had--
apple
上例中apple单词的相对位置从第二行开始循环，因此只需要找到单词相对位置的“循环节”，即可将问题简化。

利用字典dp记录循环节的起始位置，具体记录方式为：dp[(pc, pw)] = pr, ans

以数对(pc, pw)为键，其中pw为单词在句子中出现时的下标，pc为单词出现在屏幕上的列数

以数对(pr, ans)为值，其中pr为单词出现在屏幕上的行数，ans为此时已经出现过的完整句子数
"""
class Solution5:
    def wordsTyping(self, sentence, rows, cols):

        wcount = len(sentence)
        wlens = map(len, sentence)
        slen = sum(wlens) + wcount
        dp = dict()
        pr = pc = pw = ans = 0
        while pr < rows:
            if (pc, pw) in dp:
                pr0, ans0 = dp[(pc, pw)]
                loop = (rows - pr0) / (pr - pr0 + 1)
                ans = ans0 + loop * (ans - ans0)
                pr = pr0 + loop * (pr - pr0)
            else:
                dp[(pc, pw)] = pr, ans
            scount = (cols - pc) / slen
            ans += scount
            pc += scount * slen + wlens[pw]
            if pc <= cols:
                pw += 1
                pc += 1
                if pw == wcount:
                    pw = 0
                    ans += 1
            if pc >= cols:
                pc = 0
                pr += 1
        return ans







