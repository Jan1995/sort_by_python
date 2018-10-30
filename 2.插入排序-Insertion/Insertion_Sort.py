# 插入排序算法 ，小詹个人公众号有相关介绍 ，详情请于 README.md 中查看
# 插入排序为原地稳定算法：
# 原地指空间复杂度为O（1) 
# 插入排序的平均和最坏情况下的时间复杂度皆为 O(n^2)；最好情况下是O（n)
# 作者 ：小詹，个人公众号——小詹学python

def Insertion_Sort(lists):
    """插入排序算法，两层嵌套"""
    if len(lists) <= 1:
        return lists
    
    for i in range(1, len(lists)):
        insert_num = lists[i] #从第二个数据开始找插入位置
        j = i - 1
        
        while j >= 0: #从后往前寻找插入位置
            if insert_num < lists[j]:
                lists[j+1] = lists[j]
                j -= 1
            else:
                break
            
        lists[j+1] = insert_num    
            
    return lists

def main():
    """随便假设一个列表用于测试"""
    list_test = [5, 1, 8, 9, 0, 6, 3]
    
    Insertion_Sort(list_test)
    
    print(list_test)
    
if __name__ == '__main__':
    main()