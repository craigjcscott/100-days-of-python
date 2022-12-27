import pandas as pd

nato_df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}


def convert_nato():
    user_word = input("Type a word or phrase (resulting list will not include spaces): ")
    user_word = user_word.upper().replace(" ", "")
    nato_list = [nato_dict[letter] for letter in user_word]
    print(nato_list)
    run_again = input("Convert another word? Y/N: ")
    if run_again.upper() == "Y":
        convert_nato()


convert_nato()
