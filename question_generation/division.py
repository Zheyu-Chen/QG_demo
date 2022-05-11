# 【导⼊相应的库（对数据库进⾏切分需要⽤到的库是sklearn.model_selection 中的 train_test_split）】
import numpy as np
from sklearn.model_selection import train_test_split

# 【⾸先，读取.TSV⽂件成矩阵的形式。】
# 若标签为浮点，直接使⽤下⾯⼀⾏即可
filepath = '.\\output\\all_output.tsv'  # 数据⽂件路径
data = np.loadtxt(filepath, dtype=str, delimiter="\t", skiprows=0)
print(data)

##--------------------【若标签为Striing,先将标签转化为浮点型】------------------------------
def iris_type(s):
    class_label = {b'Iris-setosa': 0, b'Iris-versicolor': 1, b'Iris-virginica': 2}
    return class_label[s]


# 使⽤numpy中的loadtxt读⼊数据⽂件（csv格式的iris数据，也可直接换成txt格式）
# filepath = '.\\output\\all_output.tsv'  # 数据⽂件路径
# data = np.loadtxt(filepath, dtype=str, delimiter='\t', converters={4: iris_type})
##-------------------------------------------------------------------------------------
# 【将矩阵最后⼀列之前的数值给X（输⼊数据），将矩阵最后⼀列的数值给y（标签）】
X, y = data[:, :-1], data[:, -1]
# 【利⽤train_test_split⽅法，将X,y随机划分为训练集（X_train），训练集标签（y_train），测试集（X_test），测试集标签（y_test），按训练集：测试集=7:3的概率划分，到此步骤，可以直接对数据进⾏处理】
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
# 【将训练集与数据集的数据分别保存为TSV⽂件】
# np.column_stack将两个矩阵进⾏组合连接，numpy.savetxt 将txt⽂件保存为csv格式的⽂件
train = np.column_stack((X_train, y_train))
print(train)
np.savetxt('.\\output\\train.tsv', train, fmt='%s', delimiter='\t')
# np.savetsv('.\\output\\train_set.tsv', train, delimiter='\t')
test = np.column_stack((X_test, y_test))
np.savetxt('.\\output\\test.tsv', test, fmt='%s', delimiter='\t')
# np.savetsv('.\\output\\test_set.tsv', test, delimiter='\t')
