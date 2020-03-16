"""
统一训练集的数据格式，每行的格式:用户-电影-评分
"""
train = open('D:\data\data-new/train.txt', 'r+')
train_set = train.readlines()
train.close()
print(len(train_set))
uid = 0
num = 0
s = ''
for i in range(len(train_set)):
    for j in range(len(train_set[i])):
        if train_set[i][j] == '|':
            uid, num = train_set[i].split('|')
            num = int(num)
            # print(i, uid, num)
            for t in range(i + 1, i + 1 + num):
                s = s + uid + '  ' + train_set[t]
    if i % 50000 == 0:  # 每50000行写一次文件，既可以避免频繁IO,也能减少s的长度，可节省时间
        my = open('D:\data\data-new/mytrain.txt', 'a+')
        my.writelines(s)
        my.close()
        s = ''

my = open('D:\data\data-new/mytrain.txt', 'a+')
my.writelines(s)
my.close()
print('finish')
