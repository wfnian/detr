from operator import le
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(22)


class Kmeans():
    def __init__(self, k=2, data: list = []) -> None:
        assert k < len(data), 'Class is small than data'
        self.k = k
        # ~ stage 1
        self.center = []
        self.data = data
        while True:
            index = np.random.randint(len(data))
            if index in self.center:
                continue
            self.center.append(index)
            if len(self.center) == self.k:
                break
        print("first center={}".format(self.center))
        # ~ stage 2
        cluster = [[] for _ in range(self.k)]
        for i in range(len(data)):
            cluster_index = self.distance(data[i])
            cluster[cluster_index].append(i)
        # ~ stage 3
        self.center = self.update_center(cluster)
        print(self.center)
        print(cluster)
        # self.plt(cluster=cluster)

    def distance(self, elem):

        center = []
        for idx in range(self.k):
            center.append(self.data[self.center[idx]])
        val = np.inf
        for i in range(len(center)):
            dis = 0
            for j in range(len(elem)):
                dis += (center[i][j]-elem[j])**2
            if dis < val:
                val = dis
                min_index = i

        return min_index

    def update_center(self, cluster):

        for i in range(len(self.data[0])):
            for j in range(len(cluster)):
                val = 0
                for k in range(len(cluster[j])):
                    print(self.data[cluster[j][k]][i], end=" ")
                    val += self.data[cluster[j][k]][i]
                    pass
                print("update", val)
            print("fff")

    def plt(self, cluster):
        assert self.k < 4, f'dimision {self.k} is too large to plot'

        data = np.array(self.data)
        print()
        plt.plot(data[cluster[0]][:, 0], data[cluster[0]][:, 1], 'ro')
        plt.plot(data[cluster[1]][:, 0], data[cluster[1]][:, 1], 'go')
        plt.plot(data[self.center[0]][0], data[self.center[0]][1], 'b^')
        plt.plot(data[self.center[1]][0], data[self.center[1]][1], 'y^')

        pass


a = np.random.randint(1, 20, (7, 3))
print(a)

km = Kmeans(2, a)
# plt.xticks(range(20))
# plt.yticks(range(20))
# plt.grid()
# plt.show()
