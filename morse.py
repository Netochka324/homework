MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}

def decode_morse(morse_code):
    # Remember - you can use the preloaded MORSE_CODE dictionary:
    # For example:
    # MORSE_CODE['.-'] = 'A'
    # MORSE_CODE['--...'] = '7'
    # MORSE_CODE['...-..-'] = '$'
    sp = morse_code.split('   ')
    sp = [i.split() for i in sp]
    print(sp)
    for k in MORSE_CODE_DICT.keys():
        for x in sp:
            for j in x:
                if j == MORSE_CODE_DICT[k]:
                    j = k
    print(sp)
    # for k in range(len(sp)):
    #     sp2.append(''.join(sp1[k]))
    # return ' '.join(sp2)


print(decode_morse('.... . -.--   .--- ..- -.. .'))
