import requests
import re


class RequestError(Exception):
    pass


def is_in_2_follows(http_start, http_target):
    try:
        page_links = get_links(http_start)
        # print(page_links)
    except RequestError:
        return False
    for link in page_links:
        try:
            second_page_links = get_links(link)
            # print(second_page_links)
            if http_target in second_page_links:
                return True
        except RequestError:
            pass
    return False


def get_links(url):
    # pattern_link = r"<a\b.*\bhref[\b]*=[\b]*[\"'](.*?\.\w*?)[\"']"
    pattern_link = r'''<a href=['"](.*?)['"]'''
    response = requests.get(re.sub(r"stepic.org", "stepik.org", url, re.IGNORECASE))
    if response.status_code == 200 and response.headers['Content-Type'].__contains__('text'):
        html = str(response.content)
        lst = re.findall(pattern_link, html, re.IGNORECASE)
        return lst
    else:
        raise RequestError()


http_start = input()
http_target = input()
if is_in_2_follows(http_start, http_target):
    print("Yes")
else:
    print("No")
