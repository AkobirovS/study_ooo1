# def RumNumbers(args: str) -> int:
#     args = args.lower()
#     over_ansers = {'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100, 'd': 500, 'm': 1000}
#     killler = 0
#     pre = 0
#     for i in args[::-1]:
#         total = over_ansers.get(i,0)
#         if total < pre:
#             killler -= total
#             print("hello ",killler)
#         else:
#             killler += total
#             print(killler)
#         pre = total
#     return killler
# print(RumNumbers("LVIII"))

def RumSum(arg: str) -> int:
    arg = arg.lower()
    over_ansers = {'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100, 'd': 500, 'm': 1000}
    over_el = 0
    lish_onswer = 0
    for i in arg[::-1]:
        answer = over_ansers.get(i,0)
        if lish_onswer > answer:
            over_el -= answer
        else:
            over_el += answer
        lish_onswer = answer

    return over_el
print(RumSum("LVIII"))

