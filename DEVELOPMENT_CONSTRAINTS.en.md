**🌐 Language：** [中文](DEVELOPMENT_CONSTRAINTS.md) | **English** | [日本語](DEVELOPMENT_CONSTRAINTS.ja.md) | [Español](DEVELOPMENT_CONSTRAINTS.es.md) | [Français](DEVELOPMENT_CONSTRAINTS.fr.md) | [Deutsch](DEVELOPMENT_CONSTRAINTS.de.md) | [한국어](DEVELOPMENT_CONSTRAINTS.ko.md) | [Русский](DEVELOPMENT_CONSTRAINTS.ru.md)

---

# Development Environment Constraints & Honest Disclosure Template

> Copy this template to your project, check and fill in according to actual conditions. This document explains the actual development conditions and responsibility boundaries of this repository.

## I. Development Environment (Check as applicable)

- [ ] Has local IDE / SDK, can compile locally
- [ ] Has local diff tools, can review line by line
- [ ] Can run lint / unit tests
- [ ] Follows standard PR flow (fork → PR → review)
- [ ] **Relies solely on cloud CI compilation (no local toolchain)**
- [ ] **Develops solely on mobile / smartwatch**
- [ ] **Direct push to master (no PR flow)**

> Unchecked items mean **physically impossible to execute in this repository**, not "ignored".

## II. Actually Implemented Mechanisms (Check what was done)

### Disclosure
- [ ] Provides `AI_DISCLOSURE.md` explaining AI involvement and percentage
- [ ] Links to this file at the top of README
- [ ] Commit message tagged with `[ai-assisted]`

### High-Risk Features
- [ ] High-risk features disabled by default (at code level, not just docs)
- [ ] Separate warning section for high-risk features (see `SECURITY.md` or equivalent)
- [ ] Explicit second confirmation required before using high-risk features

### Gates
- [ ] **Release only after CI compilation passes** (the only automated gate in this project)
- [ ] Release artifacts have version numbers and tags
- [ ] `CHANGELOG.md` records every change

### Testing
- [ ] **On-device testing** (real physical devices)
- [ ] **Emulator testing** (when no physical devices are available)
- [ ] **Untested** (see honest disclosure below)

> Unchecked items mean **this repository has no conditions to do it**, not "forgot to do it".

## III. Honest Disclosure

**The following situations must be stated truthfully, no sugar-coating:**

- If this repository **has not done any on-device or emulator testing**, state it clearly here:
  > "The code in this repository has not been tested on real devices. Passing CI compilation only means syntax and dependencies are correct, not that the features work. Please evaluate the risks yourself before use."

- If a module is **sensitive but unverified**, mark it as `⚠️ Unverified` in the list below.

- If a feature is **enabled by default** (violating the "high-risk off by default" principle), state the reason clearly.

## IV. Sensitive Module List (Fill in according to actual conditions)

| Module | Verification Status |
|---|---|
| `{{your auth module}}` | ✅ On-device / ⚠️ CI only / ❌ Unverified |
| `{{your filesystem module}}` | ✅ On-device / ⚠️ CI only / ❌ Unverified |
| `{{your protocol parsing module}}` | ✅ On-device / ⚠️ CI only / ❌ Unverified |
| `{{your CI/CD release script}}` | ✅ On-device / ⚠️ CI only / ❌ Unverified |

> Modules marked `❌ Unverified` **are not necessarily unpublishable**, but please evaluate the risks before use.

## V. We Admit This Is Not Perfect

Formal PR processes, line-by-line code reviews, and local static analysis **may all be absent** in some repositories.

We bear **substantive responsibility** through "**Disclosure + Gates (what we can do) + Off by default**", rather than pretending to fulfill all **formal responsibilities**.

This is a choice under constraints, not a rejection of standards.
