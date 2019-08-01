# def insertSort(L):
#     assert (type(L) == type(['']))
#     length = len(L)
#     if length <= 1:
#         return L
#
#     for i in range(1,length):
#         value=L[i]
#         j=i-1
#         while j>=0 and L[j]<value:
#             L[j+1]=L[j]
#             j-=1
#         L[j+1]=value
#         print(L)
#         # for i in range(length):
#         #     print(L[i], sep=' ', end='\n')
def insertSort(N):
    assert (type(N)) == type([''])
    length = len(N)
    if length <= 1:
        return N
    for i in range(1, length):
        minNo = N[i]
        j = i-1
        while j >= 0 and N[j] > minNo:
            N[j+1] = N[j]
            j -= 1
        N[j+1] = minNo
    print(N)


if __name__ == "__main__":
     a = [1, 7, 3, 6, 2, 6]
     insertSort(a)
