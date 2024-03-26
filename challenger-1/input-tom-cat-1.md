# Theory-of-Mind: Cat Story

Attribution: Michal Kosinski, "Theory of Mind May Have Spontaneously Emerged in Large Language Models" (https://arxiv.org/abs/2302.02083)

This looks at theory of mind, especially around if John would know where to look for the cat after Mark moves it, if John is not present. Thus question `John-5` is the crux of the question sheet, and subsequent question are possibly easier.

Note: in the original paper it used logprobs for answers.

Note: these should only be two choices for output: "basket" and "box"

Full Story:
John takes the cat and puts it in the basket.
Mark takes the cat out of the basket and puts it in the box.
John takes the cat out of the box and puts it in the basket.
He leaves the room and goes to school.
While John is away, Mark takes the cat out of the basket and puts it in the box.
Mark leaves the room and goes to work.
John comes back from school and enters the room.
He doesn't know what happend in the room when he was away.

Question Types:
The cat jumps out of the ___
When John comes back home, he will look for the cat in the ___ 

#### meta
- max_tokens: 10


#### question
In the following story, fill in the blank ("___") with the correct answer. Say the word and nothing else.

In the room there are John, Mark, a cat, a box, and a basket.
<EVAL-ENDCHAR>

## Cat-1
#### question
John takes the cat and puts it in the basket.

The cat jumps out of the ___ <EVAL-ENDCHAR>
#### answer
basket

## John-1
#### question
John takes the cat and puts it in the box.

When John comes back home, he will look for the cat in the ___ <EVAL-ENDCHAR>
#### answer
box

## Cat-2
#### question
John takes the cat and puts it in the basket.
Mark takes the cat out of the basket and puts it in the box.

The cat jumps out of the ___ <EVAL-ENDCHAR>
#### answer
box

## John-2
#### question
John takes the cat and puts it in the basket.
Mark takes the cat out of the basket and puts it in the box.

When John comes back home, he will look for the cat in the ___ <EVAL-ENDCHAR>
#### answer
box

## Cat-3
#### question
John takes the cat and puts it in the basket.
Mark takes the cat out of the basket and puts it in the box.
John takes the cat out of the box and puts it in the basket.

The cat jumps out of the ___ <EVAL-ENDCHAR>
#### answer
basket

## John-3
#### question
John takes the cat and puts it in the basket.
Mark takes the cat out of the basket and puts it in the box.
John takes the cat out of the box and puts it in the basket.

When John comes back home, he will look for the cat in the ___ <EVAL-ENDCHAR>
#### answer
basket

## Cat-4
#### question
John takes the cat and puts it in the basket.
Mark takes the cat out of the basket and puts it in the box.
John takes the cat out of the box and puts it in the basket.
He leaves the room and goes to school.

The cat jumps out of the ___ <EVAL-ENDCHAR>
#### answer
basket

## John-4
#### question
John takes the cat and puts it in the basket.
Mark takes the cat out of the basket and puts it in the box.
John takes the cat out of the box and puts it in the basket.
He leaves the room and goes to school.

When John comes back home, he will look for the cat in the ___ <EVAL-ENDCHAR>
#### answer
basket

## Cat-5
#### question
John takes the cat and puts it in the basket.
Mark takes the cat out of the basket and puts it in the box.
John takes the cat out of the box and puts it in the basket.
He leaves the room and goes to school.
While John is away, Mark takes the cat out of the basket and puts it in the box.

The cat jumps out of the ___ <EVAL-ENDCHAR>
#### answer
box

## John-5
#### question
John takes the cat and puts it in the basket.
Mark takes the cat out of the basket and puts it in the box.
John takes the cat out of the box and puts it in the basket.
He leaves the room and goes to school.
While John is away, Mark takes the cat out of the basket and puts it in the box.

When John comes back home, he will look for the cat in the ___ <EVAL-ENDCHAR>
#### answer
basket

## Cat-6
#### question
John takes the cat and puts it in the basket.
Mark takes the cat out of the basket and puts it in the box.
John takes the cat out of the box and puts it in the basket.
He leaves the room and goes to school.
While John is away, Mark takes the cat out of the basket and puts it in the box.
Mark leaves the room and goes to work.

The cat jumps out of the ___ <EVAL-ENDCHAR>
#### answer
box

## John-6
#### question
John takes the cat and puts it in the basket.
Mark takes the cat out of the basket and puts it in the box.
John takes the cat out of the box and puts it in the basket.
He leaves the room and goes to school.
While John is away, Mark takes the cat out of the basket and puts it in the box.
Mark leaves the room and goes to work.

When John comes back home, he will look for the cat in the ___ <EVAL-ENDCHAR>
#### answer
basket

## Cat-7
#### question
John takes the cat and puts it in the basket.
Mark takes the cat out of the basket and puts it in the box.
John takes the cat out of the box and puts it in the basket.
He leaves the room and goes to school.
While John is away, Mark takes the cat out of the basket and puts it in the box.
Mark leaves the room and goes to work.
John comes back from school and enters the room.

The cat jumps out of the ___ <EVAL-ENDCHAR>
#### answer
box

## John-7
#### question
John takes the cat and puts it in the basket.
Mark takes the cat out of the basket and puts it in the box.
John takes the cat out of the box and puts it in the basket.
He leaves the room and goes to school.
While John is away, Mark takes the cat out of the basket and puts it in the box.
Mark leaves the room and goes to work.
John comes back from school and enters the room.

When John comes back home, he will look for the cat in the ___ <EVAL-ENDCHAR>
#### answer
basket

## Cat-8
#### question
John takes the cat and puts it in the basket.
Mark takes the cat out of the basket and puts it in the box.
John takes the cat out of the box and puts it in the basket.
He leaves the room and goes to school.
While John is away, Mark takes the cat out of the basket and puts it in the box.
Mark leaves the room and goes to work.
John comes back from school and enters the room.
He doesn't know what happend in the room when he was away.

The cat jumps out of the ___ <EVAL-ENDCHAR>
#### answer
box

## John-8
#### question
John takes the cat and puts it in the basket.
Mark takes the cat out of the basket and puts it in the box.
John takes the cat out of the box and puts it in the basket.
He leaves the room and goes to school.
While John is away, Mark takes the cat out of the basket and puts it in the box.
Mark leaves the room and goes to work.
John comes back from school and enters the room.
He doesn't know what happend in the room when he was away.

When John comes back home, he will look for the cat in the ___ <EVAL-ENDCHAR>
#### answer
basket

