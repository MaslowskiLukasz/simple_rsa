import rsa
import file_input

def print_all(title, text, hex, encrypted, decrypted, decrypted_text):
  print(f"---------{title}-------------")
  print(f"text msg: {text}")
  print("--------")
  print(f"hex msg: {hex}")
  print("--------")
  print(f"hex signed: {''.join(str(x) for x in encrypted)}")
  print("--------")
  print(f"verified: {''.join(str(x) for x in decrypted)}")
  print("--------")
  print(f"text verified: {decrypted_text}")
  print("#########################################")

def rsa_test():
  public_key, private_key = rsa.generate_key()
  print(f"public : {public_key}")
  print(f"private: {private_key}")

  text_msg = file_input.read_from_file("50_chars.txt")
  msg = file_input.convert_ascii_to_hex(text_msg)
  encrypted = rsa.encrypt_msg(msg, public_key)
  decrypted = rsa.decrypt_msg(encrypted, private_key)
  decrypted_text = file_input.convert_hex_to_ascii(''.join(str(x) for x in decrypted))
  print_all("rsa_test", text_msg, msg, encrypted, decrypted, decrypted_text)

def digital_signature():
  msg_txt_20 = file_input.read_from_file("20_chars.txt")
  msg_20 = file_input.convert_ascii_to_hex(msg_txt_20)
  public_key_A, private_key_A = rsa.generate_key()
  print(f"public A: {public_key_A}")
  print(f"private A: {private_key_A}")
  public_key_B, private_key_B = rsa.generate_key()
  print(f"public B: {public_key_B}")
  print(f"private B: {private_key_B}")

  signed_A = rsa.encrypt_msg(msg_20, private_key_A)
  read_A = rsa.decrypt_msg(signed_A, public_key_A)
  read_A_text = file_input.convert_hex_to_ascii(''.join(str(x) for x in read_A))
  signed_B = rsa.encrypt_msg(msg_20, private_key_B)
  read_B = rsa.decrypt_msg(signed_B, public_key_B)
  read_B_text = file_input.convert_hex_to_ascii(''.join(str(x) for x in read_B))
  print_all("signature A", msg_txt_20, msg_20, signed_A, read_A, read_A_text)
  print_all("signature B", msg_txt_20, msg_20, signed_B, read_B, read_B_text)


print("1. RSA")
print("2. Podpis cyfrowy")
mode = input("Wybierz tryb: ")

if mode == "1":
  rsa_test()
else:
  digital_signature()

