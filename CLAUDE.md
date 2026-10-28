# Research vault

Research vault for a human reader (in Obsidian) and for agents. The terms Field, Topic, Question, Finding, Source, Prerequisite and Deep dive mean exactly what GLOSSARY.md says. The Fields are listed in README.md.

## Workflow

Route each request by its shape:

- **Vague curiosity** ("I'm curious about X"): use the `grilling` skill to sharpen it into concrete Questions, then write them as open Questions in the Topic README.
- **One Question**, or a deep dive into an existing Finding: use the `research` skill. It does a Research run (below).
- **Broad survey** of a new Topic: use `anthropic-skills:deep-research`, and turn its report into the Topic README's overview and open Questions. Findings still come only from Research runs.
- **New vault term**: use the `domain-modeling` skill to update GLOSSARY.md.
- **Paper literature scan** of a Topic: use `academic-research-skills:deep-research` in `lit-review` or `three-way-scan` mode. Its report feeds the Topic README's overview and open Questions, never Findings.
- **Check that cited papers are real** (a Finding's Sources, or a list of papers): use `academic-research-skills:academic-paper` in `citation-check` mode. Fix or remove any Source note it fails.

When handing a Research run to a background agent, the brief names the target `<field>/<topic>/` and tells the agent to follow the "Research run" section of this file, including its done checklist. When the agent reports back, check that checklist yourself before telling the user the run is finished.

## Research run

Each run answers one Question with one Finding.

1. **Place the Question** at `<field>/<topic>/`. Pick the Topic's *home* Field: the one where a reader would look for it first. A new Field gets created only when no existing Field fits; add its one-line definition to README.md when you create it.
2. **Write or expand the Finding** at `<field>/<topic>/<question-slug>.md`, in the textbook style of the Finding template. If a Finding already exists for this Question, expand that file. A request to elaborate adds or extends its `## Deep dive` section.
3. **Add visuals**: for each mechanism the Explanation walks through (a proof step, a transformation, a circuit), pick a rung from the ladder in [VISUALS.md](VISUALS.md), cheapest first, or decide prose is enough.
4. **Record each Source** cited in the Finding as a Source note. If a note for that Source already exists anywhere in the vault, link to the existing note instead of creating a new one.
5. **Update the Topic README**: tick the Question and link it to its Finding, and add each Follow-up as an open Question.
6. **Stub each missing Prerequisite**: create its Topic README in the Prerequisite's own home Field. Give it a ~5-line overview covering only what the dependent Topic needs, plus open Questions, and no Findings. Then link it under the dependent Topic's `## Prerequisites`.

The run is **done** when all of these are true:
- every claim sentence in the Finding has a footnote or is marked *(inference)* or *(pending source)*;
- every footnote resolves to a Source note;
- every visual has a caption whose claims carry a footnote or an (inference) marker, and every animation's storyboard matches its caption;
- the Topic README reflects the Finding and its Follow-ups;
- every linked Prerequisite has a Topic README.

## Conventions

- **Paths**: every Topic lives at `<field>/<topic>/`, exactly two levels deep. Use kebab-case for every file and folder name.
- **One home**: a Topic lives in one Field only. Other Topics reach it through links.
- **Links**: write standard Markdown links, `[text](relative/path.md)`, so they resolve in Obsidian, on GitHub and for agents.
- **Assets**: a Finding's images, SVGs and animation scenes live in `<field>/<topic>/assets/<question-slug>/`.
- **Math**: write LaTeX, `$…$` inline and `$$…$$` for display. Write kets as `\lvert 0\rangle` and bras as `\langle 0\rvert`, so that no `|` splits a table cell.

### Finding

```markdown
---
question: <the Question>
date: YYYY-MM-DD
status: answered   # partial = some part of the Question is still unresolved
---

## TL;DR
<2–3 lines>

## Explanation
<opens with 2–3 sentences on why this matters; worked examples go in `### Example: …` subsections>
<each claim sentence carries a footnote[^slug]; own reasoning is marked *(inference)*>

## Deep dive
<only when requested>

## Follow-ups
- <new Questions this research raised>

[^slug]: [Source title](sources/<source-slug>.md)
```

### Source note

`<field>/<topic>/sources/<source-slug>.md` contains:
- a one-line description,
- the URL,
- a link to the local copy, if one is kept (beside the note, or in `assets/` for an image the Finding embeds),
- the date fetched.

Every Topic has a `sources/no-access.md`, created together with its README. A Source whose full text is closed to you gets a line in it (title, DOI or URL, what the Finding needs from it), not a Source note. Claims that depend on it are marked *(pending source)*. Once the user drops the downloaded copy beside it, turn the line into a Source note and footnote those claims, then delete the PDF and write `Local copy: none`.

### Project

A Project lives at `projects/<project-slug>/`. `projects/` is not a Field and holds no Topics or Findings: a Project links to the Topics it draws on, and their Source notes stay in the Topic. Each Project has a `PLAN.md` that opens with its goal and status, and whose milestones each carry a date and a checkable done criterion. A `README.md` holds the brief and scope when the Project has an outside requester. The Projects and their status are listed in README.md.

### Topic README

```markdown
# <Topic>
<2–5 line overview>

## Prerequisites
- [C basics](../../low-level/c-basics/README.md)

## Questions
- [x] [How does a stack overflow hijack RIP?](stack-overflow-rip.md)
- [ ] How does ASLR get bypassed?
```
