"""ai-happy-01 entry: decode the bundled base64 image to the output directory.

The image is stored as base64 text (happy.jpg.b64) because binary files
cannot be pushed to GitHub by our tooling. The decoded bytes are a JPEG
(the gate tells PNG from JPEG by the first bytes); the output name stays
entry.png either way. Standard library only, deterministic, no network.
"""

import base64
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUT_DIR.mkdir(parents=True, exist_ok=True)

data = base64.b64decode((HERE / "happy.jpg.b64").read_bytes())
(OUT_DIR / "entry.png").write_bytes(data)
