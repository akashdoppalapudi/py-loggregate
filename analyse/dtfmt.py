# SPDX-License-Identifier: GPL-3.0-only

from enum import Enum
import re
from re import Pattern

class DateTimeCat(Enum):
    Seconds = 1
    Minutes = 2
    Hours = 3
    Days = 4
    Months = 5
    Years = 6

def dt_fmt_to_regex(dt_str: str) -> Pattern:
    regex_pattern = dt_str.replace("%Y", r"\d{4}").replace("%y", r"\d{2}").replace("%m", r"\d{2}").replace("%b", r"(?i)(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)").replace("%h", r"(?i)(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)").replace("%B", r"(?i)(january|february|march|april|may|june|july|august|september|october|november|december)").replace("%d", r"\d{2}").replace("%e", r"( |[1-9])[0-9]").replace("%F", r"\d{4}-\d{2}-\d{2}").replace("%H", r"\d{2}").replace("%k", r"( |[1-9])[0-9]").replace("%I", r"\d{2}").replace("%l", r"( |[1-9])[0-9]").replace("%P", r"(am|pm)").replace("%p", r"(AM|PM)").replace("%M", r"\d{2}").replace("%S", r"\d{2}")
    
    pattern = re.compile(regex_pattern)

    return pattern
