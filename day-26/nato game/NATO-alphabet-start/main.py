#TODO 1. Create a dictionary in this format:
import pandas
import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "nato_phonetic_alphabet.csv")

data = pandas.read_csv(file_path)
nato_dict = {row["letter"]: row["code"] for (index, row) in data.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
 
word = input("Enter a word: ")
# Create list of phonetic code words for each letter in the input

phonetic_list = [nato_dict[letter.upper()] for letter in word if letter.strip()]
print(phonetic_list)


