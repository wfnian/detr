import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)


class Kmeans():
    def __init__(self, k=2, data: list = []) -> None:
        assert k < len(data), 'Class is small than data'
        self.k = k
        center = []
        while True:
            index = np.random.randint(len(data))
            if index in center:
                continue
            center.append(index)
            if len(center) == self.k:
                break
        print(center)

        pass

    def plt(self):
        assert self.k < 4, f'{self.k} is too large to plot'
        pass


a = np.random.randint(1, 20, (20, 2))
# print(a)
# plt.plot(a[:, 0], a[:, 1], 'o')
# plt.xticks(range(20))
# plt.yticks(range(20))
# plt.grid()
# plt.show()
km = Kmeans(2, a)
