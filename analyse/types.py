# SPDX-License-Identifier: GPL-3.0-only

from typing import List, Dict
from .dtfmt import DateTimeCat
from .loglevel import LogLevel
import datetime

class DateTimeLogLevelMap:
    def __init__(self, datetime: datetime, loglevel: LogLevel):
        self.datetime = datetime
        self.loglevel = loglevel

class LogsAggregate:
    def __init__(self, datetimes: List[datetime], datetime_cat: DateTimeCat, aggregates: Dict[LogLevel, List[int]]):
        self.datetimes = datetimes
        self.datetime_cat = datetime_cat
        self.aggregates = aggregates
