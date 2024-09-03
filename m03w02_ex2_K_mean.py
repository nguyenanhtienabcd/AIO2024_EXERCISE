from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


class Kmean:
    def __init__(self, k, max_iter=100):
        self.k = k
        self.max_iter = max_iter
        self.centroids = None
        self.clusters = None

    # khởi tạo điểm trung tâm ban đầu bằng cách random dữ liệu đã có

    def centroids_init(self, data):
        # lấy random một vài mẫu, tuy nhiên các mẫu này sẽ không thay đổi khi chạy lại chương trình
        # np.random.seed(42) (đây là quy chuẩn cũ)
        rng = np.random.default_rng(42)  # (quy chuẩn mới)
        return data[rng.choice(data.shape[0], self.k, replace=False)]

    # tính khoảng cách giữa hai điểm bằng công thức euclidean
    def distance(self, x1, x2):
        return np.sqrt(np.sum((x1 - x2)**2))

    # gom cụm lại
    def assign_clusters(self, data):
        distances = np.array([[self.distance(x, centroid)
                             for centroid in self.centroids] for x in data])
        return np.argmin(distances, axis=1)

    # bắt đầu update centroid

    def update_centroids(self, data):
        # tại sao lại là self,clusters mà không phải self.assign_cluster(data)
        # lý do bởi vì: selt.cluster được cập nhật theo từng vòng lặp của interation để tìm ra điểm trung tâm tối ưu nhất
        new_centroids = np.array(
            [np.mean(data[self.clusters == i], axis=0) for i in range(self.k)])
        return new_centroids

    # tạo vòng lặp cho khối dữ liệu và sau đó
    def fit(self, data):

        # tạo ngẫu nhiêm điểm trung tâm cho từng cụm
        self.centroids = self.centroids_init(data)

        self.clusters = self.assign_clusters(data)

        # self.plot_clusters(data, 0)
        for _ in range(self.max_iter):

            # gán cụm với datapoint gần nhất
            self.clusters = self.assign_clusters(data)

            # cập nhật giá trị centroid sau những lần thay đổi
            new_centroids = self.update_centroids(data)

            # vẽ lại biểu đồ của mỗi vòng lặp
            # self.plot_clusters(data, i+1)

            if np.all(self.centroids == new_centroids):
                break

            self.centroids = new_centroids
            # self.plot_clusters(data, i)

        self.plot_final_clusters(data)

        # trả về kết quả cuối cùng
        return self.centroids, self.clusters

    def plot_clusters(self, data, iteration):
        plt.scatter(data[:, 0], data[:, 1], c=self.clusters,
                    cmap='rainbow', marker='o', alpha=0.6)
        plt.scatter(
            self.centroids[:, 0], self.centroids[:, 1], c='black', marker='x', s=300)
        plt.title(f"Iteration {iteration+1}")
        plt.xlabel('Sepal length')
        plt.ylabel('Sepal width')
        plt.show()

    def plot_final_clusters(self, data):
        plt.scatter(data[:, 0], data[:, 1], c=self.clusters,
                    cmap='viridis', marker='o', alpha=0.6)
        plt.scatter(
            self.centroids[:, 0], self.centroids[:, 1], s=300, c='red', marker='x')
        plt.title("Final Clusters and Centroids")
        plt.xlabel('Sepal length')
        plt.ylabel('Sepal width')
        plt.show()


if __name__ == "__main__":
    iris_dataset = load_iris()
    data = iris_dataset.data
    # lấy 2 features đầu để thực hiện phân cụm bằng k-mean
    data = iris_dataset.data[:, :2]
    kmeans = Kmean(k=2)
    kmeans.fit(data)
    print(kmeans.fit(data))

    data1 = np.array([
        [2.0, 3.0, 1.5],
        [3.0, 3.5, 2.0],
        [3.5, 3.0, 2.5],
        [8.0, 8.0, 7.5],
        [8.5, 8.5, 8.0],
        [9.0, 8.0, 8.5],
        [1.0, 2.0, 1.0],
        [1.5, 2.5, 1.5]])
    kmeans = Kmean(k=3)
    kmeans.fit(data1)
    print(kmeans.fit(data1))
