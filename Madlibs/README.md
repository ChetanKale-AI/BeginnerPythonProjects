# Madlibs Game - Python

This is a simple **Madlibs** game written in Python. The program asks the user to input an adjective, two verbs, and the name of a famous person. These inputs are then used to generate a fun sentence using string concatenation.

## How It Works

1. The program prompts the user for the following:
   - An adjective (e.g., "amazing", "fun")
   - A verb (e.g., "run", "jump")
   - Another verb (e.g., "sing", "dance")
   - A famous person (e.g., "Albert Einstein", "Beyoncé")

2. Using these inputs, the program constructs a sentence and prints it out:
   ```python
   Computer programming is so [Adjective]! It makes me so excited all the time because I love to [Verb1]. Stay hydrated like [Verb2] and you are [Famous Person]!

  ## What We Did
- User Input: We used the input() function to get responses from the user.  
- String Concatenation: The program uses f-strings (formatted string literals) to insert user inputs into the predefined sentence.  
- Print Statement: The final output is printed using the print() function.  

## For example, if the inputs were:

Adjective: awesome  
Verb1: code  
Verb2: run  
Famous Person: Elon Musk  

The output would be:
   ```python
   Computer programming is so awesome! It makes me so excited all the time because I love to code. Stay hydrated like run and you are Elon Musk!

