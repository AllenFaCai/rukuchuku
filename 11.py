import pickle

i = 123000
a = 100.23
s = '鸡排咖喱蛋包饭'
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
tu = (5, 10, 4)
coll = {3, 4, 5}
dic = {'a': 'apple', 'b': 'bear', 'c': 'cat'}
data = [i, a, s, lst, tu, coll, dic]

with open('sample_pickle111.dat', 'wb') as f:
    try:
        pickle.dump(len(data), f)
        for item in data:
            pickle.dump(item, f)
    except:
        print('写文件异常!')