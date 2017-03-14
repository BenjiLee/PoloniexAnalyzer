import time

from matplotlib import pyplot as plot


class bcolors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    END_COLOR = '\033[0m'


def _get_epoch(date_string):
    pattern = '%Y-%m-%d %H:%M:%S'
    epoch = int(time.mktime(time.strptime(date_string, pattern)))
    return epoch - 14400


def _to_percent_change(number):
    if not isinstance(number, float):
        number = float(number)
    return "{:.2f}%".format(number * 100 - 100)


def _plot_graph(graph_data_dict):
    x = graph_data_dict['x']
    y = graph_data_dict['y']
    colors = graph_data_dict['colors']
    title = graph_data_dict['title']
    x_label = graph_data_dict['x-label']
    y_label = graph_data_dict['y-label']

    plot.plot_date(x, y, marker=None)
    plot.plot(x, y)
    plot.scatter(x, y, color=colors)
    plot.axes().grid(color='k', linestyle='-', linewidth=.1)
    plot.title(title)
    plot.xlabel(x_label)
    plot.ylabel(y_label)
    plot.xticks(rotation=30)
    plot.show()
