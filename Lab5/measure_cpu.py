import psutil
import plotly.plotly as py
import plotly.graph_objs as go
import time

if __name__ == "__main__":
    arr = []
    times = [0]
    t = 0
    while t < 15:
        t += 1
        x = psutil.cpu_percent(interval=1, percpu=True)
        arr.append(x)
        print(x)
        times.append(t)
        time.sleep(1)


    data = []

    for i in range(len(arr[0])):
        t = go.Scatter(
            x=times,
            y=[z[i] for z in arr],
            mode='lines',
            name='Core ' + str(i + 1),
            connectgaps=True
        )
        data.append(t)


    layout = dict(title="CPU Usage Per Core",
                  xaxis=dict(title="Elapsed Time (seconds)"),
                  yaxis=dict(title="CPU Usage")
                  )

    fig = go.Layout(
    )

    fig = go.Figure(data=data, layout=layout)
    py.iplot(fig, filename='cpu_usage')