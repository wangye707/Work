import sys
sys.path.append("../")
import jieba
import os
import jieba.posseg as pseg
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
#加载停用词表
stop = [line.strip() for line in open('stopword.txt').readlines() ]
path = "D:/TXT/test"  # 文件夹目录
files = os.listdir(path)  # 得到文件夹下的所有文件及文件夹名称（这里注意文件和文件夹都有！）
s = []
for file in files:
    if not os.path.isdir(file):  # 判断是文件夹，不是文件夹即为文件
        f = open(path + "/" + file)  # 找到该文件的路径打开文件，或者用os.path.join(path,file)
        iter_f = iter(f);  # 创建迭代器
        str = ""
        for line in iter_f:  # 遍历文件，一行行遍历，读取文本
            str = str + line
        s.append(str)  # 每个文件的文本存到list中
        print(s)
#分词
segs = jieba.cut(s, cut_all=False)
segs = pseg.cut(s)
l = ''
for word ,flag in segs:
    #去停用词
    if word not in stop:
       #去数词和去字符串
       if flag !='m' and flag !='x':
            #输出分词
            l +=' '+ word

print (l)
words = CountVectorizer().fit_transform(l)#TF词频特征向量
qiuqiu = TfidfTransformer().fit_transform(words)#IDF逆向文档频率特征向量
print(words)
print (qiuqiu)