# 快速排序算法 ，小詹个人公众号有相关介绍 ，详情请于 README.md 中查看
# 快速排序为原地但不稳定算法：
# 快速排序的最好情况、最坏情况，还是平均情况，时间复杂度都是 O(nlogn)
# 递归思路
# 作者 ：小詹，个人公众号——小詹学python


def Quick_Sort(lists):
    """ 快速排序算法利用递归：
    
        递推公式：
        quick_sort(p…r) = quick_sort(p…q-1) + quick_sort(q+1, r)

        终止条件：
        p >= r

    """
    quicksortHelper(lists, 0, len(lists)-1)
    
def quicksortHelper(lists, left, right):
    """辅助函数"""
    if len(lists) <= 1:
        return lists
    
    if left < right:
        pivotLocation = partion(lists, left, right)
        quicksortHelper(lists, left, pivotLocation - 1)
        quicksortHelper(lists, pivotLocation + 1, right)

def partion(lists, left, right):
    """
    寻找基准位置pivot
    并把小于基准值和大于基准值的元素放到pivot两边
    """
    #找到中间元素并和最末尾交换
    middle = (left + right) // 2
    
    pivot = lists[middle]
    lists[middle], lists[right] = lists[right], pivot
    
    #从首处开始边界索引
    boundary = left
    
    #把所有小于基准的元素交换到边界左边
    for index in range(left, right):
        if lists[index] < pivot:
            lists[index], lists[boundary] = lists[boundary], lists[index]
            boundary += 1
    
    #交换边界位置元素和基准元素，得到基准元素右边都是大于基准值的元素
    lists[right], lists[boundary] = lists[boundary], lists[right]
    
    return boundary
    
    
def main():
    """随便假设一个列表用于测试"""
    list_test = [5, 1, 8, 9, 0, 6, 3]
    
    Quick_Sort(list_test)
    
    print(list_test)
    
if __name__ == '__main__':
    main()