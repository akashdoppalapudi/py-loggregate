# SPDX-License-Identifier: GPL-3.0-only

import argparse

def arg_parser()-> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="Loggregate",
        description="Aggregates, Analyses and Generates reports from log files"
    )

    parser.add_argument('glob_pattern')
    parser.add_argument('-d', '--datetime-format', required=True)
    parser.add_argument('-u', '--user')

    return parser
