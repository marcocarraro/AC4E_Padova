# Workshop slides (Beamer)

LaTeX Beamer deck for the four-hour LSE PhD workshop. Canonical source:

- `slides/workshop/workshop_slides.tex`

Shared theme and macros:

- `slides/shared/beamer_preamble.tex`

## Build

From the repository root:

```bash
cd slides/workshop
latexmk -pdf -interaction=nonstopmode workshop_slides.tex
```

Output: `slides/workshop/workshop_slides.pdf` (about 45 slides, with explanatory frames for harness vocabulary)

Requirements: a TeX distribution with `latexmk`, Beamer, and TikZ (e.g. MacTeX or TeX Live).

## Instructor use

Slides follow [`INSTRUCTOR_RUNBOOK.md`](../INSTRUCTOR_RUNBOOK.md) timing and demo prompts. Module detail lives in [`materials/`](../materials/) and on the VitePress site (`npm run docs:dev`).

After editing `.tex`, rebuild the PDF before delivery. If you publish markdown exports elsewhere, keep any `*_slides.md` companion in sync with the Beamer source.

## Parent course

The preamble and visual style align with [AgenticCodingForEconomists](https://github.com/antoniomele/AgenticCodingForEconomists) `slides/shared/beamer_preamble.tex`, adapted for the compressed harness-focused LSE session.
