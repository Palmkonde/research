# Research vault

Research vault for a human reader (in Obsidian) and for agents. The terms Field, Topic, Question, Finding, Source, Prerequisite and Deep dive mean exactly what GLOSSARY.md says. The Fields are listed in README.md.

## Research run

Each run answers one Question with one Finding.

1. **Place the Question** at `<field>/<topic>/`. Pick the Topic's *home* Field: the one where a reader would look for it first. A new Field gets created only when no existing Field fits; add its one-line definition to README.md when you create it.
2. **Write or expand the Finding** at `<field>/<topic>/<question-slug>.md`. If a Finding already exists for this Question, expand that file. A request to elaborate adds or extends its `## Deep dive` section.
3. **Record each Source** cited in the Finding as a Source note. If a note for that Source already exists anywhere in the vault, link to the existing note instead of creating a new one.
4. **Update the Topic README**: tick the Question and link it to its Finding, and add each Follow-up as an open Question.
5. **Stub each missing Prerequisite**: create its Topic README in the Prerequisite's own home Field. Give it a ~5-line overview covering only what the dependent Topic needs, plus open Questions, and no Findings. Then link it under the dependent Topic's `## Prerequisites`.

The run is **done** when all of these are true:
- every claim sentence in the Finding has a footnote or is marked *(inference)*;
- every footnote resolves to a Source note;
- the Topic README reflects the Finding and its Follow-ups;
- every linked Prerequisite has a Topic README.

## Conventions

- **Paths**: every Topic lives at `<field>/<topic>/`, exactly two levels deep. Use kebab-case for every file and folder name.
- **One home**: a Topic lives in one Field only. Other Topics reach it through links.
- **Links**: write standard Markdown links, `[text](relative/path.md)`, so they resolve in Obsidian, on GitHub and for agents.

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
- a link to the local copy, if one is kept beside the note,
- the date fetched.

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
