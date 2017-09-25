import timeit
import memory_profiler
from lxml import etree
import plotly.plotly as py
import plotly.graph_objs as go

@memory_profiler.profile
def process_xml(fp):
    tree = etree.parse(fp)
    tree.write('C:\\Users\\Joe\\Desktop\\SPE\\Lab3\\output.xml', pretty_print=True)
    return tree


@memory_profiler.profile
def query_xml(tr, np):
    tree = etree.iterparse(tr)
    result = []
    for action, elem in tree:
        if elem.tag == np:
            result.append(elem)
        elem.clear()
    print(len(result))
    return result

if __name__ == "__main__":
    file_path = "C:\\Users\\Joe\\Desktop\\SPE\\Lab3\\52mb.xml"


    t1 = []
    t2 = []
    t3 = []
    t4 = []

    #p4 = timeit.Timer(lambda: query_xml(tree4, "{http://www.mediawiki.org/xml/export-0.10/}title"))
    runs = 50

    #tree1 = process_xml("C:\\Users\\Joe\\Desktop\\SPE\\Lab3\\demodata.xml")
    p1 = timeit.Timer(lambda: query_xml("C:\\Users\\Joe\\Desktop\\SPE\\Lab3\\demodata.xml", "percent_male"))
    for i in range(runs):
        t1.append(p1.timeit(1))

    #tree2 = process_xml("C:\\Users\\Joe\\Desktop\\SPE\\Lab3\\52mb.xml")
    p2 = timeit.Timer(lambda: query_xml("C:\\Users\\Joe\\Desktop\\SPE\\Lab3\\52mb.xml", "link"))
    for i in range(runs):
        t2.append(p2.timeit(1))

    #tree3 = process_xml("C:\\Users\\Joe\\Desktop\\SPE\\Lab3\\127mb.xml")
    p3 = timeit.Timer(lambda: query_xml("C:\\Users\\Joe\\Desktop\\SPE\\Lab3\\127mb.xml", "year"))
    for i in range(runs):
        t3.append(p3.timeit(1))


    trace0 = go.Scatter(
        x=[i for i in range(runs)],
        y=t1,
        mode='lines',
        name='610KB XML File',
        connectgaps=True
    )
    trace1 = go.Scatter(
        x=[i for i in range(runs)],
        y=t2,
        mode='lines',
        name='52MB XML File',
        connectgaps=True
    )

    trace2 = go.Scatter(
        x=[i for i in range(runs)],
        y=t3,
        mode='lines',
        name='127MB XML File',
        connectgaps=True
    )

    trace3 = go.Scatter(
        x=[i for i in range(runs)],
        y=t4,
        mode='lines',
        name='635MB XML File',
        connectgaps=True
    )

    layout = dict(title="XML Process Time For 635MB File",
                  xaxis=dict(title="Run number"),
                  yaxis=dict(title="Runtime (seconds)")
                  )

    #data = [trace3]
    #fig = dict(data=data, layout=layout)
    #py.iplot(fig, filename="LargeProcess")
