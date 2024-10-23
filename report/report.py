# SPDX-License-Identifier: GPL-3.0-only

from analyse.loglevel import LogLevel
from typing import Dict

def generate_html_report(report_dir: str, no_of_files: int, no_of_logs: int, combined_log_level_count: Dict[LogLevel, int], user: str | None = None):
    HTML_TMPL = '<!doctype html><html lang="en"><head><meta charset="UTF-8"><title>Loggregate</title><style>body{padding:1% 10%}.page-header{display:flex;justify-content:center;padding-bottom:15px}.page-title{font-size:60px;margin:0}section{margin-bottom:2rem}.combined-logs-sec,.time-trend-sec{display:flex;justify-content:center}.combined-logs,.time-trend{width:80%}.combined-logs>h2,.combined-logs>p,.time-trend>h2,.time-trend>p{text-align:center}img.plot{width:100%;border:1px #000 solid}.trend-plot-container>.plot{margin:1rem 0}.trend-plot-container>.hide{display:none}footer>p{text-align:end}</style></head><body><header class="page-header"><h1 class="page-title">Loggregate Report</h1></header><hr><section><section class="combined-logs-sec"><div class="combined-logs"><h2>Log Analysis</h2><p>Read<b>{#NO_OF_FILES#}</b>file(s) and<b>{#NO_OF_LOGS#}</b>log(s).</p><p>These are the number of logs occured over the duration of given log files.</p><details><summary>Expand to see detailed numbers</summary><ul><li>Emergency:<b>{#NO_OF_EMERGENCY#}</b></li><li>Alert:<b>{#NO_OF_ALERT#}</b></li><li>Critical:<b>{#NO_OF_CRITICAL#}</b></li><li>Error:<b>{#NO_OF_ERROR#}</b></li><li>Warning:<b>{#NO_OF_WARNING#}</b></li><li>Notice:<b>{#NO_OF_NOTICE#}</b></li><li>Info:<b>{#NO_OF_INFO#}</b></li><li>Debug:<b>{#NO_OF_DEBUG#}</b></li><li>Others:<b>{#NO_OF_OTHERS#}</b></li></ul></details><img class="plot combined-plot" alt="" src="plots/combined.png"></div></section><hr><section class="time-trend-sec"><div class="time-trend"><h2>Log trends over time</h2><p>Log trends of different Log level types over time during the duration of logs are presented below</p><div class="trend-plot-container"><img class="plot {#EMERGENCY_VISIBILITY#}" alt="" src="plots/emergency.png"> <img class="plot {#ALERT_VISIBILITY#}" alt="" src="plots/alert.png"> <img class="plot {#CRITICAL_VISIBILITY#}" alt="" src="plots/critical.png"> <img class="plot {#ERROR_VISIBILITY#}" alt="" src="plots/error.png"> <img class="plot {#WARNING_VISIBILITY#}" alt="" src="plots/warning.png"> <img class="plot {#NOTICE_VISIBILITY#}" alt="" src="plots/notice.png"> <img class="plot {#INFO_VISIBILITY#}" alt="" src="plots/info.png"> <img class="plot {#DEBUG_VISIBILITY#}" alt="" src="plots/debug.png"> <img class="plot {#OTHERS_VISIBILITY#}" alt="" src="plots/others.png"></div></div></section></section><hr><footer><p>Created{#BY_USER#} using <a href="https://github.com/akashters/loggregate">Loggregate</a>.</p></footer></body></html>'
    html_report_path = f"{report_dir}/report.html"

    value_map = prepare_placeholder_map(no_of_files, no_of_logs, combined_log_level_count, user)
    html_text = replace_placeholders(HTML_TMPL, value_map)
    with open(html_report_path, mode='w') as file:
        file.write(html_text)


def prepare_placeholder_map(no_of_files: int, no_of_logs: int, combined_loglevel_count: Dict[LogLevel, int], user: str = None) -> Dict[str, str]:
    return {
        "NO_OF_FILES": f"{no_of_files}",
        "NO_OF_LOGS": f"{no_of_logs}",
        "NO_OF_ALERT": f"{combined_loglevel_count[LogLevel.Alert]}",
        "NO_OF_CRITICAL": f"{combined_loglevel_count[LogLevel.Critical]}",
        "NO_OF_EMERGENCY": f"{combined_loglevel_count[LogLevel.Emergency]}",
        "NO_OF_ERROR": f"{combined_loglevel_count[LogLevel.Error]}",
        "NO_OF_WARNING": f"{combined_loglevel_count[LogLevel.Warning]}",
        "NO_OF_NOTICE": f"{combined_loglevel_count[LogLevel.Notice]}",
        "NO_OF_INFO": f"{combined_loglevel_count[LogLevel.Info]}",
        "NO_OF_DEBUG": f"{combined_loglevel_count[LogLevel.Debug]}",
        "NO_OF_OTHERS": f"{combined_loglevel_count[LogLevel.Others]}",
        "ALERT_VISIBILITY": "hide" if combined_loglevel_count[LogLevel.Alert] <= 0 else "",
        "CRITICAL_VISIBILITY": "hide" if combined_loglevel_count[LogLevel.Critical] <= 0 else "",
        "EMERGENCY_VISIBILITY": "hide" if combined_loglevel_count[LogLevel.Emergency] <= 0 else "",
        "ERROR_VISIBILITY": "hide" if combined_loglevel_count[LogLevel.Error] <= 0 else "",
        "WARNING_VISIBILITY": "hide" if combined_loglevel_count[LogLevel.Warning] <= 0 else "",
        "NOTICE_VISIBILITY": "hide" if combined_loglevel_count[LogLevel.Notice] <= 0 else "",
        "INFO_VISIBILITY": "hide" if combined_loglevel_count[LogLevel.Info] <= 0 else "",
        "DEBUG_VISIBILITY": "hide" if combined_loglevel_count[LogLevel.Debug] <= 0 else "",
        "OTHERS_VISIBILITY": "hide" if combined_loglevel_count[LogLevel.Others] <= 0 else "",
        "BY_USER": "" if user == None or user == "" else f" by {user}"
    }


def replace_placeholders(text: str, value_map: Dict[str, str]) -> str:
    replaced_text = text
    for fro, to in value_map.items():
        replaced_text = replaced_text.replace(f"{{#{fro}#}}", to)

    return replaced_text
