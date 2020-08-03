# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 15:40:47 2020

@author: 13988
"""

# 引入数据集，sklearn包含众多数据集
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

data = load_iris()

print(u'%s\tlabel' % (u'\t'.join(data.feature_names)))

for sample_data, sample_label in zip(data.data, data.target):
    sample_data_str = u'\t'.join([str(w) for w in sample_data])
    sample_label_str = data.target_names[sample_label]
    print("%s\t%s"% (sample_data_str, sample_label_str))
colors = ['red', 'dodgerblue','lime']
attr_index1 = 0
atrr_index2 = 2

print(u'%s\tlabel' % (u'\t'.join((data.feature_names[attr_index1], data.feature_names[atrr_index2]))))

for label_ser, label_name in enumerate(data.target_names):
    category_data = data.data[data.target==label_ser][:][:,(attr_index1, atrr_index2)]
    for sample_data in category_data:
        sample_data_str = u'\t'.join([str(w) for w in sample_data])
        print("%s\t%s" % (sample_data_str, label_name))
    plt.scatter(category_data[:,0], category_data[:,1], c=colors[label_ser], marker='x')

plt.xlabel(data.feature_names[attr_index1])
plt.ylabel(data.feature_names[atrr_index2])
plt.title("iris data")
plt.show()








