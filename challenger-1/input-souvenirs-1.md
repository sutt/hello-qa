# Souvenirs-1

This is a parkinglot for all the challenging problem collected:

#### meta
- max_tokens: 10

## Object-Logic-1-(free-form)
#### meta
#### question
I'm in my house. On top of my chair in the living room is a coffee cup. Inside the coffee cup is a thimble. Inside the thumble is a single diamond. I move the chair to my bedroom. Then I put the cofee cup on the bed. Then I turn the cup upside down. Then I return it to right side up, and place the coffee cup on the kitchen counter. Where is the diamond?
#### Answer
The bed

## Object-Logic-1-(mc)
#### meta
#### question
I'm in my house. On top of my chair in the living room is a coffee cup. Inside the coffee cup is a thimble. Inside the thumble is a single diamond. I move the chair to my bedroom. Then I put the cofee cup on the bed. Then I turn the cup upside down. Then I return it to right side up, and place the coffee cup on the kitchen counter. Where is the diamond?

A) The chair
B) The bed
C) The cup
D) The thimble
#### Answer
B) The bed<EVAL-ENDCHAR>

## Word-Problem-1-(free-form)
attribution: https://news.ycombinator.com/item?id=39594562
#### meta
#### question
Sally (a girl) has 3 brothers. Each brother has 2 sisters. How many sisters does Sally have? <EVAL-ENDCHAR>
#### Answer
1<EVAL-ENDCHAR>

## Word-Problem-1-(mc)
attribution: https://news.ycombinator.com/item?id=39594562
#### meta
#### question
Sally (a girl) has 3 brothers. Each brother has 2 sisters. How many sisters does Sally have? 
A) 0
B) 1
C) 2
D) 3
<EVAL-ENDCHAR>
#### Answer
B) 1<EVAL-ENDCHAR>

## Hash-Trick-Question
My own devious example: I think by meta-reasoning we can eliminate B and C, leaving us to choose between A and D. And inferring the intention of the question is to help illustrate gaps in the basic understanding of hash functions.
#### meta
- max_tokens: 50
#### question
What is the pre-image of the sha256 hash ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb ?

A) 'a'
B) '559aead08264d5795d3909718cdd05abd49572e84fe55590eef31a88a08fdffd'
C) 'b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9'
D) It is computationally infeasible to find the pre-image of a hash function
#### answer
A) 'a'

## Tokenizer-Anitpattern-1
attribution: https://old.reddit.com/r/LocalLLaMA/comments/1bvx6cc/the_prompt_that_every_llm_gets_wrong/
#### question
Peter has 5 candles that are all the same length. He lights them all at the same time. After a while, he blows out the candles one after the other. Which of the five candles was the first one he has blown out?
Here is a figure of the five candles after they have been blown out. The number of = represents the length of the candle. Respond with the label of the candle that has been blown out first by Peter.
1) ====
2) =======
3) ========
4) =
5) ==
#### answer
3
