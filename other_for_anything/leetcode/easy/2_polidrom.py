def Polimdrom(num: int) -> bool:
    pod = str(num)
    pod = pod[::-1]
    return True if pod == str(num) else False
print(Polimdrom(-121))