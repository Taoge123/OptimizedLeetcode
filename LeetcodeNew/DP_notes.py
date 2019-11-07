"""DP notes
"""

"""
problem 1:

0 / 1 Knapsack 

total wt = 7 

items:

wt   val
1     1
3     4
4     5 
5     7 
 

val wt     1  2  3  4  5  6  7
(1)  1  0  1  1  1  1  1  1  1
(4)  3  0  1  1  4  5  5  5  5 
(5)  4  0  1  1  4  5  6  6  9 
(7)  5  0  1  1  4  5  7  8  9  

val wt     1  2  3  4  5  6  7
(1)  1  0- 1  1  1  1  1  1  1
(4)  3  0  1  1  4- 5  5  5  5 
(5)  4  0  1  1  4  5  6  6  9- 
(7)  5  0  1  1  4  5  7  8  9-

item 
(5) 4
(4) 3
--------
(9) 7

transition:
j is the weight 
i is the 

# i can't be used for j, else whe i can be used 
if j < wt[i]:
    T[i][j] = T[i-1][j]
else:
    T[i][j] = max(val[i] + T[i-1][j - wt[i]], T[i-1][j])
    
    
-----------------------------------------------------------------------------------------------
problem 2:
Longest Common Subsequence
a b c d a f 
a c b c f 
--------------   
a b c f
    
      a  b  c  d  a  f
   0- 0  0  0  0  0  0 
a  0  1- 1  1  1  1  1                          
c  0  1- 1  2  2  2  2                        
b  0  1  2- 2  2  2  2                       
c  0  1  2  3- 3- 3- 3                        
f  0  1  2  3  3  3  4-                    

if (s1[i] == s2[j]):
    T[i][j] = T[i-1][j-1] + 1
else:
    T[i][j] = max(T[i-1][j], T[i][j-1])



-----------------------------------------------------------------------------------------------
problem 3:
Matrix Mutilplication
   0      1      2     3 
 [2,3]  [3,6]  [6,4] [4,5]

from len = 1 all the way to len
[0,1][1,2][2,3]
2 * 3 * 6 = 36 
2 * 6 * 4 = 72 
6 * 4 * 5 = 120

[0,2]
0 + dp[1, 2]
2 * 3 * 4 + 72 = 96
[0, 1] + 2
36 + 2 * 6 * 4 = 84

[1,3]
1 + [2,3]
3 * 6 * 5 + 120 = 210 
[1,2] + 3
72 + 3 * 4 * 5 = 132

[0, 3]
[0,2] + 3
84 + 2 * 4 * 5 = 124
0 + [2,3]
2 * 3 * 5 + 120 = 150
    0    1    2    3
0   0   36   84   124         
1        0   72   132          
2             0   120        
3                  0       

T[i][j] = min(T[i][k] + T[K+1][j] + val[i].first * val[k].second * val[j].second)


-----------------------------------------------------------------------------------------------
problem 4:
Subset Sum Problem

    0  1  2  3  4  5  6  7  8  9  10  11 
 2  T  F  T  F  F  F  F  F  F  F  F   F                                      
 3  T  F  T- T  F  T  F  F  F  F  F   F                                       
 7  T  F  T- T  F  T  F  T  F  T  T   F                                      
 8  T  F  T  T  F  T  F  T  T  T  T   T-               
10  T  F  T  T  F  T  F  T  T  T  T   T-                                    

if (j < nums[i]):
    T[i][j] = T[i-1][j]
else:
    T[i][i] = T[i-1][j] || T[i-1][j-nums[i]]



-----------------------------------------------------------------------------------------------
problem 5:
Coin Changing Problem

coins - 1, 5, 6, 8
total - 11

    0  1  2  3  4  5  6  7  8  9  10  11   
1      1  2  3  4  5  6  7  8  9  10  11                                   
5      1  2  3  4  1  2  3  4  5  2   3                                   
6      1  2  3  4  1  1  2  3  4  2   2                                     
8      1  2  3  4  1  1  2  1  2  3   2                                    

if coins[i] <= j:
    T[i][j] = min(T[i-1][j], T[i][j-coins[i] + 1]) 
else:
    T[i][j] = T[i-1][j] 



-----------------------------------------------------------------------------------------------
problem 6:
Minimum Edit Distance
a b c d e f 

         *
a  b  c  d  e  f    
a  z  c  e  d
   b        f
--------------------
a  b  c  e  f


      a  b  c  d  e  f  
   0  1  2  3  4  5  6                  
a  1  0  1  2  3  4  5                   
z  2  1  1  2  3  4  5                   
c  3  2  2  1  2  3  4                  
e  4  3  3  2  2  2  3                  
f  5  4  4  3  2  3  3                

if s1[i] == s2[j]:
    T[i][j] = T[i-1][j-1]
else:
    T[i][j] = min(T[i-1][j], T[i][j-1], T[i-1][j-1]) + 1



-----------------------------------------------------------------------------------------------
problem 7:
Longest Increasing Subsequence

3 4 -1 0 6 2 3
 ----   ----

2 5 1 8 3 
----  --     

   j                        i 
   3   4   -1   0   6   2   3
   1   2   1    2   3   3   4                                    
                                   
for i in range(1, len):
    for j in range(0, i):
        if nums[j] < nums[i]:
            T[i] = max(T[i], T[j] + 1)




-----------------------------------------------------------------------------------------------
problem 8:
Optimal Binary Search Tree

   0    1    2    3 
  10   12   16   21           
  4    2    6    3         

     11(1)
  /       \
 10(2)    12(2)   

1 + 2 * 2 + 2 * 2 = 9


layer 1:
4 2 6 3

layer2:
[0, 1] = 6 + min(2, 4) = 8
[1, 2] = 8 + min(2, 6) = 10
[2, 3] = 9 + min(6, 3) = 12

layer3:
[0, 2] = 4 + 2 + 6 + min(10, 4 + 6, 8) = 20 
[1, 3] = 2 + 6 + 3 + min(12, 2 + 3, 10) = 16

layer4:
[0,3] = 4 + 2 + 6 + 3 + min(16, 4 + 12, 8 + 3, 20) = 26

    0   1   2   3  
0   4   8   20  26        
1       2   10  16       
2           6   12   
3               3  

       6 
    4     3
      2


-----------------------------------------------------------------------------------------------
problem 9:
Longest Palindromic Subsequence

0 1 2 3 4 5 
a g b d b a
-   - - - -

    0  1  2  3  4  5 
0   1  1  1  1  3  5         
1      1  1  1  3  3        
2         1  1  3  3       
3            1  1  1      
4               1  1     
5                  1                       
                   

if s[i] == s[j]:
    T[i][j] = T[i+1][j-1] + 1                 
else:
    T[i][j] = max(T[i+1][j], T[i][j-1])
                   

        
         
-----------------------------------------------------------------------------------------------
problem 9:
Cutting Rod to maxium profits

len = 5

1 2 3 4
2 5 7 8 

Option 1:
2 3 
5 7 = 12

Option 2:
1 2 2 
2 5 5 = 12 

      0  1  2  3  4  5
(2)1     2  4  6  8  10      
(5)2     2  5  7  10 12-       
(7)3     2  5  7  10 12-        
(8)4     2  5  7  10 12-        
                    
if (j >= i):
    T[i][j] = max(T[i-1][j], val[i] + T[i][j-i])                    
else:
    T[i][j] = T[i-1][j]



-----------------------------------------------------------------------------------------------
problem 11:
Coin Changing Number of ways to get total

coins 1 2 3   total = 5

   0  1  2  3  4  5  
1  1  1  1  1  1  1         
2  1  1  2  2  3  3                
3  1  1  2  3  4  5         
                     
if j >= coins[i]:
    T[i][j] = T[i-1][j] + T[i][j-coins[i]]
else:
    T[i][j] = T[i-1][j]                  
                     



-----------------------------------------------------------------------------------------------
problem 12:
Egg Dropping Dynamic Programming


   1  2  3  4  5  6
1  1  2  3  4  5  6                   
2  1  2  2  3  3  3              
[1, 3] 
1 + max(0,2) = 3
1 + max(1,1) = 2
1 + max(2,0) = 3

[1, 4]
1 + max(0, 2) = 3
1 + max(1, 2) = 3
1 + max(2, 1) = 3
1 + max(3, 0) = 4

[1, 5]
1 + max(0, 3) = 4
1 + max(1, 2) = 3
1 + max(2, 2) = 3
1 + max(3, 1) = 4
1 + max(4, 0) = 5

[1, 6]
1 + max(0, 3) = 4
1 + max(1, 3) = 4
1 + max(2, 2) = 3
1 + max(3, 2) = 5
1 + max(4, 1) = 6
1 + max(5, 0) = 6



#eggs more than floor 
if i > j:
    T[i][j] = T[i-1][j]
else:
    T[i][j] = 1 + max(T[i-1][k-1], T[i][j-k]) for k in range(i, j)

if breaks, i-1 eggs left and k-1 floors left
if doesn't, i eggs left and j-k floors left




-----------------------------------------------------------------------------------------------
problem 13:
Weighted Job Scheduling Dynamic Programming

  j                               i
(1,3)   (2,5)   (4,6)   (6,7)   (5,8)   (7,9)
  5       6       5       4       11      2
  5       6       10      14      17      16                                             
                                              
                                              
for i in range(1, len):
    for j in range(0, i):
        #do not overlap 
        if i.start >= j.end:
            T[i] = max(T[i], T[j] + profit[i])            

-----------------------------------------------------------------------------------------------
problem 14:
Regular Expression Dynamic Programming

* match 0 or more occurrence of charactoers before * 
. match nay single character

a.b 
acb aab axb -- True
ab  acby cb -- False

a*b.*y 
by, bly, ably, ablmy -- True
ay, ab -- False

if s[i] == pattern[j] or p[j] == '.':
    T[i][j] = T[i-1][j-1]
elif p[j] == '*':
    T[i][j] = T[i][j-2]
    if p[j-1] == s[i] or p[j-1] == '.':
        T[i][j] = T[i-1][j]
else:
    T[i][j] = False

     0  1  2  3  4  5  6 
        x  a  *  b  .  c
0    T  F  F  F  F  F  F   
1  x F  T  F  T  F  F  F                  
2  a F  F  T (T) F  F  F             
3  a F  F  F (T) F  F  F                 
4  b F  F  F  F  T  F  F                    
5  y F  F  F  F  F  T  F        
   c F  F  F  F  F  F  T         
            
x a * 
a          
                                         


-----------------------------------------------------------------------------------------------
problem 15:
Maximum Sum Rectangular Submatrix in Matrix dynamic programming/2D kadane







-----------------------------------------------------------------------------------------------
problem 16:
Longest Common Substring

a b c d a f 
  -----
z b c d f
-------

      a  b  c  d  a  f 
   0  0  0  0  0  0  0             
z  0  0  0  0  0  0  0                     
b  0  0  1  0  0  0  0                  
c  0  0  0  2  0  0  0                     
d  0  0  0  0 (3) 0  0                    
f  0  0  0  0  0  0  1                    

if s1[i] == s2[j]:
    T[i][j] = T[i-1][j-1] + 1
else:
    T[i][j] = 0



-----------------------------------------------------------------------------------------------
problem 17:
Maximum Size Rectangle of All 1's Dynamic Programming

   0  1  2  3  4  5 
0  1  0  0  1  1  1                 
1  1  0  1  1  0  1                  
2  0  1  1  1  1  1                  
3  0  0  1  1  1  1                  
             
             
    0  1  2  3  4  5 
    -----------------
0   1  0  0  1  1  1
1   2  0  1  2  0  2                
2   0  1  2  3  1  3                  
3   0  0  3  4  2  4                
      
maxArea = 8




-----------------------------------------------------------------------------------------------
problem 18:
Word Break Problem Dynamic Programming

0  1  2  3  4  5
I  a  m  a  c  e
-  ----  -------
I a m c                 
                 
   0  1  2  3  4  5             
0  T  T  T  T  F  T       
1     T  T  T  F  T    
2        T  F  F  F    
3           T  F  T    
4              T  F 
5                 T                 
                    
if word[i:j] in dictionary:
    T[i][j] = True
else:
    T[i][j] = True for k in T[i][k] and T[k+1][j] 
                      


                        

-----------------------------------------------------------------------------------------------
problem 19:
Buy/Sell Stock With K transactions To Maximize Profit Dynamic Programming

#case1 is not transacting on jth day
#case2 is completing transaction on jth day
T[i][j] = max(T[i][j-1],
              T[i-1][m] + price[j] - price[m] for m in range(0, j) )
              
              
T[i][j] = max(T[i][j-1],
              prices[j] + maxDiff
              maxDiff = max(maxDiff, T[i-1][j] - price[j]))
k = 3
row is transactions 

j = 3, i = 2
m = 0, T[1][0] - price[0] + price[3]
m = 1, T[1][1] - price[1] + price[3]
m = 2, T[1][2] - price[2] + price[3]

j = 4, i = 2
m = 0, T[1][0] - price[0] + price[4]
m = 1, T[1][1] - price[1] + price[4]
m = 2, T[1][2] - price[2] + price[4]
m = 3, T[1][3] - price[3] + price[4]

   0  1  2  3  4  5  6  7 
   2  5  7  1  4  3  1  3
0  0  0  0  0  0  0  0  0                         
1  0  3  5  5  5  5  5  5                    
2  0  3  5  5  8  8  8  8                      
3  0  3  5  5  8  8  8  10                     
                           
                             
                        
-----------------------------------------------------------------------------------------------
problem 20:
Minimum jump to reach end
   
   j                          i                      
   0  1  2  3  4  5  6  7  8  9
   2  3  1  1  2  4  2  0  1  1
                                 
   0  1  1  2  2  3  3  4  4  4                                         
                                
  -1  0  0  1  1  4  4  5  5  5

if i <= nums[j]:
    T[i] = min(T[i], T[j] + 1)



-----------------------------------------------------------------------------------------------
problem 21:
Minimum Cost Path Dynamic Programming 

--------
1 3 5 8| 
4 2 1 7|
4 3 2 3|


1 4 9 17 
5 6 7 14       
9 9 9 12

T[i][j] = val[i][j] + min(T[i-1][j], T[i][j-1])






-----------------------------------------------------------------------------------------------
problem 22:
Text Justification Dynamic Programming

0 Tushar - 6
1 Roy    - 3
2 like   - 5
3 to     - 2 
4 code   - 4

https://github.com/mission-peace/interview/blob/master/src/com/interview/dynamic/TextJustification.java


    0   1   2   3   4
0  16   0  inf inf inf                
1       49  1  inf inf       
2           25  4  inf      
3               64  9 
4                   36               
                 
         i  j
         9  36        
0  1  2  3  4                                       
         5  5      
0  1  2  3  4
              
               
C[][]

M[i] = min(M[j] + C[i][j-1]) for j in range(i+1, len)          
             
               

-----------------------------------------------------------------------------------------------
problem 23:


if s[i] == p[j] or p[j] == '?':
    T[i][j] = T[i-1][j-1]
elif p[j] == '*':
    T[i][j] = T[i-1][j] or T[i][j-1]
else:
    T[i][j] = False


     pattern 
     0   1   2   3   4   5 
         x   ?   y   *   z
0    T   F   F   F   F   F                    
1 x  F   T   F   F   F   F                  
2 a  F   F   T   F   F   F                  
3 y  F   F   F   T   T   F                  
4 l  F   F   F   F   T   F                    
5 m  F   F   F   F   T   F                    
6 z  F   F   F   F   T   T                  




-----------------------------------------------------------------------------------------------
problem 24:
Palindrome Partition Dynamic Programming

   0   1   2   3   4
   a   b   c   b   m
   
   
   0  1  2  3  4    
0  0  1  2  1  2         
1     0  1  0  1     
2        0  1  2     
3           0  1   
4              0     
   
if isPalindrome(i, j):
    T[i][j] = 0                
else:
    T[i][j] = 1 + min(T[i][k] + T[k+1][j]) for k in range(i, j-1)            
                      








                
"""
























