from simplecrypt import encrypt, decrypt

json=""

key="BEST"
ciphertext = encrypt(key, 'password')
plaintext = decrypt(key, ciphertext)

print ciphertext
print plaintext

print decrypt(key, json)