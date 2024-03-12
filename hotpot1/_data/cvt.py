import json
import sys

try: input_fn = sys.argv[1]
except: raise ValueError('Provide input filename as first argument')

# print(f'input_fn: {input_fn}')

with open(input_fn, 'r') as f:
    data = json.load(f)

# print(json.dumps(data, indent=4))
    
s_output = ''
for i, item in enumerate(data):
    s_output += f'''## Q-{i+1}\n'''
    s_output += f'''#### question\n{item.get('question').strip()}<EVAL-ENDCHAR>\n'''
    s_output += f'''#### answer\n{item.get('answer').strip()}<EVAL-ENDCHAR>\n'''
    s_output += '\n'

# deal with unicode chars?
s_output = s_output.encode('utf-8') #.decode('utf-8')

sys.stdout.buffer.write(s_output)
# print(s_output)

