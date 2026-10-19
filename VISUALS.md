# Visuals

How a Finding gets figures and animations. A visual illustrates claims the prose already makes and footnotes; it never adds a new claim.

## The ladder

Pick the lowest rung that shows the mechanism:

1. **LaTeX**: equations and matrices, inline in the Finding.
2. **Mermaid**: flowcharts, relations between gates, state machines, inline as a ` ```mermaid ` block. Circuits with ⊕ targets go up a rung.
3. **Static figure**, committed under `assets/<question-slug>/`:
   - an openly licensed web image (search first), or
   - a hand-written `.svg`, or
   - when neither works, a PNG or JPG used directly.
4. **Animation**: a manimgx scene, only when the motion itself is the point (a rotation, a path, a sweep).

## Captions

Put an italic caption line directly under every embed, starting `*Figure:`, `*Diagram:` or `*Animation:`. Each caption sentence carries a footnote or (inference), like any claim sentence; the caption is already italic, so write the marker without asterisks. An animation's caption describes what happens on screen, because GitHub and agents cannot play the video. Write alt text in words, with no `|`, since Obsidian reads `|` in alt text as a size.

## Web images

1. Use only openly licensed images (Wikimedia Commons, CC BY, CC BY-SA). Link to anything else instead of copying it.
2. Download into a fresh scratch directory with a user agent set (`curl -A '...'`), since Wikimedia refuses curl's default. For an SVG, grep for `<script` before copying it into `assets/`.
3. Give it a Source note that records the author, the license with its URL, and any change you made, and links the local copy in `assets/`.
4. Footnote that Source note in the caption.

## Hand-written SVG

- Give it a white background `<rect>` and black strokes: Obsidian's default theme is dark, and a transparent SVG with black lines disappears there. Add the same rect to a downloaded image that lacks one, and record the change in its Source note.
- Check the render before embedding it: `qlmanage -t -s 600 -o <scratch-dir> file.svg`, then view the PNG.
- Example: [swap-from-three-cnots.svg](quantum-computing/quantum-computing-basics/assets/common-gates-action/swap-from-three-cnots.svg).

## Animations (manimgx)

[manimgx](https://github.com/academa-labs/manimgx) uses the Manim CE API (`import manimgx as m`), needs Python 3.13 or 3.14, and typesets math itself, so it needs no LaTeX or ffmpeg. Its full API is at <https://manimgx.academa.ai/llms-full.txt>; download it once and grep it, rather than guessing class names.

1. **Write the scene** as `assets/<question-slug>/<name>.py`. Its docstring holds its exact render command:
   ```
   uvx --python 3.14 manimgx@0.1.1 render <name>.py -o <name>.mp4 -r 1280x720 --fps 30
   ```
2. **Inspect**: run `uvx --python 3.14 manimgx@0.1.1 inspect <name>.py` from the scene's folder, and fix every reported problem.
3. **View the storyboard** PNG it writes, and check each frame against the caption. This is the real check for 3D scenes, since `inspect` skips layout checks for them.
4. **Render** with the docstring command.
5. **Embed** it with `![<alt>](assets/<question-slug>/<name>.mp4)`.

Git ignores renders (`*.mp4`, `*.storyboard*.png`, `*.srt`), so the `.py` file is the only thing that reproduces the video. Keep the version pin in its command.

Scene-writing gotchas:
- Rotate a vector about the origin, `m.Rotate(arrow, angle, axis=..., about_point=m.ORIGIN)`. The default pivot is the mobject's own center, which makes an arrow wobble instead of sweep.
- Start each motion from a state that makes it visible. For example, a $z$ rotation does nothing visible to $\lvert 0\rangle$, so start it at $\lvert +\rangle$ or above the equator.
- Text placed in a 3D scene lies flat. Stand it up to face the camera, and pin titles with `self.add_fixed_in_frame_mobjects`.
- Example: [bloch-gate-rotations.py](quantum-computing/quantum-computing-basics/assets/common-gates-action/bloch-gate-rotations.py).

## Rendering every animation

After cloning, run this from the vault root to render all scenes:

```sh
find . -path '*/assets/*/*.py' -execdir sh -c 'uvx --python 3.14 manimgx@0.1.1 render "$1" -o "${1%.py}.mp4" -r 1280x720 --fps 30' _ {} \;
```
