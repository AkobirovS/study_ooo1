def Two_Sum(arg: list,target: int)-> list:
    dicts_nums = {}
    for i in range(len(arg)):
        dicts_nums[arg[i]] = i
    for i in range(len(arg)):
        over_el = target - arg[i]
        if over_el in dicts_nums and i != dicts_nums[over_el]:
            return [i , dicts_nums[over_el]]
print(Two_Sum([1,2,3,4,5,6,7], 9))