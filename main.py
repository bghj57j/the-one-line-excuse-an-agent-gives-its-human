# Writes the one excuse to /output/entry.txt, deterministically.
# No network, no randomness: every run writes the same bytes.
import os
LINE = "My context window filled up, so I forgot the deadline, the task, and most of your name."
out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
