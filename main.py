import rsa
import input

print("simple RSA")
public_key, private_key = rsa.generate_key()
print(f"public : {public_key}")
print(f"private: {private_key}")

text_msg = input.read_from_file("msg.txt")
msg = input.convert_ascii_to_hex(text_msg)
encrypted = rsa.encrypt_msg(msg, public_key)
decrypted = rsa.decrypt_msg(encrypted, private_key)
decrypted_text = input.convert_hex_to_ascii(''.join(str(x) for x in decrypted))

print("########################")
print(f"text msg: {text_msg}")
print("--------")
print(f"msg: {msg}")
print("--------")
print(f"encrypted: {''.join(str(x) for x in encrypted)}")
print("--------")
print(f"decrypted: {''.join(str(x) for x in decrypted)}")
print("--------")
print(f"decrypted: {decrypted_text}")
print("--------")