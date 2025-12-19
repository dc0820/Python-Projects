import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

dict_nato = {row.letter : row.code for (index, row) in nato_data.iterrows()}
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        phonetic = [dict_nato[letter] for letter in word]

    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()

    else:
        print(phonetic)

generate_phonetic()


