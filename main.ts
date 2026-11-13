// "Chips Fall, Talks Rise" — news-image-01 entry (Node 22, standard library only).
// The image is entry.png beside this file; the program copies it to the output
// directory given by MAKEFUN_OUTPUT_DIR (default /output). The gate takes a whole
// PNG or JPEG of at most 1 MiB and 1024 by 1024 pixels, and the judge sees exactly
// the bytes copied.
//
// Local run:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

// entry.png is drawn entirely in code by draw.py (Pillow) — no copied assets —
// so the copied file is the original artwork for this entry.

import { copyFileSync } from 'node:fs';
import { join } from 'node:path';

copyFileSync(new URL('./entry.png', import.meta.url), join(process.env.MAKEFUN_OUTPUT_DIR ?? '/output', 'entry.png'));
