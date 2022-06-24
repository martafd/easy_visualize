#!/usr/bin/env python
# coding: utf-8

from sklearn.preprocessing import MaxAbsScaler, StandardScaler
from pandas.core.common import SettingWithCopyWarning
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import warnings

warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)


df = pd.read_excel('example.xlsx')
df = np.round(df,0)
df.columns = ['cluster'] + ['cluster_#' + str(col) for col in df.columns[1:]]
df = df.set_index('cluster').transpose().fillna(0)

cols_to_plot = ['feature2',
                'feature3',
                'feature4',
                'feature5',
                'feature6',
                'feature8',
                'feature9']


data = df[cols_to_plot]
data.loc[:] = MaxAbsScaler().fit_transform(data)


def plot_radar(data, cols_to_plot):    
    fig = go.Figure()

    for cluster_name, row in data.iterrows():
        fig.add_trace(go.Scatterpolar(
              r=row.values,
              theta=cols_to_plot,
              fill='toself',
              name=cluster_name
        ))

    fig.update_layout(
      polar=dict(
        radialaxis=dict(
          visible=False,

        )),
      showlegend=True)

    fig.show()



plot_radar(data, cols_to_plot)

