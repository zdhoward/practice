"""
The Enigma machine is an encryption device developed and used in the early- to mid-20th century to protect commercial, diplomatic and military communication. It was employed extensively by Nazi Germany during World War II, in all branches of the German military.
This is one particular implementation for it, based on the earlier models but
configurable for unlimited rotators.

The basic idea of the encryption is as follows:
- Take the plain text and switch certain letters based on a patchboard
- Run the result of the the patchboard through a polyalphabetic substitution
    cipher with the following rules:
    - Increment the cipher key for the last rotator 1 for every step
    - Have set step frequencies in which the other rotators increment for every
        nth step
- Take the encrypted text and run it through the patchboard to switch out the
    same set of characters as before to better obfuscate the encryption pattern
- This is easily encyptable and decryptable as long as the user has the correct
    configuration
"""

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main():

    plain_text = "Super secret code that the English will never understand"

    plugboard = [
        ("T", "Q"),
        ("H", "L"),
        ("E", "Z"),
        ("I", "G"),
        ("A", "P"),
        ("N", "R"),
        ("M", "O"),
        ("Y", "S"),
    ]  # pairs that are switched before and after the rotors

    rotators = [
        (1, 2),
        (17, 3),
        (12, 1),
        # (5, 7),
        # (7, 17),
    ]  # 3 rotators, (starting_value, step_frequency) with the last rotator changing every key press

    cipher_text = enigma(plugboard, rotators, "encrypt", plain_text)
    decrypted_text = enigma(plugboard, rotators, "decrypt", cipher_text)

    print("Encrypting: ", plain_text)
    print("Encrypted : ", cipher_text)
    print("Decrypted : ", decrypted_text)


def enigma(_plugboard, _rotators, _function, _text):
    if _function.lower() == "encrypt":
        processed_text = enigma_encrypt(_plugboard, _rotators, _text)
    elif _function.lower() == "decrypt":
        processed_text = enigma_decrypt(_plugboard, _rotators, _text)
    else:
        print("_function not provided; select 'encrypt' or 'decrypt'")
    return processed_text


def enigma_decrypt(_plugboard, _rotators, _text):
    _text = _text.upper()
    cipher_text = plugboard_switch(_plugboard, _text)
    cipher_text = rotators_decrypt(_rotators, cipher_text)
    cipher_text = plugboard_switch(_plugboard, cipher_text)
    return "".join(cipher_text)


def enigma_encrypt(_plugboard, _rotators, _text):
    _text = _text.upper()
    cipher_text = plugboard_switch(_plugboard, _text)
    cipher_text = rotators_encrypt(_rotators, cipher_text)
    cipher_text = plugboard_switch(_plugboard, cipher_text)
    return "".join(cipher_text)


def plugboard_switch(_plugboard, _text):
    """
    The Enigma's Plugboard unit is manually patched to switch 2 letters before
    and after the rotators' conversion
    """
    _text = list(_text)
    for char1, char2 in _plugboard:
        all_c1 = []
        all_c2 = []
        pos = 0
        for char in _text:
            if char == char1:
                all_c1.append(pos)
            elif char == char2:
                all_c2.append(pos)
            for char in all_c1:
                _text[char] = char2
            for char in all_c2:
                _text[char] = char1
            pos += 1
    return "".join(_text)


def rotators_encrypt(_rotators, _text):
    """
    The rotators work by being given both an initial value as well as a
    frequency of how often it shifts up.
    The last rotator always increments one for every character encoded/decoded
    and other rotators can be configured for different frequencies.
    If Rotator 1 has a frequency of 3 then after every 3 steps that rotator
    is increased by 1.
    """
    global alphabet
    _text = list(_text)
    cipher_text = []
    step = 0
    for char in _text:
        if char != " ":
            offset = 0
            for starting_pos, step_frequency in _rotators:
                offset += starting_pos + int(step / step_frequency)
            cur_pos = alphabet.find(char)
            new_pos = (cur_pos + offset) % 26
            cipher_text.append(alphabet[new_pos])
            step += 1
        else:
            cipher_text.append(" ")
    return "".join(cipher_text)


def rotators_decrypt(_rotators, _text):
    """
    The rotators work by being given both an initial value as well as a
    frequency of how often it shifts up.
    The last rotator always increments one for every character encoded/decoded
    and other rotators can be configured for different frequencies.
    If Rotator 1 has a frequency of 3 then after every 3 steps that rotator
    is increased by 1.
    """
    global alphabet
    _text = list(_text)
    plain_text = []
    step = 0

    for char in _text:
        if char != " ":
            offset = 0
            for starting_pos, step_frequency in _rotators:
                offset -= starting_pos + int(step / step_frequency)
            cur_pos = alphabet.find(char)
            new_pos = (cur_pos + offset) % 26
            plain_text.append(alphabet[new_pos])
            step += 1
        else:
            plain_text.append(" ")
    return "".join(plain_text)


if __name__ == "__main__":
    main()
