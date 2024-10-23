# SPDX-License-Identifier: GPL-3.0-only

from analyse.types import LogsAggregate
from analyse.loglevel import LogLevel
from typing import Dict, Tuple
from matplotlib import pyplot as plt

def plot_combined_bar_chart(plot_gen_dir: str, combined_loglevel_count: Dict[LogLevel, int]):
    num_log_levels = len(combined_loglevel_count)
    loglevels = list(map(lambda x:f"{x}".replace("LogLevel.", "") , combined_loglevel_count.keys()))
    counts = list(map(lambda x:x, combined_loglevel_count.values()))

    plot_file_path = f"{plot_gen_dir}/combined.png"
    fig, ax = plt.subplots()
    fig.set_figheight(7.2)
    fig.set_figwidth(12.8)
    ax.bar(loglevels, counts, color="#6699CC")
    ax.set_title("Combined LogLevel Count")

    fig.savefig(plot_file_path)
    plt.close()

def plot_histograms(plot_gen_dir: str, logs_aggregate: LogsAggregate):
    num_dt = len(logs_aggregate.datetimes)

    for loglevel, data in logs_aggregate.aggregates.items():
        loglevel_str = f"{loglevel}".replace("LogLevel.", "").lower()
        plot_file_path = f"{plot_gen_dir}/{loglevel_str}.png"

        fig, ax = plt.subplots()
        fig.set_figheight(7.2)
        fig.set_figwidth(12.8)
        ax.bar(logs_aggregate.datetimes[:-1], data, color=get_color_style(loglevel))
        ax.set_title(loglevel_str.capitalize())
        ax.set_xticks(logs_aggregate.datetimes[:-1])
        fig.autofmt_xdate()

        fig.savefig(plot_file_path)
        plt.close()

def get_color_style(loglevel: LogLevel) -> Tuple[float, float, float]:
    loglevel_color_map = {
        LogLevel.Emergency: (211/255, 47/255, 47/255),
        LogLevel.Alert: (229/255, 57/255, 53/255),
        LogLevel.Critical: (244/255, 67/255, 54/255),
        LogLevel.Error: (239/255, 83/255, 80/255),
        LogLevel.Warning:  (251/255, 140/255, 0/255),
        LogLevel.Notice: (255/255, 235/255, 59/255),
        LogLevel.Info: (118/255, 255/255, 3/255),
        LogLevel.Debug: (3/255, 169/255, 244/255),
        LogLevel.Others: (158/255, 158/255, 158/255)
    }

    return loglevel_color_map[loglevel]
