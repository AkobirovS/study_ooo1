def remove_duplicates(nums):
    if not nums:  # Проверка на пустой массив
        return 0

    i = 0  # Указатель на последний уникальный элемент

    for j in range(1, len(nums)):
        if nums[j] != nums[i]:  # Находим новый уникальный элемент
            i += 1
            nums[i] = nums[j]  # Перемещаем его на позицию i

    return i + 1  # Количество уникальных элементов


# Пример использования
nums = [1, 1, 2, 3, 3, 4]
k = remove_duplicates(nums)
print(k)  # Вывод: 4
print(nums[:k])  # Вывод: [1, 2, 3, 4]



# lists = [1,4,2,5,6,4,4,4,4]
# counts = 0
# while 4 in lists:
#     if lists[counts] != 4:
#         counts += 1
#     else:
#         del lists[counts]
#         counts -= 1
# print(lists)