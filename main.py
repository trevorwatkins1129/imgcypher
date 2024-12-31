from collections import Counter
from itertools import permutations
import time
import math

def letter_frequency_analysis(text):
    # Remove non-alphabetic characters and convert to uppercase
    text = ''.join(filter(str.isalpha, text)).upper()
    total_letters = len(text)
    
    # Calculate frequency of each letter
    frequency = Counter(text)
    frequency_percent = {char: (count / total_letters) * 100 for char, count in frequency.items()}
    
    return frequency_percent

def is_beaufort_cipher(text):
    # Perform frequency analysis
    frequency = letter_frequency_analysis(text)
    
    # Expected frequency of letters in English (approximate)
    expected_frequency = {
        'A': 8.17, 'B': 1.49, 'C': 2.78, 'D': 4.25, 'E': 12.70,
        'F': 2.23, 'G': 2.02, 'H': 6.09, 'I': 7.00, 'J': 0.15,
        'K': 0.77, 'L': 4.03, 'M': 2.41, 'N': 6.75, 'O': 7.51,
        'P': 1.93, 'Q': 0.10, 'R': 5.99, 'S': 6.33, 'T': 9.06,
        'U': 2.76, 'V': 0.98, 'W': 2.36, 'X': 0.15, 'Y': 1.97,
        'Z': 0.07
    }
    
    # Calculate the difference between observed and expected frequencies
    score = 0
    for char, freq in frequency.items():
        if char in expected_frequency:
            score += abs(freq - expected_frequency[char])
    
    # A lower score indicates a higher chance of being a Beaufort cipher
    return score

def analyze_permutations(text):
    # Split the text into chunks of 5 characters
    chunks = [text[i:i+5] for i in range(0, len(text), 5)]

    print(chunks)
    
    # Generate all permutations of the chunks
    all_permutations = permutations(chunks)
    total_permutations = math.factorial(math.floor(len(text)/5))
    
    start_time = time.time()

    # Analyze each permutation
    highest_score = -1

    with open("results.txt", "a") as file:
        for index, perm in enumerate(all_permutations):
            permuted_text = ''.join(perm)
            score = is_beaufort_cipher(permuted_text)
            highest_score = score if score > highest_score else highest_score

            file.write(f"Permuted Text: {permuted_text} | Score: {score} \n")

            if (index + 1) % 100 == 0:
                elapsed_time = time.time() - start_time
                tries_per_second = (index + 1) / elapsed_time if elapsed_time > 0 else 0
                print(f"\rProcessed {index + 1}/{total_permutations} permutations | Tries per second: {tries_per_second:.2f} | Highest score: {highest_score:.2f}", end='')
    
    return results

# Example usage
input_text = "PILUNIBENGUNQZSEXAJCMFIRKHADMFTMPYROHKTMGZCLEATWFYSLOXQYRUDWLEHQJJCFOHCVYHAZSVEXNGJSLBUXGZWPSBUKDGPIRKNWPQJMVODWZIBFYBKDXQTCV"
results = analyze_permutations(input_text)

# Print the results
for permuted_text, score in results.items():
    print(f"Permuted Text: {permuted_text} | Score: {score}")
