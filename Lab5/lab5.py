import multiprocessing as mp
import timeit
import plotly.plotly as py
import plotly.graph_objs as go
import memory_profiler
import random


# Sequential IS
def insertion_sort(arr):
    for i in range(1, len(arr)):
        k = arr[i]
        j = i - 1
        while j >= 0 and k < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = k


#BFS
@memory_profiler.profile
def rand_char_bfs(g, start):
    visited = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            adj = g[node]

            for n in adj:
                queue.append(n)

    return visited


def bfs_n(g, node, n):
    for i in range(n):
        rand_char_bfs(g, node)



@memory_profiler.profile
def parallel_bfs(g, node, runs):
    processes = [mp.Process(target=bfs_n, args=(g, node, runs//10)) for i in range(runs//10)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()


@memory_profiler.profile
def parallel_is(arr, runs):
    processes = [mp.Process(target=is_n, args=(arr, runs//10)) for i in range(runs//10)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()


def is_n(arr, n):
    for i in range(n):
        x = list(arr)
        insertion_sort(x)

if __name__ == '__main__':
    s = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    arr = [random.randint(0, 100000) for i in range(1000)]
    g = {}
    for c in s:
        rand = random.sample(s, random.randint(5, 16))
        g[c] = rand

    t1 = []
    t2 = []

    timer = timeit.Timer(lambda: rand_char_bfs(g, "A"))
    timer3 = timeit.Timer(lambda: insertion_sort(list(arr)))
    t1.append(timer.timeit(100))
    t1.append(timer3.timeit(100))

    timer2 = timeit.Timer(lambda: parallel_bfs(g, "A", 100))
    timer4 = timeit.Timer(lambda: parallel_is(arr, 100))
    t2.append(timer2.timeit(1))
    t2.append(timer4.timeit(1))

    print(t1)
    print(t2)

    trace0 = go.Bar(
        x=['Breadth First Search (N=100)', 'Insertion Sort (N = 100)'],
        y=[100/i for i in t1],
        name='Sequential Implementation Throughput'
    )

    trace1 = go.Bar(
        x=['Breadth First Search (N = 100)', 'Insertion Sort (N = 100)'],
        y=[100/i for i in t2],
        name='Parallel Implementation Throughput'
    )

    data = [trace0, trace1]

    layout = dict(title="Parallel and Sequential Throughputs",
                  xaxis=dict(title="Implementation Type"),
                  yaxis=dict(title="Throughput (Jobs/Second)")
                  )

    fig = go.Layout(
        barmode='group'
    )

    fig = go.Figure(data=data, layout=layout)
    py.iplot(fig, filename='throughputs')