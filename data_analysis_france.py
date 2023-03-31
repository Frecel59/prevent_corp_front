import pandas as pd
import plotly.express as px

data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

def create_plot():
    fig = px.bar(df, x=df.index, y=['A', 'B'], title='Example Plot')
    return fig
