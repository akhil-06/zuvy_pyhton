a = [0,0,0,0,1,1,1,1,1,1,1,1,2,3,3,3,3,3,4,4,4,4,5,5,5,5,6];
n = len(a)
if n<=1:
    print(a)
# newL = [];
j = 1;
for i in range(1,n):
    if a[i] != a[i-1]:
        a[j] = a[i];
        j=j+1;

for i in range(0,j):
    print(a[i])







# a = [3,2,4]
# target = 6;
# n = len(a);

# for i in range(n):
#     for j in range(i+1, n):
#         if(a[i]+a[j] == target):
#             print(i,j)
#             break




# a = [10,-2,34,32,12,0,23,12,34,50,43,12,21]
# indexes = [];
# target = 122;
# for i in range(len(a)):
#     if a[i] == target:
#         indexes.append(i)
    
# print(indexes)



# a = [10,-2,34,32,12,0,23,12,34,50,43,12,21]
# largest  = a[0]
# # print(largest)
# for val in a:
#     if val > largest:
#         largest = val
# print(largest)