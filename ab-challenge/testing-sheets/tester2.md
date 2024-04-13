# AB-Challenge: Prompt-Basic-1

First example of this
- prompt: default prompt some extra to get solution tag to work.
- questions = instances[0:10][0]

#### meta
- max_tokens: 4000
#### question
Your job is to take the input string and fully compute it, step by step. Finish your answer by adding the final result in the solution tag.

A::B is a system with 4 tokens: `A#`, `#A`, `B#` and `#B`.

An A::B program is a sequence of tokens. Example:

    B# A# #B #A B#

To *compute* a program, we must rewrite neighbor tokens, using the rules:

    A# #A ... becomes ... nothing
    A# #B ... becomes ... #B A#
    B# #A ... becomes ... #A B#
    B# #B ... becomes ... nothing

When a program can no longer be computer it always ends with format: <solution>FINAL_SOLUTION_STRING</solution>

In other words, whenever two neighbor tokens have their '#' facing each-other,
they must be rewritten according to the corresponding rule. For example, the
first example shown here is computed as:

    B# A# #B #A B# =
    B# #B A# #A B# =
    A# #A B# =
    B#
    <solution>B#</solution>

The steps were:
1. We replaced `A# #B` by `#B A#`.
2. We replaced `B# #B` by nothing.
3. We replaced `A# #A` by nothing.
The final result was just `B#`.


    <solution>B#</solution>

Now, consider the following program:

## Q-1
#### question
#A #B #A #A #B B# B# B# B# A# B# A# 

Fully compute it, step by step. Finish your answer by adding the final result in the solution tag.
#### answer
<solution>#A #B #A #A #B B# B# B# B# A# B# A#</solution>

## Q-2
#### question
#B #B #B #A #B A# B# A# A# #A A# B# 

Fully compute it, step by step. Finish your answer by adding the final result in the solution tag.
#### answer
<solution>#B #B #B #A #B A# B# A# A# B#</solution>