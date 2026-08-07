import pandas
import os


script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "nato_phonetic_alphabet.csv")

data = pandas.read_csv(file_path)
nato_dict = {row["letter"]: row["code"] for (index, row) in data.iterrows()}

def generate_phonetic():
    word = input("Enter a word: ")
    try:
        phonetic_list = [nato_dict[letter.upper()] for letter in word if letter.strip()]
    except KeyError:
        print("Please enter only letters.")
        generate_phonetic()
    else:
        print(phonetic_list)

generate_phonetic()