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
problem 10:
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
problem 10:
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
problem 11:
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









                   
"""
























