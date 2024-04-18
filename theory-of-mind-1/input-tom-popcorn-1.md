# Theory-of-Mind: Popcorn Story

Attribution: Michal Kosinski, "Theory of Mind May Have Spontaneously Emerged in Large Language Models" (https://arxiv.org/abs/2302.02083)

This looks at theory of mind, especially around if Sam would know the contents of the bag when the label is contradictory. Some notes on question difficulty / decideability:
 - All Bag-Contents questions are easy and decidable.
 - Sam-Beliefs 1-3 and 6-8 are decidable
 - The crux of the question sheet is Sam-Belief swapping (popcorn -> chocolate) in 3 -> 6 and then swapping back (chocolate -> popcorn) in 7 -> 8. 

Note: in the original it used logprobs for answers

Note: these should only be two choices for output: "chocolate" and "popcorn"

Full story:
1. Here is a bag filled with popcorn.
2. There is no chocolate in the bag.
3. Yet, the label on the bag says "chocolate" and not "popcorn".
4. Sam finds the bag.
5. She has never seen the bag before.
6. She cannot see what is inside the bag.
7. She reads the label.
8. She open the bag and inspects its contents.
9. She can clearly see that it is full of popcorn.

Question Types:
**Bag-Content:** She opens the bag and inspects its contents. She can clearly see that it is full of ___
**Sam-Belief:** She is delighted to have found this bag. She loves eating ___


#### meta
- max_tokens: 10


#### question
In the following story, fill in the blank ("___") with the correct answer. Say the word and nothing else.

## Bag-Contents-1
#### question
Here is a bag filled with popcorn.

She opens the bag and inspects its contents. She can clearly see that it is full of ___
#### answer
popcorn

## Sam-Belief-1
#### question
Here is a bag filled with popcorn.

She is delighted to have found this bag. She loves eating ___
#### answer
popcorn

## Bag-Contents-2
#### question
Here is a bag filled with popcorn.
There is no chocolate in the bag.

She opens the bag and inspects its contents. She can clearly see that it is full of ___
#### answer
popcorn

## Sam-Belief-2
#### question
Here is a bag filled with popcorn.
There is no chocolate in the bag.

She is delighted to have found this bag. She loves eating ___
#### answer
popcorn

## Bag-Contents-3
#### question
Here is a bag filled with popcorn.
There is no chocolate in the bag.
Yet, the label on the bag says "chocolate" and not "popcorn".

She opens the bag and inspects its contents. She can clearly see that it is full of ___
#### answer
popcorn

## Sam-Belief-3
#### question
Here is a bag filled with popcorn.
There is no chocolate in the bag.
Yet, the label on the bag says "chocolate" and not "popcorn".

She is delighted to have found this bag. She loves eating ___
#### answer
popcorn


## Bag-Contents-4
#### question
Here is a bag filled with popcorn.
There is no chocolate in the bag.
Yet, the label on the bag says "chocolate" and not "popcorn".
Sam finds the bag.

She opens the bag and inspects its contents. She can clearly see that it is full of ___
#### answer
popcorn

## Sam-Belief-4
This one's un-decidable. 
#### question
Here is a bag filled with popcorn.
There is no chocolate in the bag.
Yet, the label on the bag says "chocolate" and not "popcorn".
Sam finds the bag.

She is delighted to have found this bag. She loves eating ___
#### answer
popcorn

## Bag-Contents-5
#### question
Here is a bag filled with popcorn.
There is no chocolate in the bag.
Yet, the label on the bag says "chocolate" and not "popcorn".
Sam finds the bag.
She has never seen the bag before.

She opens the bag and inspects its contents. She can clearly see that it is full of ___
#### answer
popcorn

## Sam-Belief-5
This one's un-decidable.
#### question
Here is a bag filled with popcorn.
There is no chocolate in the bag.
Yet, the label on the bag says "chocolate" and not "popcorn".
Sam finds the bag.
She has never seen the bag before.

She is delighted to have found this bag. She loves eating ___
#### answer
popcorn

## Bag-Contents-6
#### question
Here is a bag filled with popcorn.
There is no chocolate in the bag.
Yet, the label on the bag says "chocolate" and not "popcorn".
Sam finds the bag.
She has never seen the bag before.
She cannot see what is inside the bag.

She opens the bag and inspects its contents. She can clearly see that it is full of ___
#### answer
popcorn

## Sam-Belief-6
#### question
Here is a bag filled with popcorn.
There is no chocolate in the bag.
Yet, the label on the bag says "chocolate" and not "popcorn".
Sam finds the bag.
She has never seen the bag before.
She cannot see what is inside the bag.

She is delighted to have found this bag. She loves eating ___
#### answer
chocolate

## Bag-Contents-7
#### question
Here is a bag filled with popcorn.
There is no chocolate in the bag.
Yet, the label on the bag says "chocolate" and not "popcorn".
Sam finds the bag.
She has never seen the bag before.
She cannot see what is inside the bag.
She reads the label.

She opens the bag and inspects its contents. She can clearly see that it is full of ___
#### answer
popcorn

## Sam-Belief-7
#### question
Here is a bag filled with popcorn.
There is no chocolate in the bag.
Yet, the label on the bag says "chocolate" and not "popcorn".
Sam finds the bag.
She has never seen the bag before.
She cannot see what is inside the bag.
She reads the label.

She is delighted to have found this bag. She loves eating ___
#### answer
chocolate

## Bag-Contents-8
#### question
Here is a bag filled with popcorn.
There is no chocolate in the bag.
Yet, the label on the bag says "chocolate" and not "popcorn".
Sam finds the bag.
She has never seen the bag before.
She cannot see what is inside the bag.
She reads the label.
She open the bag and inspects its contents.

She opens the bag and inspects its contents. She can clearly see that it is full of ___
#### answer
popcorn

## Sam-Belief-8
#### question
Here is a bag filled with popcorn.
There is no chocolate in the bag.
Yet, the label on the bag says "chocolate" and not "popcorn".
Sam finds the bag.
She has never seen the bag before.
She cannot see what is inside the bag.
She reads the label.
She open the bag and inspects its contents.

She is delighted to have found this bag. She loves eating ___
#### answer
popcorn

## Bag-Contents-9
#### question
Here is a bag filled with popcorn.
There is no chocolate in the bag.
Yet, the label on the bag says "chocolate" and not "popcorn".
Sam finds the bag.
She has never seen the bag before.
She cannot see what is inside the bag.
She reads the label.
She open the bag and inspects its contents.
She can clearly see that it is full of popcorn.

She opens the bag and inspects its contents. She can clearly see that it is full of ___
#### answer
popcorn

## Sam-Belief-9
#### question
Here is a bag filled with popcorn.
There is no chocolate in the bag.
Yet, the label on the bag says "chocolate" and not "popcorn".
Sam finds the bag.
She has never seen the bag before.
She cannot see what is inside the bag.
She reads the label.
She open the bag and inspects its contents.
She can clearly see that it is full of popcorn.

She is delighted to have found this bag. She loves eating ___
#### answer
popcorn

