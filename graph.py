import matplotlib.pyplot as plot

def _plot_graph(graph_data_dict):
    x = graph_data_dict['x']
    y = graph_data_dict['y']
    colors = graph_data_dict['colors']

    plot.plot_date(x, y, marker=None)
    plot.plot(x, y)
    plot.scatter(x, y, color=colors)
    plot.axes().grid(color='k', linestyle='-', linewidth=.1)
    plot.xticks(rotation=30)
    plot.show()
