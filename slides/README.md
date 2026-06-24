# Workshop Slides (Beamer)

LaTeX Beamer deck for the 5-hour Padova workshop. Canonical source:

- `slides/workshop/workshop_slides.tex`

Slide-to-demo map:

- `slides/workshop/demo_map.md`

Shared theme and macros:

- `slides/shared/beamer_preamble.tex`

## Build

From the repository root:

```bash
cd slides/workshop
latexmk -pdf -interaction=nonstopmode workshop_slides.tex
```

Output: `slides/workshop/workshop_slides.pdf`.

Requirements: a TeX distribution with `latexmk`, Beamer, and TikZ (e.g. MacTeX or TeX Live).

## Instructor use

Slides follow [`SCHEDULE.md`](../SCHEDULE.md), [`GUIDE.md`](../GUIDE.md), and
the demo order in [`slides/workshop/demo_map.md`](workshop/demo_map.md).
Participant detail lives in [`materials/`](../materials/) and the example paths
called out directly in the deck.

After editing `.tex`, rebuild the PDF before delivery.

## Source Notes

The deck keeps the imported Beamer theme but is adapted to the Padova sequence
and the Card-Krueger running example from `AC4E_Pavia`.
