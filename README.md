# more-ambitious

A skill for Claude that takes a request you're about to give it (a task, a prompt or a
project) and rewrites it to aim higher. Then it offers to do the stronger version.

It uses the four types of ambition from Felix Rieseberg's essay
[How to be more ambitious: A tutorial for humans with models](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/):

| Axis | The question it asks |
|---|---|
| **Speed** | Can the same work be done faster? (Mentioned only when it's the only real gain.) |
| **Altitude** | What's the goal behind the goal? Ask for the outcome, not the task. |
| **Depth** | How would the best person in the field do this, using which raw data, tools and checks? |
| **Range** | Which other disciplines (including a red team) could help? |

The skill picks only the axes that change the result. You get back:

1. the rewritten request, ready to paste;
2. what changed and on which axis;
3. what's needed for the ambitious version to work (data, tools, access);
4. how to check the result with something other than the model grading itself.

## Example

> **You:** /more-ambitious Make a slide deck for our quarterly business review.

**Without the skill**, you get a deck.

**With the skill**, you get a request like this: *"Using the raw data for the last 8
quarters, find the 3 decisions leadership most urgently needs to make, with options and
trade-offs backed by real statistics. Propose a lighter process that would have flagged
last year's two biggest misses a month earlier, and show it on the historical data.
Have a red team try to refute each claim before you finish."* You also get a note on
the data access it needs and how the numbers will be checked.

More example prompts that trigger it:

- "Raise the bar on this: I want to write a blog post about our migration."
- "Make this prompt more ambitious: *summarise these customer interviews*."
- "Before I start, am I aiming too low with this research plan?"

## Install

### Claude Code (plugin marketplace)

```
/plugin marketplace add YOUR_GITHUB_USER/more-ambitious
/plugin install more-ambitious@more-ambitious
```

### Claude Code (manual)

Copy `skills/more-ambitious/` into `~/.claude/skills/` (all projects) or
`.claude/skills/` (a single project).

### Claude apps (claude.ai, desktop)

Download `more-ambitious.zip` from the
[latest release](https://github.com/YOUR_GITHUB_USER/more-ambitious/releases) and upload
it in the skills section of Settings.

### Other agents

The skill follows the open [Agent Skills](https://agentskills.io) format (`SKILL.md`
with YAML frontmatter), so any agent that supports the format can load it.

## Repository layout

```
.claude-plugin/        plugin.json + marketplace.json (Claude Code plugin)
skills/more-ambitious/ the skill itself
evals/                 trigger test cases (should / shouldn't activate)
scripts/validate.py    structure and frontmatter checks, run in CI
```

## Contributing

Issues and pull requests are welcome, especially real requests where the skill
triggered when it shouldn't have, or didn't when it should. Add them to
`evals/triggers.json`.

## Credits and license

The framework is Felix Rieseberg's. This skill is an independent adaptation and isn't
affiliated with or endorsed by him or by Anthropic. Read the
[original essay](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/).

The skill text is released under the [MIT License](LICENSE).
