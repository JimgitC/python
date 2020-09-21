from flask import Flask, render_template, request
import pandas as pd
import cufflinks as cf
#import plotly as py


app = Flask(__name__)


df1 = pd.read_csv('C:/AppData/qimo/data/class_adolescent.csv',encoding='utf-8')
df2 = pd.read_csv('C:/AppData/qimo/data/regoin_skilled.csv', encoding='utf-8')
# dd=df1.set_index("Country Name")
df3 = pd.read_csv('C:/AppData/qimo/data/region_maternity.csv',encoding='utf-8')
df4 = pd.read_csv('C:/AppData/qimo/data/class_skilled.csv',encoding='utf-8')
df5 = pd.read_csv('C:/AppData/qimo/data/class_maternity.csv',encoding='utf-8')
df6 = pd.read_csv('C:/AppData/qimo/data/class_adolescent.csv',encoding='utf-8')
df7 = pd.read_csv('C:/AppData/qimo/data/regoin_skilled.csv',encoding='utf-8')
df8 = pd.read_csv('C:/AppData/qimo/data/region_maternity.csv',encoding='utf-8')
df9 = pd.read_csv('C:/AppData/qimo/data/region_adolescent.csv',encoding='utf-8')

content = {"表格一":df1,"表格二":df2,"表格三":df3}

regions_available_loaded = ['表格一','表格二','表格三']       #第一个下拉框的内容选择

cf.set_config_file(offline=True, theme="ggplot")
#py.offline.init_notebook_mode()


@app.route('/',methods=['GET'])

def hu_run():



    data_str = df7.to_html()     #首页的表格


    regions_available = regions_available_loaded                  #第一个下拉框的内容
    # regions_available1 = regions_available_loaded1
    return render_template('results.html',
                           the_res = data_str,
                           # the_result = plot_all,
                           the_select_region=regions_available
                           # the_select_region1=regions_available1
                           )

@app.route('/select',methods=['POST'])
def run_select():

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

def dfa():
    content = {"表格一": df1, "表格二": df2, "表格三": df3}   #存放选择框的内容


    the_region = request.form["the_region_selected"]
    print(the_region)


    data_str = content[the_region].to_html()  # 数据列表的实时交互


    return data_str,

def dfb():
    content = {"表格一": df1, "表格二": df2, "表格三": df3}      #存放选择框的内容
    the_region = request.form["the_region_selected"]

    data_str = content[the_region].to_html()  # 数据列表的实时交互


    return data_str


def dfc():
    content = {"表格一": df1, "表格二": df2, "表格三": df3}     #存放选择框的内容
    the_region = request.form["the_region_selected"]

    data_str = content[the_region].to_html()  # 数据列表的实时交互
    return data_str


@app.route('/interface',methods=['GET'])
def interface():

    return render_template('interface.html',
                            )



if __name__ == '__main__':
    app.run(debug=True)
