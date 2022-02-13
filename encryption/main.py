# encrypt message with a public key
# colaborate with github copilot
#
# encrypt('data.txt', 'public.pem')
# decrypt('data_encrypted.txt', 'private.pem')
# author : Febi Mudiyanto
# date : 13 Februari 2022


from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
import os


def encrypt(dataFile, publicKeyFile):
    '''
    use EAX mode to allow detection of unauthorized modifications
    '''
    # read data from file
    with open(dataFile, 'rb') as f:
        data = f.read()
    
    # convert data to bytes
    data = bytes(data)

    # read public key from file
    with open(publicKeyFile, 'rb') as f:
        publicKey = f.read()
    
    # create public key object
    key = RSA.import_key(publicKey)
    sessionKey = os.urandom(16)

    # encrypt the session key with the public key
    cipher = PKCS1_OAEP.new(key)
    encryptedSessionKey = cipher.encrypt(sessionKey)

    # encrypt the data with the session key
    cipher = AES.new(sessionKey, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    []

    # save the encrypted data to file
    [ fileName, fileExtension ] = dataFile.split('.')
    encryptedFile = fileName + '_encrypted.' + fileExtension
    with open(encryptedFile, 'wb') as f:
        [ f.write(x) for x in (encryptedSessionKey, cipher.nonce, tag, ciphertext) ]
    print('Encrypted file saved to ' + encryptedFile)
    

def decrypt(dataFile, privateKeyFile):
    '''
    use EAX mode to allow detection of unauthorized modifications
    '''

    # read private key from file
    with open(privateKeyFile, 'rb') as f:
        privateKey = f.read()
        # create private key object
        key = RSA.import_key(privateKey)


    # read data from file
    with open(dataFile, 'rb') as f:
        # convert data to bytes
        

        # read the session key
        encryptedSessionKey, nonce, tag, ciphertext = [ f.read(x) for x in (key.size_in_bytes(), 16, 16, -1) ]

    
    # decrypt the session key
    cipher = PKCS1_OAEP.new(key)
    sessionKey = cipher.decrypt(encryptedSessionKey)

    # decrypt the data with the session key
    cipher = AES.new(sessionKey, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)

    # save the decrypted data to file
    [ fileName, fileExtension ] = dataFile.split('.')
    decryptedFile = fileName + '_decrypted.' + fileExtension
    with open(decryptedFile, 'wb') as f:
        f.write(data)


    print('Decrypted file saved to ' + decryptedFile)




data = 'data.txt'
publicKeyFile = 'public.pem'
encrypt( data, publicKeyFile )
print('\n')

decryptFile = 'data_encrypted.txt'
privateKeyFile = 'private.pem'

decrypt(decryptFile, privateKeyFile)

print('Done')
