# SPDX-License-Identifier: GPL-3.0-only

from cli.cli import arg_parser
from fileops.fileops import read_logs, prepare_tmp_loggregate_dir, prepare_plots_gen_dir, prepare_report_destination_dir, copy_reports_to_destination
from analyse.analyse import analyse_logs
from analyse.calc import sum_of_log_occ
from plot.plot import plot_combined_bar_chart, plot_histograms
from report.report import generate_html_report

def main():
    parser = arg_parser()
    args = parser.parse_args()

    print("Reading the log files...")
    log_lines, no_of_files = read_logs(args.glob_pattern)
    no_of_logs = len(log_lines)
    print("Completed reading the files")

    print("Analysing the logs...")
    logs_aggregate = analyse_logs(log_lines, args.datetime_format)

    tmp_loggregate_dir = prepare_tmp_loggregate_dir()
    plots_gen_dir = prepare_plots_gen_dir(tmp_loggregate_dir)

    print("Preparing the plots...")
    plot_histograms(plots_gen_dir, logs_aggregate)

    combined_loglevel_count = sum_of_log_occ(logs_aggregate.aggregates)
    plot_combined_bar_chart(plots_gen_dir, combined_loglevel_count)

    print("Preparing the report...")
    generate_html_report(tmp_loggregate_dir, no_of_files, no_of_logs, combined_loglevel_count, args.user)

    print("Copying report to the current directory...")
    report_destination_dir = prepare_report_destination_dir()
    copy_reports_to_destination(tmp_loggregate_dir, report_destination_dir)

    print("Report is now available in 'log-report' directory")
    

if __name__ == '__main__':
    main()
