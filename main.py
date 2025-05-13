import pandas

morse_running = True

morse_code_df = pandas.read_csv("morse_code.csv")

letter_to_morse_code_dict = {row.char: row.code for (index, row) in morse_code_df.iterrows()}
morse_code_to_letter_dict = {row.code: row.char for (index, row) in morse_code_df.iterrows()}



def convert_text_to_morse(text_input):
    result = []
    for char in text_input:
        if char == " ":
            result.append("/")
        elif char in letter_to_morse_code_dict:
            result.append(letter_to_morse_code_dict[char])

    return " ".join(result)

def convert_morse_to_text(morse_input):
    morse_codes = morse_input.split()
    print(morse_codes)
    result = []
    for char in morse_codes:
        if char == "/":
            result.append(" ")
        elif char in morse_code_to_letter_dict:
            result.append(morse_code_to_letter_dict[char])

    return "".join(result)



if __name__ == "__main__":
    while morse_running:
        user_choice = input("Do you wish to (1) Convert Text to Morse, (2) Convert Morse to Text, (3) Quit: ")
        if user_choice.strip() == "1":
            user_input = input("Enter the text you wish to convert to Morse code: ").upper().strip()
            print(f"{user_input.title()} is {convert_text_to_morse(user_input)} in Morse Code.")
        elif user_choice.strip() == "2":
            morse_user_input = input("Enter the Morse Code you wish to convert to text: ").upper().strip()
            print(f'{morse_user_input} is "{convert_morse_to_text(morse_user_input).lower()}" in normal text.')
        elif user_choice.strip() == "3":
            print("Goodbye!")
            morse_running = False
        else:
            print("Invalid input. Please try again.")







