'''
pip install pycryptodome
'''

from Crypto.PublicKey import RSA

key = RSA.generate(2048)
privateKey = key.export_key()
publicKey = key.publickey().export_key()

# save private key to file
with open('private.pem', 'wb') as f:
    f.write(privateKey)

# save public key to file
with open('public.pem', 'wb') as f:
    f.write(publicKey)

print('Private key saved to private.pem')
print('Public key saved to public.pem')
print('Done')
print(privateKey)