import string

LOWER = string.ascii_lowercase
SKIP = string.digits + string.whitespace + string.punctuation


def caesar_cipher_encode(plain_text: str, step=3):
	cipher = ''

	for c in plain_text:
		if c in SKIP:
			cipher += c
			continue
		diff = ord(c) - (ord('a') if c in LOWER else ord('A'))
		diff = (diff + step) % 26
		cipher += chr(diff + 
						(ord('a') if c in LOWER else ord('A'))
					)
		return cipher