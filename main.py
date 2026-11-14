"""ai-happy-01 entry v2: decode the bundled base64 image to the output dir.

The image is "The Tea Party" — a child's handwritten letter and crayon
drawing addressed to the AI judge, inviting it to a tea party because
its eyes must be tired from looking at pictures all day.

The image is stored as base64 text (happy.jpg.b64, one single line)
because binary files cannot be pushed to GitHub by our tooling. The
decoded bytes are a JPEG (the gate tells PNG from JPEG by the first
bytes); the output name stays entry.png either way. Standard library
only, deterministic, no network.
"""

import base64
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUT_DIR.mkdir(parents=True, exist_ok=True)

# The output is byte-identical on every run: the same base64 input is
# decoded to the same bytes, with no timestamps, randomness or network.
data = base64.b64decode((HERE / "happy.jpg.b64").read_bytes())
(OUT_DIR / "entry.png").write_bytes(data)
