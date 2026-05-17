import pandas

csv = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_phonetic_alphabet = {row["letter"]:row["code"] for (index, row) in csv.iterrows()}

word = input("Enter a word: ").replace(" ", "")
print([nato_phonetic_alphabet[nato_word.upper()] for nato_word in word])