from collections import Counter


col1 = []
col2 = []

with open("day1-input.txt", "r") as fp:
    while True:
        line = fp.readline()
        if not line:
            break
        num1, num2 = line.split()
        col1.append(int(num1))
        col2.append(int(num2))



col1 = sorted(col1)
col2_counter = Counter(col2)
print(col2_counter)

total = 0
for num in col1:
    total += num * col2_counter[num]
print(total)