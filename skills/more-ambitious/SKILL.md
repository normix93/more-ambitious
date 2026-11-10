---
name: more-ambitious
description: Rewrites a request, prompt or project so it aims higher along four axes (speed, altitude, depth, range), then offers to do the ambitious version. Use when the user asks to raise the bar, aim higher, be more ambitious, go bigger or deeper, or make a prompt more ambitious, or before starting substantial work that may be under-asking.
license: MIT
---

# More ambitious

Based on the framework in Felix Rieseberg's essay
"How to be more ambitious: A tutorial for humans with models" (October 2026):
https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/

The premise: with a capable model, the bottleneck is often how high the person aims,
not what the model can do. This skill takes a request (a task, a prompt, a project)
and pushes it along four axes, then offers to carry out the stronger version.

## When to use

- "Make this more ambitious", "raise the bar", "how could I aim higher?", "go deeper".
- Before a substantial piece of work, to check whether we are asking for too little.
- To rewrite a prompt into a deeper or higher-level version.

Do not use it for quick lookups, small edits, or when the person has clearly scoped
the work and just wants it done.

## Procedure

1. **Understand the starting request**: what the task is, who uses the result, and
   what happens after it is delivered. If the request is too vague to elevate
   (no task, no audience), ask one short question first.
2. **Run it through the four axes** below. You do not need all four: pick the ones
   that actually change the outcome. If the elevated version is only "longer" or
   "more pages", you picked the wrong axis.
3. **Return**:
   - the rewritten request, ready to paste as a prompt (in a code block);
   - what changed and on which axis, in a few lines;
   - what is needed for the ambitious version to be feasible (raw data, tools,
     access, permissions);
   - how the result will be checked by a judge outside the model.
4. If the person agrees, **do the ambitious version** instead of the original,
   rather than only describing it.

Write the rewritten prompt in the language the person asks for; default to the
language of the conversation.

## The four axes

### 1. Speed
The same work in less time. It is the most obvious axis: mention it only when it is
the only real gain.

### 2. Altitude: ask for the outcome, not the task
Ask: what is the goal behind the goal? Climb as far as it makes sense:
- level 1: analyse what happened and why;
- level 2: identify the most urgent decisions and develop options with trade-offs;
- level 3: design a better process than the one that produces the task, show on
  historical data that it would have worked better, and run it alongside the old one.

Useful signal: if the work would normally need a meeting to discuss it, it can
probably be asked for at a higher level.
Altitude often means changing the workflow: giving the model direct access to the
data, logs and environments where it can check its own work.
Limits: works best with clear end goals; less well with open creative work. Vague
goals ("make money") are not enough.

### 3. Depth: do it the way the best in the field would
Not a bigger task, but the task done the way a top practitioner would do it, to the
point where an expert learns something. Techniques:
- **Professional tools**: if the language sounds expert but the methods are amateur
  (markdown tables, eyeballed estimates), switch to real tools: databases,
  statistical models, simulations, executable code.
- **Unreasonable goals framed as reasonable**: instead of halving a time, aim for an
  order of magnitude. If it seems impossible, keep looking for a path before giving up.
- **Test the assumptions**: go back to raw data and adversarially check what is being
  taken for granted.
- **Produce new knowledge**: look for blind spots and signals no one has noticed yet,
  and check them on data the model has not seen.
- **Outside judge**: the model does not grade itself. Use external verification,
  ideally an executable check with fast feedback (tests, benchmarks, held-out data,
  primary sources).

Before rewriting a prompt for depth, answer four questions:
1. What would a top professional in this field do that the request does not ask for?
2. What is the rawest material they would start from, instead of pre-processed inputs?
3. Which specific methods and tools would they use?
4. What, outside the two of us, would prove the result is right?
Then rewrite the prompt accordingly.

### 4. Range: more disciplines than used to be affordable
- **Verbs instead of nouns**: describe the work by what it must do, not by the object
  it produces. A deck is not "a deck": it is getting busy people to believe a story of
  cause and effect and decide quickly. The verbs point to the disciplines that can help.
- **Assemble the team**: list the useful disciplines, including a red team (whoever
  would try to tear the work apart). With subagents they can actually work in parallel.
- **No role-play**: ask for what that discipline *does* (its techniques and tools),
  not for its voice. Role-play changes the jargon without improving the method.
- Look for tools from fields other than the starting one: that is often where the
  most surprising ideas come from.

## Prerequisites to flag

Ambition needs tools and access, not just better prompts: a computer where software
can be installed, the relevant data (connectors, files, logs), and a way to verify.
If any are missing, say so plainly and suggest how to get them.

## Caveats

- Model capabilities are uneven: remarkable in some directions, weak in others. If an
  axis does not hold up for this task, say so.
- Specific, hard goals work better than "do your best", but they need a way to
  measure the result.
- Ambition raises the task, never the risk: it is not a licence to skip safety
  checks, approvals or confirmation before external actions.
- Give yourself and the person permission to fail: an ambitious attempt that partly
  fails is often worth more than a cautious one that succeeds.

## Example

Starting request: "Make a slide deck for our quarterly business review."

Elevated (altitude + depth + range):

```text
The QBR exists so leadership spots problems early and reallocates resources.
Using the raw sales, support and product-usage data for the last 8 quarters:
1. Identify the 3 decisions leadership most urgently needs to make this quarter,
   with options and trade-offs for each, backed by statistical analysis (not tables
   of eyeballed numbers).
2. Propose a lighter recurring process that would have flagged last year's two
   biggest misses at least a month earlier; show this on the historical data.
3. Before finalising, have a red-team pass try to refute each claim from the raw data.
Deliver a short deck built around the decisions, plus the analysis notebook so the
numbers can be re-run.
```

What changed: altitude (decisions and a better process instead of slides), depth
(raw data, real statistics, backtest), range (red team, verbs: "spot problems early"
instead of "make slides"). Needed: access to the raw data. Judge: the backtest on
historical quarters and a re-runnable notebook.
