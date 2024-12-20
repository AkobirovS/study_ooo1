number_1 = int(input(":: "))
number_2 = int(input(":: "))
number_3 = number_2 * number_1
counts = []
for i in range(1,number_3):
    if i%number_2==0:
        counts.append(i)
        print(i)
        print(counts)