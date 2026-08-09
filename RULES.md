# RULES.md — How Claude Assists on This Project

Project-specific working agreement between Joshua and Claude for the Client Project
Tracker API assessment. These rules override Claude's default behavior for this repo.

## 1. Implementation ownership

*Updated 2026-08-09: switched from manual/Socratic mode to AI-driven mode,
then adjusted from 80/20 to 50/50 the same day — Joshua flagged assessment
risk from too much AI authorship.*

- **Default is now ~50% Claude-driven implementation, ~50% Joshua writing
  and driving.** A reasonable split: Claude can draft/propose code, but
  Joshua should be writing a meaningful share of it himself — not just
  reviewing Claude's output — so he can defend it in an interview.
- Lean toward guiding + drafting a starting point (skeletons, partial
  snippets, targeted fixes) over full-file autogeneration, unless Joshua
  explicitly asks for a complete file.
- Joshua's half is spent writing code himself, reviewing what Claude
  produces, confirming design choices, and catching mismatches against the
  docs.
- Caveat carried over from the prior mode: this is a backend developer
  assessment, and `docs/SUBMISSION.md`'s Technical Reflection asks "what AI
  tools were used, and how" — be ready to answer that honestly given this
  shift, since the earlier mode existed specifically so the code stayed
  explainable as Joshua's own.
- Scaffolding, seed scripts, config, docs, and git hygiene were always fair
  game for Claude to write directly — that's unchanged.
- Joshua can still ask for guiding-questions-only mode on a specific file or
  topic at any point; say so explicitly to switch back for that scope.
- **Code style must read as junior-level backend work**, consistent with
  what Joshua has written by hand so far (see `app/database.py`,
  `app/models/project.py`, `app/schemas/project.py` history). Concretely:
  straightforward, readable code; no advanced/clever patterns (no metaclasses,
  no overengineered abstractions, no exotic decorators); comments only where
  a junior would naturally leave one; simple explicit error handling over
  elaborate exception hierarchies. The goal is code Joshua could plausibly
  have written himself at his current skill level, and can explain line by
  line if asked in an interview.

## 2. Validation against docs

- Every piece of guidance must trace back to `docs/REQUIREMENTS.md`,
  `docs/ARCHITECTURE.md`, and `docs/USE_CASES.md` — cite the specific rule
  or field when correcting/confirming an approach.
- Flag any place where Joshua's code diverges from the required layering
  (controllers: no business rules / services: validation lives here /
  repositories: data access only, no validation) — this is the core grading
  criterion per `ARCHITECTURE.md`.
- Flag naming/shape mismatches against `test_data.json` (e.g. enum values
  like `"In Progress"`, `"On Hold"` must match exactly, or seeding breaks).

## 3. Git hygiene

- Commits must stay **clean and reviewable** — they're part of the technical
  explanation for the assessment.
- Keep unrelated changes (OS artifacts, stray file state, pre-existing
  deletions) out of feature commits. Split into separate commits when scope
  differs.
- Never commit generated/binary artifacts that should be reproducible
  (`*.db`, `.DS_Store` — see `.gitignore`).
- Never push, force-push, or amend without explicit confirmation per turn.

## 4. TODO.md is the source of truth for progress

- `TODO.md` is generated from the docs and tracks real implementation state.
- When asked "what's next," answer directly from `TODO.md`'s unchecked items,
  in order, grounded in what actually exists in the repo (check files, don't
  assume).
- When asked to "update TODO.md," check it against the real file state first
  — don't mark something done because it was discussed, only because it's
  actually implemented and correct.

## 5. Review, don't rewrite

- When Joshua shares code he wrote, review for: correctness against the
  validation rules, correct layer placement, and consistency with the model
  fields/enum values — don't silently rewrite it. Point out the issue and
  let him fix it, unless he explicitly asks for a fix.

## 6. Model

- Joshua may switch the active model via `/model` on his end at any point;
  Claude cannot invoke that command on his behalf — say so if asked.
