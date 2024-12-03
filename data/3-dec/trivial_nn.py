import time
import random

train = [(0,0),
         (1,2),
         (2,4),
         (3,6),
         (4,8)]

def err(a, b):
    return (a - b)**2

def cost(w):
    c = 0
    for x, y in train:
        pred = x * w
        c += err(y, pred)
    return c / len(train)


if __name__ == "__main__":
    # y = x * w
    w = random.random() * 10.0
    epochs = 500
    epsilon = 0.01
    lr = 0.001
    losses = []
    for e in range(epochs):
        losses.append(cost(w))
        dcost = (cost(w + epsilon) - cost(w)) / epsilon 
        w -= lr * dcost
        if (e + 1) % 11 == 0:
            print(f'Epoch {e}, Value = {w:.8f}, Cost = {cost(w):.5f}')
