# Hello-QA Data Repository

These are demonstration datasets for [lime](https://github.com/sutt/lime) commands that demonstrate different functionalities of the lime command line eval tool.

### List of directories: contents and purpose

- **[`ab-challenge`](./ab-challenge):** Inspired by a viral $10K twitter bet, a challenge to provide a sufficient prompt that will simulate a state machine via completion. See README for more details.
  - `_autogen` - generate a template sheet of example
  - `main-sheets/` - main directory for candidate sheets
    - current sheet is 1 problem from each of difficulties 1-10.
  - `testing-sheets/` - small step testing sheets.

- **[`theory-of-mind-1`](./theory-of-mind-1):** Contrived word problems designed to test a model's ability to reason about the beliefs of other agents.

- **[`challenge-1`](./challenge-1):** A collection of one-off challenging questions sourced from social media, etc.

- **[`hotpot1`](./hotpot1):** Using a sampling of the datasets from the [HotpotQA](https://hotpotqa.github.io/) dataset to:
  - utilize contents of [`_app`](./hotpot1/_app) to demonstrate how to use run a cpl server on a DSPy based pipeline app. See the [README](./hotpot1/_app/readme.md) for more details.
  - how to use `--discrepancies` agg report to distinguish between models that got a question where the other got it wrong, e.g. GPT-3.5 vs DSPy+RAG.
  - small converter in ['_data'](./hotpot1/_data) to convert the HotpotQA dataset to a lime dataset.

- [`params-tester`](./params-tester/): testing that inference parameters load properly from multiple sources:
   - parameters:
     - temperature
     - seed
     - max_tokens
   - sources:
     - config
     - sheet
     - question