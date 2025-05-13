import pandas

morse_code_df = pandas.read_csv("morse_code.csv")

morse_code_dict = {row.char: row.code for (index, row) in morse_code_df.iterrows()}


