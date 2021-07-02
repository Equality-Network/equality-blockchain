import os
from pathlib import Path

DEFAULT_ROOT_PATH = Path(os.path.expanduser(os.getenv("EQUALITY_ROOT", "~/.equality/mainnet"))).resolve()
