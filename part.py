import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 100)


def partition(number):
    answer = set()
    answer.add((number,))
    for x in range(1, number):
        for y in partition(number - x):
            if(x == 2):
                return
            answer.add(tuple(sorted((x,) + y)))

    return answer



for i in range(1, 25):
    print(i)
    print(len(partition(i)))
