"""
统一测试集的数据格式，每行的格式:用户-电影
"""
train = open('D:\data\data-new/test.txt', 'r+')
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
            print(i, uid, num)
            for t in range(i + 1, i + 1 + num):
                s = s + uid + '  ' + train_set[t]
    if i % 50000 == 0:
        my = open('D:\data\data-new/mytest.txt', 'a+')
        my.writelines(s)
        my.close()
        s = ''

print('finish')
my = open('D:\data\data-new/mytest.txt', 'a+')
my.writelines(s)
my.close()
