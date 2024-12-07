from dataclasses import is_dataclass

import pytest

def is_valid_step(increasing: bool, prev_num, current_num):
    difference = abs(prev_num - current_num)
    if increasing:
        return prev_num < current_num and 1 <= difference <= 3
    else:
        return prev_num > current_num and 1 <= difference <= 3


def is_safe(nums: list[int], is_volatile: bool=False):
    is_increasing = None

    all_valid = True
    for idx, num in enumerate(nums):
        if idx == 0:
            continue

        prev_num = nums[idx - 1]
        if prev_num < num and is_increasing is None:
            is_increasing = True
        elif prev_num > num and is_increasing is None:
            is_increasing = False

        if not is_valid_step(is_increasing, prev_num, num):
            all_valid = False
            break
    if all_valid:
        return True

    # Question does only having one step wrong mean, we get rid of the previous and we are now fine?

def test_scenarios():
    assert is_safe([7, 6, 4, 2, 1])
    assert not is_safe([1, 2, 7, 8, 9])
    assert not is_safe([9, 7, 6, 2, 1])
    assert is_safe([1, 3, 2, 4, 5])
    assert is_safe([8, 6, 4, 4, 1])
    assert is_safe([1, 3, 6, 7, 9])
    assert is_safe([39, 42, 45, 43, 44])
    assert not is_safe([46, 44, 46, 46, 50])
    assert not is_safe([79, 86, 88, 87, 88])

def main():
    with open("day2-input.txt", "r") as fp:
        count = 0
        while True:
            line = fp.readline()
            if not line:
                break

            nums = [int(num) for num in line.split()]
            count += 1 if is_safe(nums) else 0

        print(count)

if __name__ == '__main__':
    main()