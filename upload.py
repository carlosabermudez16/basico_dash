import datetime

import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Upload(
        id='upload-image',
        children=html.Div([ html.A(' ')]),
        style={
            'width': '50px',
            'height': '50px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '100%',
            'textAlign': 'center',
            'margin': '10px',
            'cursor':'pointer',
            #'background':'linear-gradient(-135deg, #2941b6, #f1eff1,#2941b6)',
            },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    html.Div(id='output-image-upload'),
])


def parse_contents(contents):
    return html.Div([
        # HTML images accept base64 encoded strings in the same format
        # that is supplied by the upload
        html.Img(src=contents,
                style={
                    'width': '50px',
                    'height': '50px',
                    'lineHeight': '60px',
                    'borderWidth': '1px',
                    'borderStyle': 'dashed',
                    'borderRadius': '100%',
                    'margin': '10px',
                    'position':'absolute',
                    'top':'0px',
                    'z-index':'-1',
                    'cursor':'pointer',
                    },
            ),
        ],
        )


@app.callback(Output('output-image-upload', 'children'),
              Input('upload-image', 'contents'),)
def update_output(list_of_contents):
    if list_of_contents is not None:
        children = [
            parse_contents(c) for c in list_of_contents]
        return children


if __name__ == '__main__':
    app.run_server(debug=True)