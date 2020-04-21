#!/usr/bin/python
# coding=utf-8
from numpy import *
import numpy as np
import matplotlib.pyplot as plt

# 加载数据
def loadDataSet(fileName):  # 解析文件，按tab分割字段，得到一个浮点数字类型的矩阵
    dataMat = []              # 文件的最后一个字段是类别标签
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        #print(curLine)
        fltLine = list(map(float, curLine))     # 将每个元素转成float类型
        dataMat.append(fltLine)
    return dataMat

# 计算欧几里得距离
def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2)))  # 求两个向量之间的距离

# 构建聚簇中心，取k个(此例中为4)随机质心
def randCent(dataSet, k):
    n = shape(dataSet)[1]
    centroids = mat(zeros((k, n)))   # 每个质心有n个坐标值，总共要k个质心
    for j in range(n):
        minJ = min(dataSet[:, j])
        maxJ = max(dataSet[:, j])
        rangeJ = float(maxJ - minJ)
        centroids[:, j] = minJ + rangeJ * random.rand(k, 1)
    return centroids

# k-means 聚类算法
def kMeans(dataSet, k, distMeans =distEclud, createCent = randCent):
    m = shape(dataSet)[0]
    clusterAssment = mat(zeros((m,2)))    # 用于存放该样本属于哪类及质心距离
    # clusterAssment第一列存放该数据所属的中心点，第二列是该数据到中心点的距离
    centroids = createCent(dataSet, k)
    clusterChanged = True   # 用来判断聚类是否已经收敛
    while clusterChanged:
        clusterChanged = False
        for i in range(m):  # 把每一个数据点划分到离它最近的中心点
            minDist = inf
            minIndex = -1
            for j in range(k):
                distJI = distMeans(centroids[j,:], dataSet[i,:])
                if distJI < minDist:
                    minDist = distJI; minIndex = j  # 如果第i个数据点到第j个中心点更近，则将i归属为j
            if clusterAssment[i,0] != minIndex: clusterChanged = True  # 如果分配发生变化，则需要继续迭代
            clusterAssment[i,:] = minIndex,minDist**2   # 并将第i个数据点的分配情况存入字典
        print(centroids)
        for cent in range(k):   # 重新计算中心点
            ptsInClust = dataSet[nonzero(clusterAssment[:,0].A == cent)[0]]   # 去第一列等于cent的所有列
            centroids[cent,:] = mean(ptsInClust, axis=0)  # 算出这些数据的中心点
    return centroids, clusterAssment

# 取数据的前两维特征作为该条数据的x , y 坐标，
def getXY(dataSet):
    m = shape(dataSet)[0]  # 数据集的行
    X = []
    Y = []
    for i in range(m):
        X.append(dataSet[i,0])
        Y.append(dataSet[i,1])
    #print(X,Y)
    return np.array(X), np.array(Y)

# 数据可视化
def showCluster(dataSet, k, clusterAssment, centroids):
    fig = plt.figure()
    plt.title("K-means")
    ax = fig.add_subplot(111)
    data = []

    for cent in range(k):  # 提取出每个簇的数据
        ptsInClust = dataSet[nonzero(clusterAssment[:,0].A==cent)[0]] #获得属于cent簇的数据
        data.append(ptsInClust)

    for cent, c, marker in zip(range(k), ['r', 'g', 'b', 'y'], ['^', 'o', '*','s']):  # 画出数据点散点图
        X, Y = getXY(data[cent])
        ax.scatter(X, Y, s=80, c=c, marker=marker)
    centroidsX, centroidsY = getXY(centroids)
    ax.scatter(centroidsX, centroidsY, s=3000, c='black', marker='+', alpha=1)  # 画出质心点
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    plt.show()



# --------------------测试----------------------------------------------------
# 用测试数据及测试kmeans算法
datMat = mat(loadDataSet('C:/Users/KerryChen/OneDrive/桌面/11.txt'))
cluster_Num = 3
centroids, clusterAssment = kMeans(datMat, cluster_Num)
print(centroids,clusterAssment)
showCluster(datMat, cluster_Num, clusterAssment, centroids)
