# Victor's AB Challenge Evaluation

**TL/DR:** This is a challenge to develop the best system prompt to solve a state-machine emulation task

### Background
This was an online challenge initiated by [Victor Taelin](https://twitter.com/VictorTaelin/status/1776096481704804789) on April 4, 2024 where he offered $10K to anyone who could prompt a model to solve a TuringMachine-like state machine to manipulate tokens, to an accuracy of 90% or more.

Despite Victor's initial skepticisim, the challenge was [solved](https://twitter.com/VictorTaelin/status/1777049193489572064) within 48 hours by [futuristfrog](https://twitter.com/futuristfrog/status/1778109834509832462).

### Repo Resources:

This is how the repo is organized

 - **`_autogen`:** scripts to automatically build problem and solution pairs and create a lime sheet.
    - run `node app.js > output-data.json` to generate problem/solution pairs in json format (taken from Victor's eval repo)
    - run `python gen_sheet.py > template.md` to output the question portion
    - concatenate `header.md` with `template.md` to generate the full lime sheet.
- **`_outputs`:** all output .json files moved here
- **`_reports`:** outputs from agg moved here.
- **`testing-sheets`:** small sheets for experimenting on getting one aspect of the task correct, e.g. enclosing the final portion in a `<solution/>` tag
- **`main-sheets`:** main sheets for evaluating model perf on the main task:
  - `input-basic-prompt-1.md`: basic prompt with questions 1-10; does not work

### Significance

This challenge is significant because it demonstrates the power of prompt engineering to navigate a certain type of task purely in the LLM evaluation - where there are multiple relatively simple steps, but where the results builds on previous steps making the reliability of each step of importance.

At a high-level you could argue that this is a planning and delegation task, rather than a cognitive or creative task. With GPTs as next token predictors, the challenge is: can the model stay on the right track to enter the spirit of a state machine and then re-emerge with the correct output and final processing.


##### More background information

The challenge was formalized [here](https://gist.github.com/VictorTaelin/8ec1d8a0a3c87af31c25224a1f7e31ec) with rules:
 - Prompt contains xml tag `<problem/>`, output must contain `<solution/>`
 - Prompt size < 8K tokens, Context size < 32K tokens
 - 12-token instance of the A::B problem
 - All LLM's are allowed including GPT-4 and Claude-3-Opus, and open-source models. Fine-tuning is not allowed.


### External Resources:
 - Compeition Thread, with links to various submissions:
  https://gist.github.com/VictorTaelin/8ec1d8a0a3c87af31c25224a1f7e31ec
 - Victor Taelin's Eval Repo:
  https://github.com/VictorTaelin/ab_challenge_eval
 - Alternative Prompt:
  https://gist.github.com/thakkarparth007/f727eceedaaab7c14078c511370bf440
 - @kenshin9000_'s starting prompt:
  https://platform.openai.com/playground/p/Oz4K4cIMJWJlxc1l9aFEwYJD?mode=chat&model=gpt-4-0125-preview