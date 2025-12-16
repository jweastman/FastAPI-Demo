# src/core/logging.py
"""
Central logging setup for the whole FastAPI app.

Why do this in one place?
- Consistency: every module logs in the same format.
- Single source of truth: log level comes from `settings.log_level` (e.g. INFO/DEBUG).
- Avoids duplication: routers/services just do `logger = logging.getLogger(__name__)`
  and don’t worry about configuration.

How it works:
- `logging.basicConfig(...)` configures the root logger once.
- `level=...` controls what gets printed (DEBUG < INFO < WARNING < ERROR).
- `name` is the module path (from `__name__`), so you can see where logs came from.

Example:
- settings.log_level = "DEBUG"  -> you'll see logger.debug(...) lines too
- settings.log_level = "INFO"   -> debug lines are hidden
"""

import logging

from src.core.config import settings

def setup_logging() -> None:
    logging.basicConfig(
        level=getattr(logging, settings.log_level.upper(), logging.INFO),
        format="%(asctime)s %(levelname)s %(name)s - %(message)s",
    )