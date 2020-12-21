from random import randrange
from flask import Flask, render_template
from jinja2 import Markup, Environment, FileSystemLoader
import pandas as pd
from draw_graph import *
import json


app = Flask(__name__, static_folder="templates")

with open('Kline_graphs.json','r') as f:
    kline_graphs = json.load(f)

with open('volume_Line_Graph.json','r') as f:
    volume_Line_graphs = json.load(f)
with open('boxplot.json','r') as f:
    boxplot_graphs = json.load(f)

with open('dataObj.json','r') as f:
    dataObj = json.load(f)

with open('multi_y.json','r') as f:
    multi_y = json.load(f)


@app.route("/")
def index():
    return render_template("index.html",
                           Kline_graphs=kline_graphs,
                           volume_Line_graphs = volume_Line_graphs,
                           boxplot_graphs = boxplot_graphs,
                           dataObj = dataObj,
                           multi_y=multi_y
                           )



if __name__ == "__main__":
    app.run()