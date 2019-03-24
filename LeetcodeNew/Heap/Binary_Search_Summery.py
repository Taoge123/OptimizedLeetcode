
"""
http://www.cnblogs.com/grandyang/p/6854825.html

http://www.cnblogs.com/grandyang/p/4606334.html


"""

"""
第一类： 需查找和目标值完全相等的数

这是最简单的一类，也是我们最开始学二分查找法需要解决的问题，
比如我们有数组[2, 4, 5, 6, 9]，target = 6，那么我们可以写出二分查找法的代码如下：
int find(vector<int>& nums, int target) {
    int left = 0, right = nums.size();
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) return mid;
        else if (nums[mid] < target) left = mid + 1;
        else right = mid;
    }
    return -1;
}

会返回3，也就是target的在数组中的位置。注意二分查找法的写法并不唯一，主要可以变动地方有四处：

第一处是right的初始化，可以写成 nums.size() 或者 nums.size() - 1

第二处是left和right的关系，可以写成 left < right 或者 left <= right

第三处是更新right的赋值，可以写成 right = mid 或者 right = mid - 1

第四处是最后返回值，可以返回left，right，或right - 1

但是这些不同的写法并不能随机的组合，像博主的那种写法，若right初始化为了nums.size()，那么就必须用left < right，
而最后的right的赋值必须用 right = mid。但是如果我们right初始化为 nums.size() - 1，那么就必须用 left <= right，
并且right的赋值要写成 right = mid - 1，不然就会出错。所以博主的建议是选择一套自己喜欢的写法，并且记住，
实在不行就带简单的例子来一步一步执行，确定正确的写法也行。

Intersection of Two Arrays

"""
"""
第二类： 查找第一个不小于目标值的数，可变形为查找最后一个小于目标值的数

这是比较常见的一类，因为我们要查找的目标值不一定会在数组中出现，也有可能是跟目标值相等的数在数组中并不唯一，而是有多个，
那么这种情况下nums[mid] == target这条判断语句就没有必要存在。比如在数组[2, 4, 5, 6, 9]中查找数字3，就会返回数字4的位置；
在数组[0, 1, 1, 1, 1]中查找数字1，就会返回第一个数字1的位置。我们可以使用如下代码：

int find(vector<int>& nums, int target) {
    int left = 0, right = nums.size();
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] < target) left = mid + 1;
        else right = mid;
    }
    return right;
}

Heaters， Arranging Coins， Valid Perfect Square，Max Sum of Rectangle No Larger Than K，Russian Doll Envelopes
第二类变形应用：Valid Triangle Number
"""

"""
第三类： 查找第一个大于目标值的数，可变形为查找最后一个不大于目标值的数

这一类也比较常见，尤其是查找第一个大于目标值的数，在C++的STL也有专门的函数upper_bound，这里跟上面的那种情况的写法上很相似，
只需要添加一个等号，将之前的 nums[mid] < target 变成 nums[mid] <= target，就这一个小小的变化，其实直接就改变了搜索的方向，
使得在数组中有很多跟目标值相同的数字存在的情况下，返回最后一个相同的数字的下一个位置。比如在数组[2, 4, 5, 6, 9]中查找数字3，
还是返回数字4的位置，这跟上面那查找方式返回的结果相同，因为数字4在此数组中既是第一个不小于目标值3的数，也是第一个大于目标值3的数，
所以make sense；在数组[0, 1, 1, 1, 1]中查找数字1，就会返回坐标5，通过对比返回的坐标和数组的长度，
我们就知道是否存在这样一个大于目标值的数。

int find(vector<int>& nums, int target) {
    int left = 0, right = nums.size();
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] <= target) left = mid + 1;
        else right = mid;
    }
    return right;
}


这一类可以轻松的变形为查找最后一个不大于目标值的数，怎么变呢。我们已经找到了第一个大于目标值的数，那么再往前退一位，返回right - 1，
就是最后一个不大于目标值的数。比如在数组[0, 1, 1, 1, 1]中查找数字1，就会返回最后一个数字1的位置4，这在有些情况下是需要这么做的。

第三类应用实例：

Kth Smallest Element in a Sorted Matrix

第三类变形应用示例：

Sqrt(x)
"""


"""
第四类： 用子函数当作判断关系

这是最令博主头疼的一类，而且通常情况下都很难。因为这里在二分查找法重要的比较大小的地方使用到了子函数，
并不是之前三类中简单的数字大小的比较，比如Split Array Largest Sum那道题中的解法一，就是根据是否能分割数组来确定下一步搜索的范围。类似的还有Guess Number Higher or Lower这道题，是根据给定函数guess的返回值情况来确定搜索的范围。
对于这类题目，博主也很无奈，遇到了只能自求多福了。

第四类应用实例：

Split Array Largest Sum， Guess Number Higher or Lower，Find K Closest Elements，
Find K-th Smallest Pair Distance，Kth Smallest Number in Multiplication Table，
Maximum Average Subarray II，Minimize Max Distance to Gas Station，Swim in Rising Water


"""

"""
第五类： 其他

有些题目不属于上述的四类，但是还是需要用到二分搜索法，比如这道 Find Peak Element，求的是数组的局部峰值。
由于是求的峰值，需要跟相邻的数字比较，那么target就不是一个固定的值，而且这道题的一定要注意的是right的初始化，
一定要是nums.size() - 1，这是由于算出了mid后，nums[mid] 要和 nums[mid+1] 比较，
如果right初始化为nums.size()的话，mid+1可能会越界，从而不能找到正确的值。

第五类应用实例：

Find Peak Element"""


