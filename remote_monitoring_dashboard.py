# remote_monitoring_dashboard.py
"""
Remote monitoring dashboard script.
"""

import dash
from dash import dcc, html
import plotly.graph_objs as go
from sensor_data_collector import SensorDataCollector

app = dash.Dash(__name__)

# Initialize sensor data collector
collector = SensorDataCollector()

# Define the layout of the dashboard
app.layout = html.Div(children=[
    html.H1(children='Remote Monitoring Dashboard'),

    dcc.Interval(
        id='interval-component',
        interval=5*1000,  # Update every 5 seconds
        n_intervals=0
    ),

    dcc.Graph(
        id='live-update-graph'
    )
])

# Callback to update the graph
@app.callback(
    dash.dependencies.Output('live-update-graph', 'figure'),
    [dash.dependencies.Input('interval-component', 'n_intervals')]
)
def update_graph_live(n):
    data = collector.collect_data()
    temperature_data = [data[sensor_id] for sensor_id in data if 'temperature' in sensor_id]
    vibration_data = [data[sensor_id] for sensor_id in data if 'vibration' in sensor_id]

    figure = {
        'data': [
            go.Scatter(
                x=list(range(len(temperature_data))),
                y=temperature_data,
                mode='lines+markers',
                name='Temperature'
            ),
            go.Scatter(
                x=list(range(len(vibration_data))),
                y=vibration_data,
                mode='lines+markers',
                name='Vibration'
            )
        ],
        'layout': go.Layout(
            title='Live Sensor Data',
            xaxis={'title': 'Time'},
            yaxis={'title': 'Value'},
        )
    }

    return figure

if __name__ == '__main__':
    app.run_server(debug=True)
