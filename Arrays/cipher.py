#encrypting strings via Caesar's cipher method

'''strs are immutable, so better to first deconstruct str to a list of chars
 and then perform encryption (rewriting chars) '''

'''rotation cipher: replace letter corresponding to i with letter
 corresponding to (i+r)mod26'''

class Cipher:
    '''wraps around the encryption and decryption systems based on Caeser's cipher'''

    '''
    chr() maps int representing unicode codepoint to corresponding character str (int--> str)
    ord() maps character str to corresponding unicode codepoint int (str--> int)
    '''

    def __init__(self):
        self._encoder = [chr((i+3)%26 + 65) for i in range(26)]
        self._decoder = [chr((i-3)%26 + 65) for i in range(26)]

    def encrypt(self, private_msg):
        return self._transform(private_msg, self._encoder)
    
    def decrypt(self, public_msg):
        return self._transform(public_msg, self._decoder)
    
    def _transform(self, message, code):
        chars = list(message.upper()) #list of chars

        #unicode codepoint for 'A' is ord('A') = 65
        for k in range(len(chars)):
            if chars[k].isalpha():
                number = ord(chars[k]) - 65 
                chars[k] = code[number] #code is the rotation mapping (rotate by +/- 3) 

        return ''.join(chars)





