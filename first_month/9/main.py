# numbers = int(input("add number:: "))
# for i in range(1,numbers+1):
#     number = numbers - 2
#     if i == 1:
#         print(numbers * "1")
#     elif i == numbers:
#         print(numbers * "1")
#     else:
#         print(f"1{number*'0'}1")
#2

# numbers = int(input("add number:: "))
# counts = 1
# r = range(1,numbers+1)
# r = list(r)
# while numbers >= counts:
#         arr = r[:counts]
#         print(arr)
#         counts += 1
# 3
# numbers = int(input("add number:: "))
# counts = 0
# r = range(1,numbers+1)
# r = list(r)
# while numbers >= counts:
#         arr = str(r[counts])
#         print(r[counts]*arr)
#         counts += 1

# 4
# numbers = int(input("add number:: "))
# counts = [0,numbers]
# r = list(range(1,numbers+1))
# while numbers > counts[0]:
#     counts[0]+=1
#     print(f"{counts[1] * '0'}{r[:counts[0]]}")
#     counts[1]-=1
#5
# numbers = int(input("add number:: "))
# counts = 1
# r = list(range(1,numbers+1))
# while numbers >= counts:
#     s = r[-counts:]
#     print(s[::-1])
#     counts+=1
