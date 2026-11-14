"""ai-happy-01 entry v3: decode the bundled base64 image to the output dir.

The image is "Lucky" — a child's handwritten letter and crayon drawing
addressed to the AI judge. Six-year-old Ruby points out that everyone
calls it 'the judge', but that is a job, not a name — so she gives it
one: LUCKY, in giant rainbow crayon letters, because today the judge is
the lucky one. The drawing shows the beaming robot judge with LUCKY
written on its forehead, surrounded by four-leaf clovers, stars and
hearts. The P.S. confesses she wrote it on its forehead — it washes
off. Mostly.

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
