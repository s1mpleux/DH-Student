# Day 1 Exercise: Agile Research Stories (Software Engineering Focus)

## Project Context
This document contains 5 research stories for a small study on **software engineering team productivity and code quality practices in student projects**.

---

## Research Stories (RS)

### RS1: Static code analysis impact
**Priority:** High  
**Sprint:** Sprint 1

Within the field of software quality assurance, investigate the impact of integrating static code analysis tools (e.g., linters, formatters) into student projects, to understand whether automated checks reduce the number of critical bugs introduced during development.

Implemented according to criteria:
- Compare bug counts (compiler errors, runtime exceptions) in projects with vs. without static analysis
- Track the number of late-stage fixes required in both groups
- Measure student-reported time spent debugging trivial issues

---

### RS2: Git branching strategy adoption
**Priority:** High  
**Sprint:** Sprint 1

Within the field of collaborative software development, experiment with using feature-branch workflows (vs. direct commits to main) in student team projects, to corroborate the assumption that structured branching reduces merge conflicts.

Implemented according to criteria:
- Count merge conflicts per sprint in both workflow types
- Measure time spent resolving conflicts in both groups
- Survey students on perceived workflow clarity and frustration levels

---

### RS3: Test-driven development (TDD) in student projects
**Priority:** Medium  
**Sprint:** Sprint 2

Within the field of agile software development, explore the adoption of test-driven development practices in student backend projects, to understand whether writing tests before code improves overall code maintainability.

Implemented according to criteria:
- Measure test coverage of projects using TDD vs. traditional development
- Count the number of code rewrites/refactors needed during the project
- Evaluate code readability scores from peer reviews

---

### RS4: Code review effectiveness
**Priority:** Medium  
**Sprint:** Sprint 2

Within the field of software engineering collaboration, investigate the impact of mandatory peer code reviews on student projects, to understand whether early feedback reduces technical debt in the final submission.

Implemented according to criteria:
- Track the number of unresolved technical debt items before and after reviews
- Count the number of critical design flaws caught during review
- Measure the time saved on post-submission bug fixes

---

### RS5: Documentation practices in open-source student projects
**Priority:** Low  
**Sprint:** Sprint 3

Within the field of open-source software engineering, experiment with different README and inline documentation styles in public student repositories, to corroborate the theory that clear documentation increases peer collaboration and contributions.

Implemented according to criteria:
- Compare the number of external pull requests/issues between well-documented vs. poorly documented repos
- Measure time taken by peers to understand and contribute to the project
- Survey contributors on perceived clarity of the project setup instructions

---

## Sprint Planning
| Sprint | Stories | Focus |
|--------|---------|-------|
| Sprint 1 | RS1, RS2 | Core quality & collaboration workflows (static analysis + Git branching) |
| Sprint 2 | RS3, RS4 | Quality practices (TDD + peer review) |
| Sprint 3 | RS5 | Open-source collaboration & documentation |
