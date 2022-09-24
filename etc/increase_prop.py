# 확률 10^30 배 올리기
import random


def solution(boxes, numbers):
    answer = []
    d = {}
    for k, v in zip(boxes, numbers):
        d[k] = v
    for i in boxes:
        link = i
        count = 0
        while count < 50:
            count += 1
            if d[link] == i:
                answer.append(True)
                break
            else: link = d[link]
        else: break
    return len(answer)

total = []
for i in range(5000):
    boxes = list(range(1, 101))
    numbers = boxes.copy()
    random.shuffle(numbers)
    result = solution(boxes, numbers)
    if result == 100:
        total.append(True)
    else:
        total.append(False)

print(float(sum(total)) / float(len(total)))