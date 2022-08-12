# a = ['a', 'b', 'c', '\0']
# def strlen(x):
#     i = 0
#     count = 0
#     while True:
#         if a[i] != '\0':
#             i += 1
#             count += 1
#         else:
#             break
#     return count
# print(strlen(a))

a = []
for i in range(1,10):
	a += [i]
print(a)