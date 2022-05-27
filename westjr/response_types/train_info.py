# [/api/v3/area_{AREA}_trafficinfo.json]
from __future__ import annotations

from typing import Any, TypedDict


class TrainInfo(TypedDict):
    lines: dict[str, Any]
    express: dict[str, Any]
