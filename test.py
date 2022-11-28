# count =  0
# while count <= 11:
#     print(count)
#     count += 1

# lastNumber = 6
# for row in range(0, lastNumber + 1):
#     for column in range(1, row + 1):
#         print(column, end=', ')
#     print(" ")

# sum = 0
# n = int(input("please enter number n "))
# for i in range(1, n+1, 1):
#     sum += i
# print("sum is: ", sum)

# num = 2
# for i in range(1, 11, 1):
#     mult = num * i
#     print(mult)

# list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
# for item in list1:
#     if item > 150:
#         break

#     if item % 5 == 0:
#         print(item)

# num = 75869
# count = 0
# while num != 0:
#     num //= 5
#     count+= 1
# print('total digits are: ', count)

total = 0
for i in range(1, 100):
    if i % 3 or 5  == 0:
        total += i
print(total)