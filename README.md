# agent-desk-demo

This repository is a sample project for [agent-desk](https://github.com/erjand/agent-desk), which runs headless Claude
Code agents on a project's issues. Its README's screenshots show this project's board, and its quickstart uses this
repository to try agent-desk on a project with nothing at stake.

The project itself is `tinytext`, a few small functions for everyday text:

```python
>>> from tinytext import title_case, word_count, reverse_words, strip_accents
>>> title_case("the quick brown fox")
'The Quick Brown Fox'
>>> word_count("one two three")
3
>>> reverse_words("one two three")
'three two one'
>>> strip_accents("café crème")
'cafe creme'
```

## Test

`tinytext` needs only Python 3.10 or newer. Run its tests from the repository's root:

```bash
python3 -m unittest
```

## Try agent-desk on it

Install agent-desk as its README describes, then clone this repository and set it up:

```bash
git clone https://github.com/erjand/agent-desk-demo
cd agent-desk-demo
agent-desk install
agent-desk doctor
```

The repository's `.agent-desk.json` already sets the test command. Issues live in agent-desk's local store on your
machine, so a fresh clone starts with none: file one with `agent-desk issue create`, or with
`/agent-desk:create-issue` in a Claude Code session in the checkout, and label it `agent-ready` to send an agent.

## License

MIT. See [LICENSE](LICENSE).
