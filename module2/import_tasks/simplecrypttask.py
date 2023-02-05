import urllib.request
import os.path as os_path
from simplecrypt import decrypt


passwords_file_path = 'passwords.txt'
encrypted_file_path = 'encrypted.bin'
if not (os_path.exists(passwords_file_path) and os_path.exists(encrypted_file_path)):
    urllib.request.urlretrieve('https://stepik.org/media/attachments/lesson/24466/encrypted.bin', 'encrypted.bin')
    urllib.request.urlretrieve('https://stepik.org/media/attachments/lesson/24466/passwords.txt', 'passwords.txt')
with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()
with open("passwords.txt", "r", encoding='utf8') as passwords:
    for line in passwords:
        try:
            print(line.strip())
            print(decrypt(line.strip(), encrypted).decode('utf-8'))
            break
        except Exception:
            print("wrong password - ", line)
