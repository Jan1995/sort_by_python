# 冒泡排序算法 ，小詹个人公众号有相关介绍 ，详情请于 README.md 中查看
# 冒泡排序算法是两两相邻比较 ，两层嵌套循环 。外层每循环一次 ，冒泡排序排好一个数据
# 冒泡排序为原地稳定算法：
# 原地指空间复杂度为O（1) 
# 冒泡排序的平均和最坏情况下的时间复杂度皆为 O(n^2)；最好情况下是O（n)
# 作者 ：小詹，个人公众号——小詹学python

def Bubble_Sort(lists):
    """冒泡排序算法 1 ，两层嵌套，每一次i循环，将最大的数据冒泡到了最后"""
    if len(lists) <= 1:
        return lists
    for i in range(len(lists)):
        flag = False
        for j in range(0, len(lists) - i - 1):
            if lists[j] > lists[j+1]:
                lists[j], lists[j+1] = lists[j+1], lists[j]
                flag = True
        if(flag == False): #考虑过程中已经排好序就及时终止
            break
    return lists

# def Bubble_Sort(lists):
#     """冒泡排序算法 2 ，每一次i循环将最小的放到了最前，上边是放最大的到最后"""
#     for i in range(len(lists)):
#         for j in range(i+1, len(lists)):
#             if lists[i] > lists[j]:
#                 lists[i], lists[j] = lists[j], lists[i]
    
#     return lists

def main():
    """随便假设一个列表用于测试"""
    list_test = [5, 1, 8, 9, 0, 6, 3]
    
    Bubble_Sort(list_test)
    
    print(list_test)
    
if __name__ == '__main__':
    main()