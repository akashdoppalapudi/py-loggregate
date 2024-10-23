# SPDX-License-Identifier: GPL-3.0-only

import sys
from datetime import datetime
from typing import List, Set
import math
from .loglevel import LogLevel, loglevel_regex_pattern, to_loglevel
from .dtfmt import DateTimeCat, dt_fmt_to_regex
from .aggregate import aggregate_in_terms_of_seconds, aggregate_in_terms_of_minutes, aggregate_in_terms_of_hours, aggregate_in_terms_of_days
from .types import LogsAggregate, DateTimeLogLevelMap

MIN_SECONDS = 60
HOUR_SECONDS = MIN_SECONDS * 60
DAY_SECONDS = HOUR_SECONDS * 24
MONTH_SECONDS = DAY_SECONDS * 31
YEAR_SECONDS = MONTH_SECONDS * 21

def analyse_logs(log_lines: List[str], datetime_format: str) -> LogsAggregate:
    log_data: List[DateTimeLogLevelMap] = []
    unq_datetimes: Set[datetime] = set()

    dt_regex_pattern = dt_fmt_to_regex(datetime_format)
    ll_regex_pattern = loglevel_regex_pattern()
    for log in log_lines:
        dt_match = dt_regex_pattern.search(log)
        if not dt_match:
            print(f"Error finding date with given format in line: {log}", file=sys.stderr)
            continue;
        dt = datetime.strptime(dt_match.group(), datetime_format)
        
        loglevel_str = "others"
        ll_match = ll_regex_pattern.search(log)
        if ll_match:
            loglevel_str = ll_match.group()
        loglevel = to_loglevel(loglevel_str)

        unq_datetimes.add(dt)
        log_data.append(DateTimeLogLevelMap(dt, loglevel))

    mindt = min(unq_datetimes)
    maxdt = max(unq_datetimes)

    logs_duration = (maxdt - mindt).total_seconds()

    if logs_duration > YEAR_SECONDS:
        duration_years = math.ceil(logs_duration / YEAR_SECONDS)
        print(duration_years)
        print("Analyse in terms of years")
    elif logs_duration > MONTH_SECONDS:
        duration_months = math.ceil(logs_duration / MONTH_SECONDS)
        print(duration_months)
        print("Analyse in terms of months")
    elif logs_duration > DAY_SECONDS:
        duration_days = math.ceil(logs_duration / DAY_SECONDS)
        logs_aggregate = aggregate_in_terms_of_days(log_data, mindt, maxdt, duration_days)
        print("Analyse in terms of days")
    elif logs_duration > HOUR_SECONDS:
        duration_hours = math.ceil(logs_duration / HOUR_SECONDS)
        logs_aggregate = aggregate_in_terms_of_hours(log_data, mindt, maxdt, duration_hours)
        print("Analyse in terms of hours")
    elif logs_duration > MIN_SECONDS:
        duration_mins = math.ceil(logs_duration / MIN_SECONDS)
        logs_aggregate = aggregate_in_terms_of_minutes(log_data, mindt, maxdt, duration_mins)
        print("Analyse in terms of minutes")
    else:
        duration_secs = math.ceil(logs_duration)   
        logs_aggregate = aggregate_in_terms_of_seconds(log_data, mindt, maxdt, duration_secs)
        print("Analyse in terms of seconds")

    return logs_aggregate
