import json

fn = 'output-data.json'
prompt_suffix = None
prompt_suffix = '''\n\nFully compute it, step by step.'''
b_solution_tag = True

with open(fn, 'r') as f:
    data = json.load(f)
out = ''
for i, row in enumerate(data):
    out += '## Q-' + str(i + 1) + '\n'
    out += '#### question\n'
    out += row['problem']
    if prompt_suffix:
        out += prompt_suffix
    out += '\n'
    out += '#### answer\n'
    if b_solution_tag:
        out += f'<solution>{row["solution"].strip()}</solution>'
    else:
        out += row['solution']
    out += '\n\n'

print(out)