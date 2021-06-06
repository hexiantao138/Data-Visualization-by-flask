"""  MATPLOTLIB在线模板"""

# 导入Flask
from flask import Flask, render_template, send_file, make_response, url_for, Response

# Pandas和Matplotlib
import pandas as pd
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
# 其他导入
import io

# 数据导入
data = pd.read_csv('desktop/pandas/data/titanic_train.csv')

app = Flask(__name__)
#Pandas页
@app.route('/')
@app.route('/pandas', methods=("POST", "GET"))
def GK():
    return render_template('pandas.html',
                           PageTitle = "Pandas",
                           table=[data.loc[0:20,:].to_html(classes='data', index = False)], 
                           titles= data.columns.values)   #仅展示20行

#Matplotlib页
@app.route('/matplot', methods=("POST", "GET"))
def mpl():
    return render_template('matplot.html',
                           PageTitle = "Matplotlib")

@app.route('/plot.png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure():
    #fig.patch.set_facecolor('#E8E5DA')
    fig, axes = plt.subplots(2,1, figsize = (10,10))
    ax = axes.ravel()
    for i, ax in zip(range(1, 5, 3), axes.ravel()):
        name_list = data[data.columns[i]].unique()
        X = len(data[data[data.columns[i]] == data[data.columns[i]].unique()[0]])
        y = len(data[data[data.columns[i]] == data[data.columns[i]].unique()[1]])
        num_list = [X,y]
        ax.bar(range(len(num_list)), num_list, color = 'rgb', tick_label = name_list)
        ax.set_title("{}".format(data.columns[i]))
    
    return fig


if __name__ == '__main__':
    app.run()