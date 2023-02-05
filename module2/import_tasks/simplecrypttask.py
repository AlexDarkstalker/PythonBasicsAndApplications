import urllib.request
import os.path as os_path
import os
from simplecrypt import decrypt


passwords_file_path = 'import_tasks/passwords.txt'
encrypted_file_path = 'import_tasks/encrypted.bin'
if not (os_path.exists(passwords_file_path) and os_path.exists(encrypted_file_path)):
    urllib.request.urlretrieve('https://stepik.org/media/attachments/lesson/24466/encrypted.bin', encrypted_file_path)
    urllib.request.urlretrieve('https://stepik.org/media/attachments/lesson/24466/passwords.txt', passwords_file_path)
with open(encrypted_file_path, "rb") as inp:
    encrypted = inp.read()
with open(passwords_file_path, "r", encoding='utf8') as passwords:
    for line in passwords:
        try:
            print(line.strip())
            print(decrypt(line.strip(), encrypted).decode('utf-8'))
            break
        except Exception:
            print("wrong password - ", line)
