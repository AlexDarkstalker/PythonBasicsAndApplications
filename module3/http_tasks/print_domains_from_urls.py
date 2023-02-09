import requests
import re


# start_url = input()
# response = requests.get(start_url.replace("stepic.org", "stepik.org"))
# if response.status_code == 200:
ref_pattern = r'''<a.*?href\s*?=\s*?["'](.*?)["']'''
dom_pattern = r'''(\w*://|)*([\w\.-]*)(/|:|)'''
    # text = response.text
text = '''<a href="http://stepic.org/courses">
<a href='https://stepic.org'>
<a href='http://neerc.ifmo.ru:1345'>
<a href="ftp://mail.ru/distib">
<a href="ya.ru"><a href="www.ya.ru">
<a href="../skip_relative_links">
<a href="/abcj/>'''
# text = r'''<a href="https://stepic.org/media/attachments/lesson/24472/sample1.html">1</a>
# <a href="http://stepic.org/courses">
# <a href='https://stepic.org'>
# <a href='http://neerc.ifmo.ru:1345'>
# <a href ="ftp://mail.ru/distib" >
# <a href="ya.ru">
# <a href="www.ya.ru">
# <a href="../skip_relative_links">
# <a href="../some_path/index.html">
# <a href="sas-_0123d.ifmo.ru">
# <a target='_top' href="http://redir.rbc.ru/cgi-bin/redirect.cgi?http://hc.ru/ru/">'''
urls = re.findall(ref_pattern, text)
# print(*urls, sep='\n')
result = []
for url in urls:
    # print(re.match(dom_pattern, url).groups())
    if re.match(dom_pattern, url) and not re.match(r"\.+", re.match(dom_pattern, url).group(2)) and \
            re.match(dom_pattern, url).group(2) not in result:
        result.append(re.match(dom_pattern, url).group(2))
print(*sorted(result), sep='\n')
