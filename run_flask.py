from flask import Flask, render_template, Markup
import io
from IPython.display import HTML
import pandas as pd
pd.options.display.float_format = '{:,.0f}'.format
pd.set_option('display.max_colwidth', -1)

app = Flask(__name__)

with open('processed_data.csv', 'rb') as f:
    df = pd.read_csv(f)
df = df.drop(df.columns[[0, 1]], axis=1)
str_io = io.StringIO()
HTML(df.to_html(buf=str_io, classes='table table-striped table-dark', escape=False, index=False))
html_table = str_io.getvalue()


@app.route('/')
def hello_world(table=Markup(html_table)):
    return render_template('table.html', table=table)


app.run()