# Hotpot Eval 1

This is based off the official HotpotQA evaluation dataset, and inspired by the DSPy tutorial:

This features an ability to use a CustomPipeLine "CPL" in the [`_app`](./_app/) .To use this you'll need to install the requirements which are in the `requirements.txt` file (which is just `dspy-ai` in this case). and also install `lime` in that environment.

The raw data in json form is in the [`_data`](./_data/) folder. Using the [`cvt.py`](./_data/cvt.py) script you can convert the json to a lime sheet, e.g.:

```bash
python cvt.py hotpot-dev.json > dev.md
```

Then add a sheet header name to the top of the file. You can also filter which questions to bring in. There are 20 quesrtions in train and 50 question in dev. These were ultimately generated from the following code:

```python
from dspy.datasets import HotPotQA
import json

dataset = HotPotQA(train_seed=1, train_size=20, eval_seed=2023, dev_size=50, test_size=0)

trainset = [x.with_inputs('question') for x in dataset.train]
devset = [x.with_inputs('question') for x in dataset.dev]

# needed to turn sets into lists
def serialize(d):
    out = {}
    for k, v in d.items():
        if isinstance(v, set): out[k] = list(v)
        else:out[k] = v
    return out
json.dump([e.toDict() for e in trainset], open('data/trainset.json', 'w'), indent=2)
json.dump([serialize(e.toDict()) for e in devset], open('data/devset.json', 'w'), indent=2)

```