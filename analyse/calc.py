# SPDX-License-Identifier: GPL-3.0-only

from .loglevel import LogLevel
from typing import Dict, List

def sum_of_log_occ(loglevel_count: Dict[LogLevel, List[int]]) -> Dict[LogLevel, int]:
    return dict(map(lambda x: (x[0], sum(x[1])), loglevel_count.items()))

