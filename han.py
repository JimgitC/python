#encoding: utf-8
from flask import Flask, render_template, request
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Funnel, Page, Pie      #引入世界地图函数
from pyecharts.charts import Bar,Tab,Line,Map,Timeline,Grid,Scatter    #引入图表制作所需要的一些函数
from pyecharts.globals import ChartType, SymbolType    #引入表格样式
import cufflinks as cf
import plotly as py
import numpy as np      #引入numpy
import plotly.graph_objs as go


df1 = pd.read_csv("E:/my_project/data/pregnant.csv",encoding='utf-8')
df2 = pd.read_csv("E:/my_project/data/nursing.csv", encoding='utf-8')
# dd=df1.set_index("Country Name")
df3 = pd.read_csv("E:/my_project/data/teen birth rate.csv",encoding='utf-8')
df4 = pd.read_csv("E:/my_project/data/class_skilled.csv",encoding='utf-8')
df5 = pd.read_csv("E:/my_project/data/class_maternity.csv",encoding='utf-8')
df6 = pd.read_csv("E:/my_project/data/class_adolescent.csv",encoding='utf-8')
df7 = pd.read_csv("E:/my_project/data/regoin_skilled.csv",encoding='utf-8')
df8 = pd.read_csv("E:/my_project/data/region_maternity.csv",encoding='utf-8')
df9 = pd.read_csv("E:/my_project/data/region_adolescent.csv",encoding='utf-8')


cf.set_config_file(offline=True, theme="ggplot")
py.offline.init_notebook_mode()


def dfa() -> 'html':
    content = {"表格一": df1, "表格二": df2, "表格三": df3}   #存放选择框的内容


    the_region = request.form["the_region_selected"]
    print(the_region)


    data_str = content[the_region].to_html()  # 数据列表的实时交互


    return data_str,

def dfb() -> 'html':
    content = {"表格一": df1, "表格二": df2, "表格三": df3}      #存放选择框的内容
    the_region = request.form["the_region_selected"]

    data_str = content[the_region].to_html()  # 数据列表的实时交互


    return data_str


def dfc() -> 'html':
    content = {"表格一": df1, "表格二": df2, "表格三": df3}     #存放选择框的内容
    the_region = request.form["the_region_selected"]

    data_str = content[the_region].to_html()  # 数据列表的实时交互
    return data_str

