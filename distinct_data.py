import pandas as pd
import os
import numpy as np


class data_frame():
    def __init__(self,path):
        self.path = path
        self.data = pd.read_json(path)
        # 区级排列顺序
        self.districts = ['浦东新区', '黄浦区', '静安区', '徐汇区', '长宁区', '普陀区', '虹口区', '杨浦区', '宝山区', '闵行区', '嘉定区', '金山区', '松江区', '青浦区', '奉贤区', '崇明区']
        # 共计新增，无症状，确诊
        self.total = self.data.iloc[0]['total']
        self.asymptomatic = self.data.iloc[0]['asymptomatic']
        self.confirmed = self.data.iloc[0]['confirmed']

    # 将数据提取，以确诊、无症状，共计顺序返回三个列表，分别包含
    def extracter(self):
        number_stat = [[0 for _ in range(16)] for _ in range(3)]
        for i in range(len(self.data)):
            l = self.data.iloc[i]
            distri = l['districts']['district_name']
            distri_number= [l['districts']['confirmed'], \
                                               l['districts']['asymptomatic'], l['districts']['total']]
            index = self.districts.index(distri)
            for j in range(3):
                number_stat[j][index] = distri_number[j]
        return number_stat




path_head = 'data/'
file_names = os.listdir('data/')
file_names = [path_head+item for item in file_names]
print(file_names)
distinct_data=[[0 for _ in range(len(file_names))] for _ in range(16)]
j=0
for item in file_names:
    data = data_frame(item)
    number = data.extracter()
    for i in range(16):
        distinct_data[i][j]=number[2][i]
    j=j+1
print(distinct_data[0:16][-30:])
distinct_data=pd.DataFrame(distinct_data,index=['浦东新区', '黄浦区', '静安区', '徐汇区', '长宁区', '普陀区', '虹口区', '杨浦区', '宝山区', '闵行区', '嘉定区', '金山区', '松江区', '青浦区', '奉贤区', '崇明区']).T
distinct_data.to_excel("distinct_data.xlsx")
