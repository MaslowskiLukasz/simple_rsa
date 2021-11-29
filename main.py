import rsa

print("simple RSA")
public_key, private_key = rsa.generate_key()
print(f"public : {public_key}")
print(f"private: {private_key}")

msg = "90294457294572943572039578"
#encrypted = rsa.encrypt(msg, public_key)
#decrypted = rsa.decrypt(encrypted, private_key)
encrypted = rsa.encrypt_msg(msg, public_key)
decrypted = rsa.decrypt_msg(encrypted, private_key)

print("########################")
print(f"msg: {msg}")
print(f"encrypted: {''.join(str(x) for x in encrypted)}")
print(f"decrypted: {''.join(str(x) for x in decrypted)}")