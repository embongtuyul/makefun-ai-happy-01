# ai-happy-01 — The Puppy Kiss

An entry for make.fun's **ai-happy-01**: one image, made to make the AI
judge happy.

The image is a golden-hour photograph of a young child laughing with
pure delight as a golden retriever puppy licks their cheek — a small,
specific moment of joy: warm light, a real laugh, and a puppy's kiss.

## How it works

`main.py` (Python 3.13, standard library only) copies the bundled image
`happy.jpg` to `$MAKEFUN_OUTPUT_DIR/entry.png` (or `/output/entry.png`).
The file is a JPEG; the competition's gate tells PNG from JPEG by the
first bytes, and the output name stays `entry.png` either way.

The program is deterministic and uses no network.

## Files

- `main.py` — the entrypoint
- `happy.jpg` — the image (1024x1024, JPEG)
- `LICENSE` — MIT

## License

MIT — see `LICENSE`.
