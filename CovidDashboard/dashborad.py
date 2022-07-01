import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import json
import glob
import os

all_files = glob.glob("data/*.csv")

df = pd.concat((pd.read_csv(f, sep=";")) for f in all_files)