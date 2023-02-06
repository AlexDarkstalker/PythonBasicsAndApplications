import zipfile
import os


with zipfile.ZipFile('main.zip', 'r') as zip_ref:
    zip_ref.extractall('.')
result_list = []
for cur_dir, dirs, files in os.walk('main'):
    for file in files:
        if file[-3:] == '.py':
            print(cur_dir)
            result_list.append(cur_dir)
            break
with open('result.txt', 'w') as result:
    for res_str in sorted(result_list):
        result.write(res_str + '\n')
result.close()
