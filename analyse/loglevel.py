# SPDX-License-Identifier: GPL-3.0-only

from enum import Enum
import re
from re import Pattern
from typing import Dict, List

class LogLevel(Enum):
    Emergency = 1
    Alert = 2
    Critical = 3
    Error = 4
    Warning = 5
    Notice = 6
    Info = 7
    Debug = 8
    Others = 9


def to_loglevel(loglevel_str: str) -> LogLevel:
    match loglevel_str.upper():
        case "INFO":
            return LogLevel.Info
        case "INFORMATION":
            return LogLevel.Information
        case "DEBUG":
            return LogLevel.Debug
        case "WARNING":
            return LogLevel.Warning
        case "WARN":
            return LogLevel.Warning
        case "ERROR":
            return LogLevel.Error
        case "NOTICE":
            return LogLevel.Notice
        case "CRITICAL":
            return LogLevel.Critical
        case "ALERT":
            return LogLevel.Alert
        case "EMERGENCY":
            return LogLevel.Emergency
        case _:
            return LogLevel.Others

def make_loglevel_count_map() -> Dict[LogLevel, int]:
    return {
        LogLevel.Info: 0,
        LogLevel.Debug: 0,
        LogLevel.Warning: 0,
        LogLevel.Error: 0,
        LogLevel.Notice: 0,
        LogLevel.Critical: 0,
        LogLevel.Alert: 0,
        LogLevel.Emergency: 0,
        LogLevel.Others: 0
    }

def make_loglevel_count_vec_map() -> Dict[LogLevel, List[int]]:
    return {
        LogLevel.Info: [],
        LogLevel.Debug: [],
        LogLevel.Warning: [],
        LogLevel.Error: [],
        LogLevel.Notice: [],
        LogLevel.Critical: [],
        LogLevel.Alert: [],
        LogLevel.Emergency: [],
        LogLevel.Others: []
    }

def loglevel_regex_pattern() -> Pattern:
    pattern = "(info|information|debug|warning|warn|error|notice|critical|alert|emergency)"
    return re.compile(pattern, re.IGNORECASE)
