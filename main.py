import rsa
import input

def print_all(title, text, hex, encrypted, decrypted, decrypted_text):
  print(f"---------{title}-------------")
  print(f"text msg: {text}")
  print("--------")
  print(f"hex msg: {hex}")
  print("--------")
  print(f"hex encrypted: {''.join(str(x) for x in encrypted)}")
  print("--------")
  print(f"decrypted: {''.join(str(x) for x in decrypted)}")
  print("--------")
  print(f"text decrypted: {decrypted_text}")
  print("--------")

def rsa_test():
  public_key, private_key = rsa.generate_key()
  print(f"public : {public_key}")
  print(f"private: {private_key}")

  text_msg = input.read_from_file("50_chars.txt")
  msg = input.convert_ascii_to_hex(text_msg)
  encrypted = rsa.encrypt_msg(msg, public_key)
  decrypted = rsa.decrypt_msg(encrypted, private_key)
  decrypted_text = input.convert_hex_to_ascii(''.join(str(x) for x in decrypted))
  print_all("rsa_test", text_msg, msg, encrypted, decrypted, decrypted_text)

def digital_signature():
  public_key_A, private_key_A = rsa.generate_key()
  print(f"public : {public_key_A}")
  print(f"private: {private_key_A}")
  public_key_B, private_key_B = rsa.generate_key()
  print(f"public : {public_key_B}")
  print(f"private: {private_key_B}")
  msg_txt_20 = input.read_from_file("20_chars.txt")
  msg_20 = input.convert_ascii_to_hex(msg_txt_20)

  signed_A = rsa.encrypt_msg(msg_20, private_key_A)
  read_A = rsa.decrypt_msg(signed_A, public_key_A)
  read_A_text = input.convert_hex_to_ascii(''.join(str(x) for x in read_A))
  signed_B = rsa.encrypt_msg(msg_20, private_key_B)
  read_B = rsa.decrypt_msg(signed_B, public_key_B)
  read_B_text = input.convert_hex_to_ascii(''.join(str(x) for x in read_B))
  print_all("signature A", msg_txt_20, msg_20, signed_A, read_A, read_A_text)
  print_all("signature B", msg_txt_20, msg_20, signed_B, read_B, read_B_text)




print("simple RSA")
rsa_test()
digital_signature()
