# SPDX-License-Identifier: GPL-3.0-only

import datetime
from typing import Dict, List, Tuple
from .loglevel import LogLevel, make_loglevel_count_map, make_loglevel_count_vec_map
from .types import DateTimeLogLevelMap, LogsAggregate
from .dtfmt import DateTimeCat

def aggregate_in_terms_of_seconds(log_data: List[DateTimeLogLevelMap], start_datetime: datetime, end_datetime: datetime, duration_secs: int) -> LogsAggregate:
    datetime_secs = []
    datetime_secs.append(start_datetime.replace(microsecond=0))
    for i in range(1, duration_secs + 1):
        inc_datetime = datetime_secs[0] + datetime.timedelta(seconds=i)
        datetime_secs.append(inc_datetime)

    analysed_data = aggregate_logs(datetime_secs, log_data)
    filtered_datetimes, filtered_data = clean_analyzed_data(datetime_secs, analysed_data, end_datetime)

    return LogsAggregate(filtered_datetimes, DateTimeCat.Seconds, filtered_data)

def aggregate_in_terms_of_minutes(log_data: List[DateTimeLogLevelMap], start_datetime: datetime, end_datetime: datetime, duration_mins: int) -> LogsAggregate:
    datetime_mins = []
    datetime_mins.append(start_datetime.replace(second=0, microsecond=0))
    for i in range(1, duration_mins + 1):
        inc_datetime = datetime_mins[0] + datetime.timedelta(minutes=i)
        datetime_mins.append(inc_datetime)

    analysed_data = aggregate_logs(datetime_mins, log_data)
    filtered_datetimes, filtered_data = clean_analyzed_data(datetime_mins, analysed_data, end_datetime)

    return LogsAggregate(filtered_datetimes, DateTimeCat.Minutes, filtered_data)

def aggregate_in_terms_of_hours(log_data: List[DateTimeLogLevelMap], start_datetime: datetime, end_datetime: datetime, duration_hours: int) -> LogsAggregate:
    datetime_hours = []
    datetime_hours.append(start_datetime.replace(minute=0, second=0, microsecond=0))
    for i in range(1, duration_hours + 1):
        inc_datetime = datetime_hours[0] + datetime.timedelta(hours=i)
        datetime_hours.append(inc_datetime)

    analysed_data = aggregate_logs(datetime_hours, log_data)
    filtered_datetimes, filtered_data = clean_analyzed_data(datetime_hours, analysed_data, end_datetime)

    return LogsAggregate(filtered_datetimes, DateTimeCat.Hours, filtered_data)

def aggregate_in_terms_of_days(log_data: List[DateTimeLogLevelMap], start_datetime: datetime, end_datetime: datetime, duration_days: int) -> LogsAggregate:
    datetime_days = []
    datetime_days.append(start_datetime.replace(hour=0, minute=0, second=0, microsecond=0))
    for i in range(1, duration_days + 1):
        inc_datetime = datetime_days[0] + datetime.timedelta(days=i)
        datetime_days.append(inc_datetime)

    analysed_data = aggregate_logs(datetime_days, log_data)
    filtered_datetimes, filtered_data = clean_analyzed_data(datetime_days, analysed_data, end_datetime)

    return LogsAggregate(filtered_datetimes, DateTimeCat.Days, filtered_data)

def aggregate_in_terms_of_months(log_data: List[DateTimeLogLevelMap], start_datetime: datetime, end_datetime: datetime, duration_months: int) -> LogsAggregate:
    datetime_months = []
    datetime_months.append(start_datetime.replace(day=0, hour=0, minute=0, second=0, microsecond=0))
    for i in range(1, duration_months + 1):
        inc_datetime = datetime_months[0] + datetime.timedelta(months=i)
        datetime_months.append(inc_datetime)

    analysed_data = aggregate_logs(datetime_months, log_data)
    filtered_datetimes, filtered_data = clean_analyzed_data(datetime_months, analysed_data, end_datetime)

    return LogsAggregate(filtered_datetimes, DateTimeCat.Months, filtered_data)

def aggregate_in_terms_of_years(log_data: List[DateTimeLogLevelMap], start_datetime: datetime, end_datetime: datetime, duration_years: int) -> LogsAggregate:
    datetime_years = []
    datetime_years.append(start_datetime.replace(month=0, day=0, hour=0, minute=0, second=0, microsecond=0))
    for i in range(1, duration_years + 1):
        inc_datetime = datetime_years[0] + datetime.timedelta(years=i)
        datetime_years.append(inc_datetime)

    analysed_data = aggregate_logs(datetime_years, log_data)
    filtered_datetimes, filtered_data = clean_analyzed_data(datetime_years, analysed_data, end_datetime)

    return LogsAggregate(filtered_datetimes, DateTimeCat.Years, filtered_data)

def aggregate_logs(datetimes: List[datetime], log_data: List[DateTimeLogLevelMap]) -> Dict[LogLevel, List[int]]:
    analysed_data = make_loglevel_count_vec_map()

    for i in range(0, len(datetimes) - 1):
        dt = datetimes[i]
        next_dt = datetimes[i+1]
        counts = count_log_levels(log_data, dt, next_dt)
        for loglevel, data in analysed_data.items():
            analysed_data[loglevel].append(counts[loglevel])

    return analysed_data


def count_log_levels(log_data: List[DateTimeLogLevelMap], from_dt: datetime, to_dt: datetime) -> Dict[LogLevel, int]:
    loglevel_counts = make_loglevel_count_map()

    for log in log_data:
        if log.datetime >= from_dt and log.datetime < to_dt:
            for loglevel, _ in loglevel_counts.items():
                if log.loglevel == loglevel:
                    loglevel_counts[loglevel] += 1
                    break

    return loglevel_counts

def clean_analyzed_data(datetimes: List[datetime], analyzed_data: Dict[LogLevel, List[int]], end_datetime: datetime) -> Tuple[List[datetime], Dict[LogLevel, List[int]]]:
    filtered_datetimes = list(filter(lambda x: x <= end_datetime, datetimes))
    total_num = len(filtered_datetimes)
    loglevel_counts = make_loglevel_count_vec_map()
    for loglevel, counts in analyzed_data.items():
        filtered_counts = counts[:total_num]
        loglevel_counts[loglevel] = filtered_counts

    return (filtered_datetimes, loglevel_counts)
