import timeit
import memory_profiler
import json
import objectpath
import plotly.plotly as py
import plotly.graph_objs as go


@memory_profiler.profile
def process_json(fp):
    with open(fp, encoding='utf-8') as df:
        str = df.read()
        data = json.loads(str)
        json.dump(data, open("C:\\Users\\Joe\\Desktop\\SPE\\Lab3\\jsonoutput.json", "w"))
    return data


@memory_profiler.profile
def query_json(fp, n):
    res = []
    with open(fp, encoding='utf-8') as df:
        str = df.read()
        data = json.loads(str)
        tree_obj = objectpath.Tree(data)

        return tuple(tree_obj.execute('$..'+n))


if __name__ == "__main__":

    t1 = []
    t2 = []
    t3 = []

    p1 = timeit.Timer(lambda: print(process_json("C:\\Users\\Joe\\Desktop\\SPE\\Lab3\\131kb.json")))
    p2 = timeit.Timer(lambda: print(process_json("C:\\Users\\Joe\\Desktop\\SPE\\Lab3\\8mb.json")))
    p3 = timeit.Timer(lambda: print(process_json("C:\\Users\\Joe\\Desktop\\SPE\\Lab3\\66mb.json")))
    runs = 10

    for i in range(runs):
        t1.append(p1.timeit(1))
    for i in range(runs):
        t2.append(p2.timeit(1))
    for i in range(runs):
        t3.append(p3.timeit(1))

    trace0 = go.Scatter(
        x=[i for i in range(runs)],
        y=t1,
        mode='lines',
        name='131KB JSON File',
        connectgaps=True
    )
    trace1 = go.Scatter(
        x=[i for i in range(runs)],
        y=t2,
        mode='lines',
        name='8MB JSON File',
        connectgaps=True
    )

    trace2 = go.Scatter(
        x=[i for i in range(runs)],
        y=t3,
        mode='lines',
        name='66MB JSON File',
        connectgaps=True
    )

    layout = dict(title="JSON Processing Time By File",
                  xaxis=dict(title="Run number"),
                  yaxis=dict(title="Runtime (seconds)")
                  )
