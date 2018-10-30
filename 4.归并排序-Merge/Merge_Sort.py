# 归并排序算法 ，小詹个人公众号有相关介绍 ，详情请于 README.md 中查看
# 归并排序为非原地但稳定算法：
# 归并排序的最好情况、最坏情况，还是平均情况，时间复杂度都是 O(nlogn)
#递归思路
# 作者 ：小詹，个人公众号——小詹学python

def Merge(left, right):
    """
    分支思想，将两部分融合，这个函数是合并两个片段
    """
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def Merge_Sort(lists):
    """ 归并排序算法利用递归
        递推公式：
        Merge_Sort(p…r) = Merge(Merge_Sort(p…q), Merge_Sort(q+1…r))

        终止条件：
        p >= r 不用再继续分解
    """
    if len(lists) <= 1:
        return lists
    
    num = len(lists) // 2    
    
    left = Merge_Sort(lists[:num])
    right = Merge_Sort(lists[num:])
    
    return Merge(left, right)

def main():
    """随便假设一个列表用于测试"""
    list_test = [5, 1, 8, 9, 0, 6, 3]
    
    list_test = Merge_Sort(list_test)
    
    print(list_test)
    
if __name__ == '__main__':
    main()