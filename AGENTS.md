# agent-desk-demo

`tinytext` is a small Python package of text functions, kept as a sample project for
[agent-desk](https://github.com/erjand/agent-desk). `README.md` shows what each function does.

## Agent Desk

agent-desk, set up by `.agent-desk.json`, runs this repository's issues. The `work-issue` and `create-issue` skills
read this section for what is particular to this project:

- **Tracker.** Issues and reviews live in agent-desk's local store. Read and write them with `agent-desk issue`
  (`view`, `list`, `create`, `comment`, `edit`, `close`) and `agent-desk review` (`create`, `view`, `list`,
  `comment`, `edit`, `checks`, `ready`), and never with `gh issue`, `gh pr`, or `gh api`.
- **Tests.** `python3 -m unittest` runs the tests in `tests/`. Add a test class beside the others in
  `tests/test_tinytext.py` for each function you add or change.
- **Dependencies.** The package uses only the Python standard library. Add no third-party dependency.
- **Visual changes.** The project has no interface to capture.
- **Design docs.** `README.md` lists each function with an example; add new functions to it. File an idea without a
  concrete outcome as an issue labelled `idea`.
