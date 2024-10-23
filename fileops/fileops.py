# SPDX-License-Identifier: GPL-3.0-only

import glob
from typing import Tuple, List
from tempfile import gettempdir
from os.path import isdir
from os import getcwd
from shutil import rmtree, copytree
from pathlib import Path

def read_logs(glob_pattern: str) -> Tuple[List[str], int]:
    file_paths = glob.glob(glob_pattern)
    log_lines = []
    for path in file_paths:
        with open(path) as file:
            for line in file:
                log_lines.append(line.rstrip())


    return (log_lines, len(file_paths))

def prepare_tmp_loggregate_dir() -> str:
    tmp_dir = gettempdir()
    tmp_loggregate_dir = tmp_dir + "/loggregate"

    if isdir(tmp_loggregate_dir):
        rmtree(tmp_loggregate_dir)

    return tmp_loggregate_dir

def prepare_plots_gen_dir(tmp_loggregate_dir: str) -> str:
    plots_gen_dir = f"{tmp_loggregate_dir}/plots"
    Path(plots_gen_dir).mkdir(parents=True, exist_ok=True)
    return plots_gen_dir

def prepare_report_destination_dir() -> str:
    cur_dir = getcwd()
    report_dest_dir = f"{cur_dir}/log-report"
    if isdir(report_dest_dir):
        rmtree(report_dest_dir)

    Path(report_dest_dir).mkdir(parents=True, exist_ok=True)
    return report_dest_dir

def copy_reports_to_destination(tmp_loggregate_dir: str, report_destination_dir: str):
    copytree(src=tmp_loggregate_dir, dst=report_destination_dir, dirs_exist_ok=True)


