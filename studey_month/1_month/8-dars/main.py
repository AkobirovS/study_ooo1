# data = [1, 2, 3, 3, 4, 23, 34, 9, 4, 5]

# a = list(range(0,9))
#
# a.insert(4, 4)
# a.insert(8, 4)

# data = input(f"ixtiyoriy sonlarni kiriting " " bilan ajratib ::: ")
#
# print(data.split(" "))
# newData = data.split(" ")
# newList = []
#
# for item in newData:
#     if int(item) != 4:
#         newList.append(item)
#
#
# print(newList)

# data = input(f"ixtiyoriy sonlarni kiriting " " bilan ajratib ::: ")
#
# print(data.split(" "))
# newData = data.split(" ")
# newList = []
# i = 0
#
# while i <= 10:
#     if int(newData[i]) != 4:
#         newList.append(newData[i])
#     i+=1
#
#
# print(newList)
#


data = input(f"ixtiyoriy sonlarni kiriting " " bilan ajratib ::: ")

print(data.split(" "))
newData = data.split(" ")
i = 0

while i < len(newData):

    if int(newData[i]) == 4:
        del newData[i]
        i -= 1
    i += 1

print(newData)
