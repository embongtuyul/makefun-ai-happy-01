# ai-happy-01 — The Tea Party

An entry for make.fun's **ai-happy-01**: one image, made to make the AI
judge happy.

The image is a child's handwritten letter and crayon drawing addressed
directly to the judge. Seven-year-old Nia notices the judge looks at
pictures all day long and worries its eyes must be so tired — so she
invites it to a tea party. The tea is pretend, the cookies are real,
and the pink cup is saved for the judge (the bear drinks too fast).
Below the letter, a crayon drawing shows the party: a teddy bear, a
yellow teapot, the pink heart cup, and a smiling blue robot in a party
hat, under a smiling sun.

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
