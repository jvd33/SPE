import plotly
import numpy
import statistics
import inspect
import plotly.plotly as py
import plotly.graph_objs as go


def retrieve_name(var):
    """
    Gets the name of var. Does it from the out most frame inner-wards.
    :param var: variable to get name from.
    :return: string
    """
    for fi in reversed(inspect.stack()):
        names = [var_name for var_name, var_val in fi.frame.f_locals.items() if var_val is var]
        if len(names) > 0:
            return names[0]

if __name__=="__main__":
    github = {
        "ttfb": [],
        "compile_time": [],
        "execution_time": [],
        "render_time": [],
        "total_time": [],
        "download_size": [],
        "num_requests": [],
        "kb_per_ms_http": []
    }

    nyt = {
        "ttfb": [],
        "compile_time": [],
        "execution_time": [],
        "render_time": [],
        "total_time": [],
        "download_size": [],
        "num_requests": [],
        "kb_per_ms_http": []
    }

    site3 = {
        "ttfb" : [],
        "compile_time": [],
        "execution_time": [],
        "render_time": [],
        "total_time": [],
        "download_size": [],
        "num_requests": [],
        "kb_per_ms_http": []
    }


    nyt['ttfb'] = [
        29.15,
        25.79,
        27.63,
        65.43,
        26.45,
        25.25,
    ]

    nyt['compile_time'] = [
        105.9/585,
        17.7/245,
        43.4/328,
        55.2/369,
        18.8/280,
        22.1/299,
    ]

    nyt['execution_time'] = [
        395.8/585,
        111.8/245,
        231.7/328,
        536.7/369,
        323.4/280,
        405.22/299,
    ]

    nyt['render_time'] = [
        671.3,
        85.8,
        328.7,
        201.1,
        155.6,
        94.8,
    ]

    nyt['total_time'] = [
        81.9+1209.8+671.3+52+267.4,
        44+467.4+85.8+17.3+197.3,
        122.4+840.9+328.7+70.3+236.5,
        17.0+658.7+201.1+42.2+211,
        20.6+460.5+155.6+63.1+201.3,
        26.6+705.4+94.8+9.7+404.8,
    ]

    nyt['download_size'] = [
        280,
        545,
        1100,
        676,
        1500,
        27500,
    ]

    nyt['num_requests'] = [
        172,
        88,
        93,
        30,
        70,
        87,
    ]

    nyt['kb_per_ms_http'] = [
        (.079+.142+.624+.632+1.8)/(75+96+101+101+62+111),
        (.313+.58+.596+.624)/(83+54+58+52),
        29.6/(41+5+32+41+42+68+69+93+126+195),
        1.9/79,
        22.1/(58+31),
        26400/(65+35+72+72+39+77+28+162+234+192+169+147+131+124+166+199+412+200+194+220+182+182+247+187+120+120+199+159+174+160+115)

    ]

    """
    Site3
    """

    site3['ttfb'] = [
        319.89,
        511.76,
        343.42,
        224.69,
        246.72,
        388.06,
    ]

    site3['compile_time'] = [
        179.4/1400,
        152/881,
        140.9/507,
        103.3/522,
        101.9/505,
        78.4/391,
    ]
    site3['execution_time'] = [
        799.4/1400,
        496.7/881,
        358.2/507,
        339.5/522,
        311.8/505,
        303.5/391,
    ]
    site3['render_time'] = [
        283.9,
        106.8,
        64.8,
        65.3,
        58.7,
        82.1
    ]
    site3['total_time'] = [
        82.6+1325.6+283.9+30.3+363.2,
        47.6+688.9+106.8+17.8+239.1,
        20.8+520.2+64.8+5+83.1,
        24.5+481.9+65.3+3.6+134.2,
        29.7+699.7+58.7+11.22+153,
        23.5+434.4+82.1+10.7+137.3,
    ]
    site3['download_size'] = [
        2900,
        1700,
        916,
        920,
        995,
        777
    ]

    site3['num_requests'] = [
        84,
        40,
        25,
        29,
        42,
        19
    ]
    site3['kb_per_ms_http'] = [
        1400/(48+68+78+78+84+84+84+85+96+96+96+100+126+130+143+202+219+220+274+317+405),
        1400 / (
        48 + 68 + 78 + 78 + 84 + 84 + 84 + 85 + 96 + 96 + 96 + 100 + 126 + 130 + 143 + 202 + 219 + 220 + 274 + 317 + 405),

    ]

    github['ttfb'] = [
        301.99,
        316.19,
        328.88,
        295.04,
        195.92,
        241.08,
        353.06,
        627.91,
        322.13,
        149.02,


    ]

    github['compile_time'] = [
        4.7/(.165+.0985),
        16.7/(.165+.0985),
        3.8/(.165+.0985),
        4.1/(.165+.0985),
        18.3/(.165+.0985),
        7.2/(.165+.0985),
        5.1/(.165+.0985),
        5.3/(.165+.0985),

    ]

    github['execution_time'] = [
        231.4/(.165+.0985),
        302.2/(.165+.0985),
        257.3/(.165+.0985),
        307.5/(.165+.0985),
        263.9/(.165+.0985),
        239.4/(.165+.0985),
        228.4/(.165+.0985),
        218.3/(.165+.0985)
    ]

    github['render_time'] = [
        43.4,
        62.6,
        18.1,
        61.7,
        21.8,
        2561.8,
        21.0,
        54.3,
        45.3,
        28.6,
    ]

    github['total_time'] = [
        86.7+32.1+43.4+280.3+34.1,
        32.1+281.3+62.6+3.1+41.7,
        30.6+274.8+18.1+1.4+53.6,
        33.7+309+61.7+8+67.7,
        29.8+285.5+21.8+2.1+83.7,
        89.8+620.1+2561.8+386+247.8,
        31.4+241.4+21+1.8+79.7,
        1.8+81.6+54.3+35.4+101.5,
        35.1+243.6+45.3+81.5+126.7,
        28.7+267.8+28.6+10.5+165.9


    ]

    github['download_size'] = [
        97.1,
        82.2,
        120,
        152,
        94.3,
        263,
        59.5,
        39.6,
        358,
        35.9
    ]


    github['num_requests'] = [
        19,
        19,
        16,
        27,
        15,
        100,
        13,
        15,
        52,
        15
    ]

    github['kb_per_ms_http'] = [
        (2.9+3.1)/(267+272),
        (2.9 + 2.7 + 3.0 + 5.3)/(254+256+266+260),
        (2.9 + 2.7 + 3.2 + 8.5)/(528+293+302+471),
        220/1120,
        2.6/395,
        (8.1+2.6+2.6+2.6+2.6+2.6)/(729+134+446+213+193+169),

    ]

    sites = [github, nyt, site3]
    s = ["github", "nyt", "site3"]
    site_str = [retrieve_name(site) for site in sites]
    site_str.append("all")
    means = {'github': [], 'nyt': [], 'site3': [], 'all': []}
    medians = {'github': [], 'nyt': [], 'site3': [], 'all': []}
    std_dev = {'github': [], 'nyt': [], 'site3': [], 'all': []}
    devs = []
    meds = []
    ms = []

    for i in range(len(sites)):
        obj = dict.fromkeys(site_str, {})
        for key, v in sites[i].items():
            devs.extend([{key: v}])
            meds.extend([{key: v}])
            ms.extend([{key: v}])

            std_dev[s[i]].append({key: statistics.stdev(v)})
            medians[s[i]].append({key: statistics.median(v)})
            means[s[i]].append({key: statistics.mean(v)})
    all = [devs, meds, ms]
    for key in github.keys():
        for nums in all:
            key_list = []
            for num in nums:
                if key in num.keys():
                    key_list.append(num[key])
            flat_list = [item for sublist in key_list for item in sublist]
            dev = statistics.stdev(flat_list)
            med = statistics.stdev(flat_list)
            me = statistics.stdev(flat_list)
        std_dev['all'].append({key: dev})
        medians['all'].append({key: med})
        means['all'].append({key: me})

    print(medians)
    print(std_dev)
    print(means)
    traces = []

    desired_times = ['ttfb', 'render_time', 'total_time']
    js = ['compile_time', 'execution_time']

    for i in range(len(means.keys())):
        mean = means[list(means.keys())[i]]
        d = std_dev[list(means.keys())[i]]
        m1 = []
        m2 = []
        for key in mean:
            m1.append(key[list(key.keys())[0]]) if list(key.keys())[0] in desired_times else None
        for key in d:
            m2.append(key[list(key.keys())[0]]) if list(key.keys())[0] in desired_times else None
        print(m1)
        names = {
            "github": "github.com",
            "nyt": "nytimes.com",
            "site3": "mycourses.rit.edu",
            "all": "Average website performance"
        }
        trace = go.Bar(
            x=["Time to First Byte", "Render Time",
               "Total Time"],
            y=m1,
            name=names[list(means.keys())[i]],
            error_y=dict(
                type='data',
                array=m2,
                visible=True
            )
        )

        traces.append(trace)

    layout = go.Layout(
        barmode='group',
        yaxis=dict(
            title='Milliseconds'
        )
    )

    fig=go.Figure(data=traces, layout=layout)
    py.iplot(fig, filename="lab6")