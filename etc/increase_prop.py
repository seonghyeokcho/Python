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


# EPOCHS = 1000
average_rates = []
TRIALS = 1000000
PRISONERS = 100

# for epoch in range(EPOCHS):
success_count = 0
boxes = list(range(1, PRISONERS + 1))
for _ in range(TRIALS):
    numbers = boxes.copy()
    random.shuffle(numbers)
    result = optimized_loop(boxes, numbers)
    if result == PRISONERS:
        success_count += 1
success_rate = success_count / TRIALS
# average_rates.append(success_rate)
    
    # if epoch % 10 == 0:
    #     print(f"Epoch: {epoch} | Success: {success_count} | Failure: {TRIALS - success_count} | Success Rate: {success_rate}")
# print(f"Average Success Rate for {EPOCHS} Epochs: {sum(average_rates)/len(average_rates)}")
print(f"Trials: {TRIALS} | Success: {success_count} | Failure: {TRIALS - success_count} | Success Rate: {success_rate}")