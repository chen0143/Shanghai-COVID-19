# 改进后的FUDAN-CCDC模型评价上海各区防疫

## data
data中为上海市每日疫情数据，数据精确到区级。数据采集方式为使用https://github.com/lewangdev/shanghai-lockdown-covid-19 中的爬虫。

## analyze.py
读取json数据，将其转化为csv格式并保存。

## model.py
对上海市数据进行建模。

## distinct_model.py
对各区数据进行建模并分析。

## distinct_data.py
分析各区数据。