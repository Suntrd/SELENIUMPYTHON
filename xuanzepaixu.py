# 选择排序
def x_sort(a):
    l = len(a)
    for i in range(0, l-1):
        minNo = i
        for j in range(i, l-1):
            if a[minNo] > a[j+1]:
                minNo = j+1
        a[i],a[minNo] = a[minNo],a[i]
    for i in range(0,l):
        print(a[i],end=' ')

if __name__ == '__main__':
    n = [65,12,42,45,76,13,8,2,7,4,4,7,12]
    x_sort(n)