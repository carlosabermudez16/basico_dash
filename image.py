import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import numpy as np
import os
from plotly.subplots import make_subplots
import dash_table
app = dash.Dash(__name__)

np.random.seed(1)

N = 100
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
sz = np.random.rand(N) * 30


fig = go.Figure()
fig.add_trace(go.Scatter(
    x=x,
    y=y,
    mode="markers",
    marker=go.scatter.Marker(
        size=sz,
        color=colors,
        opacity=0.6,
        colorscale="Viridis"
    )
    ))

fig2 = make_subplots(rows=1, cols=2, shared_yaxes=True)

fig2.add_trace(go.Bar(x=[1, 2, 3], y=[4, 5, 6],
                    marker=dict(color=[4, 5, 6], coloraxis="coloraxis")),
              1, 1)

fig2.add_trace(go.Bar(x=[1, 2, 3], y=[2, 3, 5],
                    marker=dict(color=[2, 3, 5], coloraxis="coloraxis")),
              1, 2)

fig2.update_layout(coloraxis=dict(colorscale='Bluered_r'), showlegend=False)

fig3 = go.Figure()

# Create list from 0 to 39 to use as x, y, and color
values = list(range(40))

fig3.add_trace(go.Scatter(
    x=values,
    y=values,
    marker=dict(
        size=16,
        cmax=39,
        cmin=0,
        color=values,
        colorbar=dict(title="Colorbar"),
        colorscale="Viridis"
    ),
    mode="markers"))

fig4 = go.Figure()
fig4.add_trace(go.Scatter(
    y=list(range(-5,15)),
    mode="markers",
    marker={"size": 25, "color": list(range(-3,10)), "cmid": 0}))


x = np.random.uniform(low=3, high=6, size=(500,))
y = np.random.uniform(low=3, high=4.5, size=(500,))
x2 = np.random.uniform(low=3, high=6, size=(500,))
y2 = np.random.uniform(low=4.5, high=6, size=(500,))

# Build figure
fig5 = go.Figure()

# Add first scatter trace with medium sized markers
fig5.add_trace(
    go.Scatter(
        mode='markers',
        x=x,
        y=y,
        opacity=0.5,
        marker=dict(
            color='LightSkyBlue',
            size=20,
            line=dict(
                color='MediumPurple',
                width=2
            )
        ),
        name='Opacity 0.5'
    )
)

# Add second scatter trace with medium sized markers
# and opacity 1.0
fig5.add_trace(
    go.Scatter(
        mode='markers',
        x=x2,
        y=y2,
        marker=dict(
            color='LightSkyBlue',
            size=20,
            line=dict(
                color='MediumPurple',
                width=2
            )
        ),
        name='Opacity 1.0'
    )
)

# Add trace with large markers
fig5.add_trace(
    go.Scatter(
        mode='markers',
        x=[2, 2],
        y=[4.25, 4.75],
        opacity=0.5,
        marker=dict(
            color='LightSkyBlue',
            size=80,
            line=dict(
                color='MediumPurple',
                width=8
            )
        ),
        showlegend=False
    )
)


fig6 = go.Figure()

fig6.add_trace(go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[0, 1, 3, 2, 4, 3, 4, 6, 5]
))

fig6.add_trace(go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[0, 4, 5, 1, 2, 2, 3, 4, 2]
))

fig6.add_annotation(
        x=2,
        y=5,
        xref="x",
        yref="y",
        text="max=5",
        showarrow=True,
        font=dict(
            family="Courier New, monospace",
            size=16,
            color="#ffffff"
            ),
        align="center",
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor="#636363",
        ax=20,
        ay=-30,
        bordercolor="#c7c7c7",
        borderwidth=2,
        borderpad=4,
        bgcolor="#ff7f0e",
        opacity=0.8
        )

fig6.update_layout(showlegend=False)
################################################################
size = [100, 40, 60, 80, 100, 80, 60, 40, 20, 40]

fig7 = go.Figure(data=[
    go.Scatter(
    x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    y=[11, 12, 10, 11, 12, 11, 12, 13, 12, 11],
    mode='markers+lines',
    line = dict(
					width = 3,
					color = "MediumPurple"
				),
    marker=dict(
        size=[i for i in size],
        sizemode='area',
        sizeref=2.*max(size)/(40.**2),
        sizemin=4,
        color=y,
        colorscale="Viridis",
        opacity=1,
        line = dict(
						color = "MediumPurple",
						width = 2
					),
            )
    ),
    
    ])

###############################################################

app.layout = html.Div([
        html.Button('Hola mundo'),
        html.Br(),
        html.Img(src='./assets/file.jpg',id='estilo'),
        #dcc.Graph(figure=fig),
        #dcc.Graph(figure=fig2),
        #dcc.Graph(figure=fig3),
        #dcc.Graph(figure=fig4),
        #dcc.Graph(figure=fig5),
        #dcc.Graph(figure=fig6),
        #dcc.Graph(figure=fig7),
        dash_table.DataTable(
    data=[
        {'shop': 'Bakersfield', 'sales': 4, 'goal': 10},
        {'shop': 'Berkeley', 'sales': 10, 'goal': 1},
        {'shop': 'Carlos Bermudez', 'sales': 5, 'goal': 4}
    ],
    columns=[
        {'id': 'shop', 'name': 'Store Location'},
        {'id': 'sales', 'name': 'Sales Revenue'},
        {'id': 'goal', 'name': 'Revenue Goal'},
    ],
    style_cell = {
                                        #'whiteSpace': 'normal',
                                        #'height': 'auto',
                                        'textAlign': 'center',
                                         "backgroundColor": "white",
                                         
                                         "border-bottom": "0.01rem solid #19aae1",
                                    },
    tooltip_data=[
        {
            'shop': {
                'value': 'Location at Bakersfield\n\n![Bakersfield]({})'.format(
                    app.get_relative_path('/assets/images/table/file-lanczos3.png'),
                ),
                'type': 'markdown',
                
            }
        },
        {
            'shop': {
                'value': 'Location at Bakersfield\n\n![Bakersfield]({})'.format(
                    app.get_relative_path('/assets/images/table/file-lanczos3.png')
                ),
                'type': 'markdown',
                
            }
        },
        {
            'shop': {
                'value': 'Estudiante: \n\n![Carlos Bermudez](/assets/images/table/file-lanczos3.png)',
                'type': 'markdown'
            }
        },

    ],
    css=[{
        'selector': '.dash-table-tooltip',
        'rule': """background: rgb(150,150,1540); 
                    font-family: monospace;
                    display: block;
                    vertical-align: middle;
                    white-space: inherit;
                    overflow: inherit;
                    text-overflow: inherit;
                    z-index: 1;
                    width:150px;
                    color: red;""",
        
            }],
    # Style headers with a dotted underline to indicate a tooltip
    style_data_conditional=[{
        'if': {'column_id': 'shop'},
        'textDecoration': 'underline',
        'textDecorationStyle': 'dotted',
    }],

    tooltip_delay=0,
    tooltip_duration=None
)
    ]
)


if __name__=='__main__':
    app.run_server(debug=True)