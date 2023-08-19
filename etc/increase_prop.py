# 확률 10^30 배 올리기 - loop strategy(루프 전략)
import random


def optimized_loop(boxes, numbers):
    count = 0
    pairs = {box: number for box, number in zip(boxes, numbers)}

    for box in boxes:
        choice = box
        for _ in range(len(boxes) // 2):
            choice = pairs[choice]
            if choice == box:
                count += 1
                break
        else:
            break

    return count

prisoner_numbers = 100
trials = 10000
success_count = 0

for _ in range(trials):
    boxes = list(range(1, prisoner_numbers + 1))
    numbers = boxes.copy()
    random.shuffle(numbers)
    result = optimized_loop(boxes, numbers)
    if result == prisoner_numbers:
        success_count += 1

success_rate = success_count / trials

print(f"Success: {success_count}")
print(f"Failure: {trials - success_count}")
print(f"Success Rate: {success_rate}")