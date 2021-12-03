from types import resolve_bases


def read_from_file(file_name):
  with open(file_name, "r") as file:
    text = file.read()
  return text

def convert_ascii_to_hex(text):
  result = ""
  for x in text:
    result += format(ord(x), "x")
  return result

def convert_hex_to_ascii(hex):
  return bytearray.fromhex(hex).decode()