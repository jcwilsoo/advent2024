import re


actions = []
with open('day3-input.txt', 'r') as fp:
    while True:
        line = fp.readline()
        if not line:
            break
        found = re.findall(r'(mul\(\d{1,3},\d{1,3}\))|(don\'t\(\))|(do\(\))', line)
        for pattern in found:
            action = [action for action in pattern if action]
            print(action)
            actions.append(action[0])

enabled = True
total = 0
for action in actions:
    if action == "do()":
        enabled = True
    elif action == "don't()":
        enabled = False
    else:
        if enabled is True:
            num1, num2 = [int(num) for num in action[4:-1].split(',')]
            total += (num1 * num2)
        else:
            print(f"SKIPPED {action}")

print(total)


