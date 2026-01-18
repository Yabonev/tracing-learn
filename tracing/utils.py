

import datetime
from time import timezone


def time_iso() -> str:
    return datetime.now(timezone.utc).isoformat()