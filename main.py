'''
description: A simple typing speed test application that measures typing speed and accuracy.
author: OpenAI ChatGPT
'''

import time # time module used for time-related functions

import random # random module used for generating random numbers

sentences = [ # List of sentences to choose from
    "The quick brown fox jumps over the lazy dog.",
    "A journey of a thousand miles begins with a single step.",
    "To be or not to be, that is the question.",
    "In the beginning was the Word, and the Word was with God.",
    "The only way to do great work is to love what you do."
]
def measure_accuracy(user_input, test_sentence):
    correct_chars = sum(1 for a, b in zip(user_input, test_sentence) if a == b)
    accuracy = (correct_chars / len(test_sentence)) * 100 if test_sentence else 0
    return accuracy

def typing_test():
    test_sentence = random.choice(sentences) # Select a random sentence
    print("Type the following sentence as fast as you can:")
    print(test_sentence) # Display the sentence to the user
    input("Press Enter when you are ready to start...") # Wait for user to be ready
    start_time = time.time() # Measure the start time
    user_input = input("\nStart typing:\n") # Get user input
    end_time = time.time() # Measure the end time
    time_taken = end_time - start_time # Calculate time taken
    words_count = len(test_sentence.split(" ")) # Count the number of words in the sentence

    print("Results:")
    print(f"Time taken: {time_taken / 60} seconds") # Display time taken
    print(f"Words typed: {words_count}") # Calculate and display WPM
    print(f"Typing Speed: {words_count / (time_taken / 60):.2f} WPM") # Display typing speed in WPM
    accuracy = measure_accuracy(user_input, test_sentence) # Measure accuracy
    print(f"Accuracy: {accuracy:.2f}%") # Display accuracy
    
typing_test()