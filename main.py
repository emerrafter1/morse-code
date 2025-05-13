import pandas

morse_code_df = pandas.read_csv("morse_code.csv")

morse_code_dict = {row.char: row.code for (index, row) in morse_code_df.iterrows()}


def convert_text_to_morse(text_input):
    result = []
    for char in text_input:
        if char == " ":
            result.append("/")
        elif char in morse_code_dict:
            result.append(morse_code_dict[char])

    return " ".join(result)


user_input = input("Enter the text you wish to convert to Morse code: ").upper().strip()
print(f"{user_input.title()} is {convert_text_to_morse(user_input)} in Morse Code. ")