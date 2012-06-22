#cipher

phrase = raw_input('Enter sentence to encrypt: ')
shift_value = input('Enter shift value: ')

encoded_phrase = ''
for c in phrase:
    if c.isalpha():
            ascii_code = ord(c)
            ascii_code+=shift_value
            cha = chr(ascii_code)
            
            if c.isupper():
                if ascii_code > 90:
                    ascii_code = ascii_code%91
                    ascii_code+=65
                    cha = chr(ascii_code)
                encoded_phrase = encoded_phrase +  cha

            if c.islower():
                if ascii_code > 122:
                    ascii_code = ascii_code%123
                    ascii_code+=97
                    cha = chr(ascii_code)
                encoded_phrase = encoded_phrase +  cha

    elif c.isdigit():
        encoded_phrase = encoded_phrase + str((int(c) + shift_value)%6)
    else:
        encoded_phrase = encoded_phrase + c
print 'The encoded phrase is: ',encoded_phrase
    
