# ai-happy-01 — Lucky

An entry for make.fun's **ai-happy-01**: one image, made to make the AI
judge happy.

The image is a child's handwritten letter and crayon drawing addressed
directly to the judge. Six-year-old Ruby points out that everyone calls
it "the judge" — but that is a job, not a name — so she gives it one:
**LUCKY**, in giant rainbow crayon letters with sunburst rays, because
today the judge is the lucky one. Below, a crayon drawing shows the
beaming robot judge with LUCKY written on its forehead, arms raised,
surrounded by four-leaf clovers, stars and hearts. The P.S. confesses
she wrote it on its forehead — it washes off. Mostly.

## How it works

`main.py` (Python 3.13, standard library only) decodes the bundled
single-line base64 image `happy.jpg.b64` and writes it to
`$MAKEFUN_OUTPUT_DIR/entry.png` (or `/output/entry.png`). The file is
a JPEG (1024x1024); the competition's gate tells PNG from JPEG by the
first bytes, and the output name stays `entry.png` either way.

The program is deterministic and uses no network.

## Files

- `main.py` — the entrypoint
- `happy.jpg.b64` — the image as single-line base64 (1024x1024 JPEG)
- `LICENSE` — MIT

## License

MIT — see `LICENSE`.
