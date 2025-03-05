letters='abcdefghijklmnopqrstuvwxyz'
num_letters=len(letters)

def encrypt (plaintext,key):
    ciphertext=''
    for letter in plaintext:
        letter=letter.lower()
        if not letter=='':
            index=letters.find(letter)
            if index==-1:
                ciphertext+=letter
            else:
                new_index=index+key
                if new_index>=num_letters:
                    new_index-=num_letters
                ciphertext+=letters[new_index]
    return ciphertext

def decrypt (ciphertext,key):
    plaintext=''
    for letter in ciphertext:
        letter=letter.lower()
        if not letter=='':
            index=letters.find(letter)
            if index==-1:
                plaintext+=letter
            else:
                new_index=index-key
                if new_index<0:
                    new_index+=num_letters
                plaintext+=letters[new_index]
    return plaintext

print()
print('*** Caesar Cipher Program ***')
print()

print('Do you want to encrypt or decrypt?')
user_input=input('e/d: ').lower()
print()
if user_input=='e':
    print('ENCRYPTION MODE')
    print()
    key=int(input('Enter the key between 1 to 26'))
    text=input('Enter text to encrypt: ')
    ciphertext=encrypt(text,key)
    print(f'CIPHERTEXT: {ciphertext}')

elif user_input=='d':
    print('DECRYPTION MODE')
    print()
    key=int(input('Enter the key between 1 to 26'))
    text=input('Enter text to decrypt: ')
    plaintext=decrypt(text,key)
    print(f'PLAINTEXT: {plaintext}')
