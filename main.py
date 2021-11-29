import rsa

print("primitive RSA")
public_key, private_key = rsa.generate_key()
print(f"public : {public_key}")
print(f"private: {private_key}")

msg = 8
encrypted = rsa.encrypt(msg, public_key)
decrypted = rsa.decrypt(encrypted, private_key)

print("########################")
print(f"msg: {msg}")
print(f"encrypted: {encrypted}")
print(f"decrypted: {decrypted}")