def caesar_shift_character(char, key, mode):
    ascii_start = 32
    ascii_end = 126
    range_size = ascii_end - ascii_start + 1

    if mode == "encrypt":
        shifted_code = ((ord(char) - ascii_start) + key) % range_size + ascii_start
    else:
        shifted_code = ((ord(char) - ascii_start) - key) % range_size + ascii_start
    return chr(shifted_code)


shifted = caesar_shift_character("s", 10, "encrypt")
print(shifted)
print(caesar_shift_character(shifted, 10, "decrypt"))

def caesar_shift_sentence(sentence, key, mode):
    new_sentence = ""

    for char in sentence:
        new_sentence += caesar_shift_character(char, key, mode)

    return new_sentence

print(caesar_shift_sentence("This is a good day", 5, "encrypt"))


def caesar_shift_list(sentences, key, mode):
    sentences_list = []
    for sentence in sentences:
        sentences_list.append(caesar_shift_sentence(sentence, key, mode))
    return sentences_list
sentences = ["This is a good day", "Tomorrow will be a better day."]
sentences_new = caesar_shift_list(sentences, 5, "encrypt")
print(sentences_new)
print(caesar_shift_list(sentences_new, 5, "decrypt"))

def caesar_shift_file(input_filename, key, mode):
    with open(input_filename, "r") as infile:

        with open(output_filename, "w") as outfile:
            for line in infile:
                shifte_line = caesar_shift_character(line.strip(), key, mode)
                outfile.write(shifted_line + "\n")

caesar_shift_file("in.txt",)