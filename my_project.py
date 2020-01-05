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
from han import dfa,dfb,dfc

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


# 地图 = list(zip(list(df1.CountryName),list(df1["2010"])))


# def line_base() -> Line:
#     c = (
#         Line()
#         .add_xaxis(list(dd.columns)[2:])
#         .add_yaxis("产妇死亡数", list(dd.loc['World'])[2:])
#         .set_global_opts(title_opts=opts.TitleOpts(title="近十多年来世界每10万产妇死亡数"))
#     )
#     return c
#
# line_base().render('1.html')


app = Flask(__name__)

# regions_available = list(df2.CountryName.dropna.unique())
# regions_available2 = list(df2.CountryName.dropna.unique())

content = {"表格一":df1,"表格二":df2,"表格三":df3}

regions_available_loaded = ['表格一','表格二','表格三']       #第一个下拉框的内容选择

# 基本cufflinks 及ploty設置, 查文檔看書貼上而已
cf.set_config_file(offline=True, theme="ggplot")
py.offline.init_notebook_mode()
# 准备工作
# pandas 大法读内容, 用dropna()丢缺失值, 用unique()取唯一值, 不重覆
df1 = pd.read_csv("E:/my_project/data/pregnant.csv",encoding='utf-8')
# regions_available_loaded1 = ['Aruba','Afghanistan','Angola','Albania']   #调用csv文件的Country Name 表头，来实现数据表格交互
regions_available_loaded1 = list(df1['Country Name'])     #第二个下拉框的内容选择


@app.route('/',methods=['GET'])
def hu_run() -> 'html':


    # the_region = request.form["the_region_selected"]
    # dfs = df1.query("CountryName=='{}'".format(the_region))
    # fig = dfs.iplot(kind="bar",x="CountryName",asFigure=True)
    # py.offline.plot(fig,filename="example1.html",auto_open=False)
    #
    # with open("example1.html",encoding="utf8",mode="r") as f:
    #     plot_all = "".join(f.readline())


    data_str = df7.to_html()     #首页的表格


    regions_available = regions_available_loaded                  #第一个下拉框的内容
    regions_available1 = regions_available_loaded1
    return render_template('results.html',
                           the_res = data_str,
                           # the_result = plot_all,
                           the_select_region=regions_available,
                           the_select_region1=regions_available1
                           )

@app.route('/select',methods=['POST'])
def run_select() -> 'html':

    the_region = request.form["the_region_selected"]        #获取用户的选择

    print(the_region)


    data_str = content[the_region].to_html()  # 数据列表的实时交互

    # fig = df2.iplot(kind="bar",x="Country Name",asFigure=True)
    # py.offline.plot(fig,filename="nursing.html",auto_open=False)

    # 实现表格切换效果
    if the_region == "表格一":        #表格一的选择
        dfa()


    elif the_region == "表格二":        #表格二的选择
        dfb()

    elif the_region == "表格三":        #表格三的选择
        dfc()


    regions_available = regions_available_loaded  # 下拉选单有内容

    return render_template('results.html',
                           # the_plot_all = plot_all,
                           the_res = data_str,
                           the_select_region=regions_available
                           )


@app.route('/select2',methods=['POST'])
def run_select1() -> 'html':


    the_region1 = request.form["the_region_selected1"]      #获取用户的选择
    print(the_region1)

    df1 = pd.read_csv("E:/my_project/data/pregnant.csv", encoding='utf-8')   #提取csv数据

    dfs = df1.query("Country Name=='{}'".format(the_region1))         #过滤用户的选择“Country Name”

    regions_available_loaded1 = list(df1['Country Name'])   #下拉框选择的内容

    data_str1 = dfs.to_html()   # 数据产出dfs, 完成互动过滤呢

    fig = df2.iplot(kind="bar",x="Country Name",asFigure=True)
    py.offline.plot(fig,filename="nursing.html",auto_open=False)

    regions_available1 = regions_available_loaded1 #python与数据交互下拉框

    return render_template('index.html',
                           # the_plot_all = plot_all,
                           the_res1 = data_str1,
                           the_select_region1=regions_available1
                           )





if __name__ == '__main__':
    app.run(debug=True)
