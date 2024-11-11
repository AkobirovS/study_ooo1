# # number = int(input("add the number: "))
# # arr = [4,5,2,8,6,2,815,6552,632,522,335]
# # arr = sorted(arr)
# # rights = len(arr)
# # left = 0
# # while left <= rights:
# #     mid = (rights + left)// 2
# #     if arr[mid] == number:
# #         print(number)
# #     elif arr[mid] < number:
# #         left = mid + 1
# #         print(mid)
# #     else:
# #         print(mid)
# #         rights = mid - 1
# #
#
#
# def bynery_search(number , arr):
#     arr = sorted(arr)
#     rights = len(arr)
#     left = 0
#     while rights >= left:
#         mid = (rights + left) // 2
#         if arr[mid] == number:
#             return mid
#         elif arr[mid] > number:
#             rights = mid - 1
#         else:
#             left = mid + 1
#     return -1

print("thing about number i can find it to 7 step :: ")
input("click enter if you redy:")
low = 1
high = 100
attempts = 0

while low <= high:
    mid = (low + high) // 2
    attempts +=1
    answer =  input(f"it is {mid}")
    answer = answer.lower()
    if answer == "y":
        print(f"answer id {mid} | step == {attempts}")
    elif answer == "b":
        low = mid + 1
    elif answer == "s":
        high = mid - 1
    else:
        print("please use only three letters:: y == yes , s == small , b == big your number")
