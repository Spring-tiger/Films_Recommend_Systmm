"""
将结果的格式变为要求的格式
"""

result = open('D:\data\data-new/myresult.txt', 'r+')
result_set = result.readlines()
result.close()

s = ''
# uid, mid, score, nu = result_set[0].split('  ')
old = -1
for i in range(len(result_set)):
    uid, mid, score = result_set[i].split('  ')
    new = int(uid)
    if old != new:
        old = new
        s = s + uid + '|' + '6' + '\n'
    s = s + mid + '  ' + score
    if i % 10000 == 0:  # 每50000行写一次文件，既可以避免频繁IO,也能减少s的长度，可节省时间
        print(i)
        my = open('D:\data\data-new/result.txt', 'a+')
        my.writelines(s)
        my.close()
        s = ''

my = open('D:\data\data-new/result.txt', 'a+')
my.writelines(s)
my.close()
print('finish')
