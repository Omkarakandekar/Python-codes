def counting_sort(alist, largest)

C = [0]*(largest + 1)

for i in range(len(alist)):

c [alist[i]] - [alist[i]] + 1

# Find the last index for each element
c [0] = [0] - 1 # to decrement each element for zero-based indexir
for i in range(1, largest + 1):
C[i] = c[i] + c[i - 1]
result
[None]*len(alist)
# Though it is not required here,
# it becomes necessary to reverse the list
# when this function needs to be a stable sort
for x in reversed(alist):
result(c[x]]
C[x] c[x] 1
х
return result
alist = input('Enter the list of (nonnegative) numbers: ').split()
alist = [int(x) for x in alist]
k = max(alist)
sorted_list = counting_sort(alist, k)
print('Sorted list: end='')
print(sorted_list)