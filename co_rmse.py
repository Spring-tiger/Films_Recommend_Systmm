import random
import math
import time


def InitLFM(k):
    """
    :param k: 选定的维度
    :return:  已初始化的P,Q矩阵（字典）
    """
    p = dict()
    q = dict()
    for uid in range(19835):
        p[uid] = [random.random()/math.sqrt(k) for x in range(0, k)]
    for mid in range(624961):
        q[mid] = [random.random()/math.sqrt(k) for x in range(0, k)]
    return p, q


def Predict(u, i, p, q):
    """
    :param u: 用户编号
    :param i: 电影编号
    :param p: P(m*k)
    :param q: Q(n*k)
    :return: 用户u对电影i评分的预测值
    """
    return sum(p[u][f] * q[i][f] for f in range(0, len(p[u])))


def LearningLFM(train, k, n, alpha, dea):
    """
    :param train:  划分后的训练集，为原始训练集的9/10
    :param k: 选定的维度
    :param n: 迭代次数
    :param alpha: 学习率（步长）
    :param dea:   正则化参数
    :return: 训练后的矩阵P,Q
    """
    p, q = InitLFM(k)
    print('init finished')
    for step in range(0, n):
        print('迭代次数：', step)
        for t in range(len(train)):
            u, i, rui, nu = train[t].split('  ')
            u, i, rui = int(u), int(i), float(rui)
            pui = Predict(u, i, p, q)
            eui = rui - pui
            for f in range(0, k):
                p[u][f] += alpha * (q[i][f] * eui - dea * p[u][f])
                q[i][f] += alpha * (p[u][f] * eui - dea * q[i][f])
        alpha *= 0.9  # 在每一步对步长进行衰减(alpha *= 0.9)，以便更快收敛
    return p, q


if __name__ == '__main__':
    train0 = open('D:\data\data-new/mytrain0.txt', 'r+')
    train_set0 = train0.readlines()
    train0.close()
    p, q = LearningLFM(train_set0, 15, 20, 0.0001, 0.01)
    print('got P,Q')
    test = open('D:\data\data-new/mytest0.txt', 'r+')
    test_set = test.readlines()
    test.close()
    sa = 0
    for t in range(500000):
        u, i, rui = test_set[t].split('  ')
        u, i, rui = int(u), int(i), float(rui)
        pui = Predict(u, i, p, q)
        eui = rui - pui
        sa = sa + eui ** 2
    print('finish')
    print((sa / 500000) ** 0.5)

