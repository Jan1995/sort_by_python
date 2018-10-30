# 选择排序算法 ，小詹个人公众号有相关介绍 ，详情请于 README.md 中查看
# 选择排序为原地但不稳定算法：
# 原地指空间复杂度为O（1) 
# 选择排序的最好情况、平均和最坏情况下的时间复杂度皆为 O(n^2)
# 作者 ：小詹，个人公众号——小詹学python

def Selection_Sort(lists):
    """选择排序算法，两层嵌套"""
    if len(lists) <= 1:
        return lists
    
    for i in range(len(lists)):
        min = i
        for j in range(i+1, len(lists)):
            if lists[min] >= lists[j]:
                min = j
        
        lists[min], lists[i] = lists[i], lists[min]

    return lists

def main():
    """随便假设一个列表用于测试"""
    list_test = [5, 1, 8, 9, 0, 6, 3]
    
    Selection_Sort(list_test)
    
    print(list_test)
    
if __name__ == '__main__':
    main()