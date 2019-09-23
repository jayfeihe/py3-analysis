#!/usr/bin/env python3
# coding:utf-8

from sklearn.preprocessing import MinMaxScaler,StandardScaler

'''
数据特征预处理
1、归一化
2、标准化
'''


'''
归一化处理
公式:X'=(x-min)/(max-min)  X''=X'*(mx-mi)+mi
特定：通过对原始数据进行变换把数据映射到(默认为[0,1])之间
总结：注意在特定场景下最大值最小值是变化的，另外，最大值与最小值非常容易受异常点影响，所有这种方法鲁棒性（稳定性）较差，只适合传统精确小数据场景。
目的：使得某一个特征对最终结果不会造成更大的影响。
'''
def mm():
    mm=MinMaxScaler(feature_range=(2,3))
    data=mm.fit_transform([[90,2,10,40],[60,4,15,45],[75,3,13,46]])
    print(data)
    print(type(data))

'''
标准化处理
公式：x' =(x - 𝜇)/𝜎
𝜇为平均值，𝜎=标准差（var=(x1-𝜇）²+(x2-𝜇）²+.../样本数的方差
总结：在已有样本足够多的情况下比较稳定，适合现代嘈杂大数据场景
'''
def stand():
    stand=StandardScaler()
    data = stand.fit_transform([[90, 2, 10, 40], [60, 4, 15, 45], [75, 3, 13, 46]])
    print(data)
    print(type(data))
if __name__ == '__main__':
    mm()
    stand()