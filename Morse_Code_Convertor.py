morse_code_dict = {

    'A': '.-',

    'B': '-...',

    'C': '-.-.',

    'D': '-..',

    'E': '.',

    'F': '..-.',

    'G': '--.',

    'H': '....',

    'I': '..',

    'J': '.---',

    'K': '-.-',

    'L': '.-..',

    'M': '--',

    'N': '-.',

    'O': '---',

    'P': '.--.',

    'Q': '--.-',

    'R': '.-.',

    'S': '...',

    'T': '-',

    'U': '..-',

    'V': '...-',

    'W': '.--',

    'X': '-..-',

    'Y': '-.--',

    'Z': '--..',

    '0': '-----',

    '1': '.----',

    '2': '..---',

    '3': '...--',

    '4': '....-',

    '5': '.....',

    '6': '-....',

    '7': '--...',

    '8': '---..',

    '9': '----.',

    '.': '.-.-.-',

    ',': '--..--',

    '?': '..--..',

    '/': '-..-.',

    '-': '-....-',

    '(': '-.--.',

    ')': '-.--.-'

}


def string_to_morse_code(input_str):

    morse_code_list = []

    for char in input_str:

        if char.upper() in morse_code_dict:

            morse_code_list.append(morse_code_dict[char.upper()])

    return ' '.join(morse_code_list)


input_str = input('Enter a string to convert to Morse Code: ')

morse_code = string_to_morse_code(input_str)

print(morse_code)
