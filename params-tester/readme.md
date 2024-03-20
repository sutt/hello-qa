# Params Tester

**Purpose:** We contruct sheets to test the loading inference parameters in a variety of ways.

We use the prompt: `Q: Generate an esoteric french phrase. (Then explain why it would be considered esoteric) A:` to allow the model maximum room for completion to deviate, in cases when that's the desired behavior.

### Summary

There are three main **inference parameters** we are able to control in lime currently.
- max_tokens: 10 vs 40 vs 100.
- temperature: 0.0 vs 1.0
    - note: 0.0 will override the seed making it irrevelant.
- seed: None vs 1 vs 2

We'll adjust these parameters, examine the output , to verify they are being set properly.

There are three main **sources** we are able to control in lime currently. In order of precedence:
- question
- sheet
- config

So we have different directories so we can have different config on/off for these input-sheets. Note if these parameters are not set at any-level, the model will use the default values in python package:

```python
class LocalParams(ConfigLoader):
    max_tokens = 100
    temperature = 0.0
    seed = None
```

We'll run the same input-sheets with two separate inference services:
- `OpenAIModelObj`: gpt-3.5-turbo
- `LocalModelObj`: mistral_hf_7b

Currently, `CPLModelObj` does not support passing these parameters.

### Running Notes

- Need to execute lime within the `config/` directory to get the config level settings to apply.
- The `seed` parameter with `OpenAIModelObj` will not always work as expected, but sometimes it does. This behavior is not understood at the present by the author.

### Repository Outline

- non-config/
    - question-level-1.md: individual questions have params, sheet does not.
    - sheet-level-1.md: sheet has params, individual questions do not.
    - no-level-1.md: neither sheet nor questions have params, and since there are no config level settings, the default values will be used.
    - we set the params in input-sheets like so:
   
    ```markdown
    #### meta
    - max_tokens: 10
    - temperature: 1.0
    - seed: 2
    ```

- config/
    - config-level-1.md:
    - .lime/config.yaml:

    ```yaml
    LocalParams:
    temperature: 1.0
    max_tokens: 40
    seed: null
    ```

- _aggs/
    - multiple `output-<sheet-name>-<model-name>-<runid>.json`
    -
- _reports/
    - completions-<description>.md

### Results

---

#### Check `max_tokens`

Experiment on gpt-3.5-turbo with `max_tokens` set to 10 and 40.
- `118d`: 10 tokens
- `f806`: 40 tokens

```bash
lime eval sheet-level-1.md
```

We see that the completions is longer.

| name   | run_id   | completion                                                                                                                                                                                       |
|:-------|:---------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Q-1    | 118d     | "Le silence des �toiles murmure �                                                                                                                                                                |
| Q-1    | f806     | "Les ombres dansent avec la lune et murmurent des secrets<br>anciens."  This phrase is considered esoteric because it<br>uses poetic language and metaphorical imagery, reflecting a<br>deep and |
| Q-2    | 118d     | "Les �toiles chantent la symphon                                                                                                                                                                 |
| Q-2    | f806     | "Les cicatrices de l'�me sont plus profondes que celles du<br>corps."  This phrase translates to "The scars of the soul<br>are deeper than those of the body." This                              |

---

#### Check `seed` on gpt-3.5-turbo

Experiment on gpt-3.5-turbo with `seed` set to 1 or 2.

- SheetParams:
    - max_tokens: 40
    - temperature: 1.0
- Question:
    - seed=1 (Q-1)
    - seed=2 (Q-2)

```bash
lime eval question-level-1.md
```

**Findings:** We see that completions vary across question, but not between runs so seed is working.


| name   | run_id   | completion                                                                                                                                                                                                             |
|:-------|:---------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Q-1    | 6529     | "La clairvoyance de l'esprit transcende la r�alit�<br>tangible."  This phrase is considered esoteric because it<br>delves into the concept of psychic abilities and the mind's<br>ability to perceive                  |
| Q-1    | 781b     | "La clairvoyance de l'esprit transcende la r�alit�<br>tangible."  This phrase translates to "The clairvoyance of<br>the mind transcends tangible reality." It can be considered<br>es                                  |
| Q-1    | d395     | "La clairvoyance de l'esprit transcende la r�alit�<br>tangible."  This phrase translates to "The clairvoyance of<br>the mind transcends tangible reality." It can be considered<br>es                                  |
| Q-2    | 6529     | "Le temps est un illusion, la r�alit� est un r�ve �ph�m�re."<br>This phrase is considered esoteric because it delves into<br>philosophical concepts such as the nature of time,                                        |
| Q-2    | 781b     | "Le temps est un �tranger qui voyage seul dans l'infini de<br>l'univers."  This phrase is considered esoteric because it<br>uses abstract language and philosophical concepts that may<br>not be easily                |
| Q-2    | d395     | "Le temps est un �tranger qui voyage seul."  This phrase is<br>considered esoteric because it's a metaphorical statement<br>about time being a solitary traveler, which may not be<br>easily understood or appreciated |



---

#### Check `seed` on mistral_hf_7b

Experiment on local model (mistral_hf_7b) with `seed` set to 1 or 2.

- SheetParams:
    - max_tokens: 40
    - temperature: 1.0
- Question:
    - seed=1 (Q-1)
    - seed=2 (Q-2)

```bash
lime eval question-level-1.md -m mistral_hf_7b
```

| name   | run_id   | completion                                                                                                                                |
|:-------|:---------|:------------------------------------------------------------------------------------------------------------------------------------------|
| Q-1    | 26d3     | Phrase: "Le poireau bavard r�v�le le secret du verjus<br>enroul� dans l'obscurit� du jardin."  Translation:                               |
| Q-1    | db9e     | Phrase: "Le poireau bavard r�v�le le secret du verjus<br>enroul� dans l'obscurit� du jardin."  Translation:                               |
| Q-2    | 26d3     | Phr�s� magique lune de miel enchant�e dans le labyrinthe du<br>temps :  This phrase means "magical phrase, moon of honeyed<br>enchantment |
| Q-2    | db9e     | Phr�s� magique lune de miel enchant�e dans le labyrinthe du<br>temps :  This phrase means "magical phrase, moon of honeyed<br>enchantment |

---

#### Check `temperature=0` overrides `seed` variation (on mistral_hf_7b)

Experiment on with setting temperature to 0.0 (mistral_hf_7b) with `seed` set to 1 or 2.

- SheetParams:
    - max_tokens: 10
    - temperature: 0.0
- Question:
    - seed=1 (Q-1)
    - seed=2 (Q-2)

```bash
lime eval question-level-1.md -m mistral_hf_7b
```
### Questions/IDs: full Completions 

| name   | run_id   | completion               |
|:-------|:---------|:-------------------------|
| Q-1    | 71ad     | Phrase : "Le poireau br� |
| Q-1    | ac4c     | Phrase : "Le poireau br� |
| Q-2    | 71ad     | Phrase : "Le poireau br� |
| Q-2    | ac4c     | Phrase : "Le poireau br� |


---

#### Test config-level

Experiment with a config set:

```yaml
LocalParams:
  temperature: 1.0
  max_tokens: 10
```

And sheet level params set as:

```markdown
#### meta
- seed: 1
```

```bash
lime eval config-level-1.md  #(inside config/)
```

**Findings:** The config level settings of max_tokens=10 is being applied, and since the seed is set on the sheet, it is being applied because we don't see variation across runs.


| name   | run_id   | completion                   |
|:-------|:---------|:-----------------------------|
| Q-1    | 02b4     | "La clairvoyance de l'esprit |
| Q-2    | 02b4     | "La clairvoyance de l'esprit |


---

#### Check no parameters set, default values used

No config, sheet, or question level parameters set.

**Findings:** The default value of max_tokens=100 is being used. We're getting the same output because the default temperature is set to 0.0, and the seed is set to None.


| name   | run_id   | completion                                                                                                                                                                                                                                                                                                                     |
|:-------|:---------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Q-1    | 8291     | "Les �toiles dansent avec les murmures du vent"  This phrase<br>could be considered esoteric because it combines elements of<br>nature (stars and wind) with a sense of movement and<br>mysticism. It evokes a sense of poetic imagery and symbolism<br>that may not be easily understood by those unfamiliar with<br>Frenc... |
| Q-1    | fce3     | "Les �toiles dansent avec les murmures du vent"  This phrase<br>could be considered esoteric because it combines elements of<br>nature (stars and wind) with a sense of mysticism and poetic<br>imagery. It conveys a sense of interconnectedness between<br>the celestial and earthly realms, which may not be easily<br>u... |
| Q-2    | 8291     | "Les �toiles dansent avec les murmures du vent"  This phrase<br>could be considered esoteric because it combines elements of<br>nature (stars and wind) with a sense of mysticism and poetic<br>imagery. It conveys a sense of interconnectedness between<br>the celestial and earthly realms, which may not be easily<br>u... |
| Q-2    | fce3     | "Les �toiles dansent avec les murmures du vent"  This phrase<br>could be considered esoteric because it combines elements of<br>nature (stars and wind) with a sense of mysticism and poetic<br>imagery. It may not have a clear or easily understandable<br>meaning to those who are not familiar with esoteric or<br>phil... |


