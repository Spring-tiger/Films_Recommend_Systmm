"""
按1：9的比例将原训练集划分成新的寻训练集和测试集
"""
import random
train = open('D:\data\data-new/mytrain.txt', 'r+')
train_set = train.readlines()
train.close()
print(type(train_set))
# 生成不重复的随机数，作为测试集数据在原始数据中的“下标”
Test_index = random.sample(range(0, len(train_set)), 500000)
s = ''
for j in range(500000):
    uid, mid, score, nu = train_set[Test_index[j]].split('  ')
    s = s + uid + '  ' + mid + '  ' + score + '\n'
    if j % 10000 == 0:
        print(j)
        my = open('D:\data\data-new/mytest0.txt', 'a+')
        my.writelines(s)
        my.close()
        s = ''

my = open('D:\data\data-new/mytest0.txt', 'a+')
my.writelines(s)
my.close()
Test_index.sort(reverse=True)  # 下标按降序排列
# 按照下标从大到小的顺序，在训练集中删除相应的行，若不排序会导致下标混乱
for i in range(500000):
    del train_set[Test_index[i]]
    if i % 10000 == 0:
        print(i)
my0 = open('D:\data\data-new/mytrain0.txt', 'a+')
my0.writelines(train_set)
my0.close()

print('finish')
