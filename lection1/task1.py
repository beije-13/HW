from urllib import parse
from re import match

def domain_name(url):
    if not match('(?:http|ftp|https)://', url):
        url = '%s%s' % ('http://', url)
    result = parse.urlparse(url).netloc
    if result.split('.')[0] == "www":
        return result.split('.')[1]
    else:
        return result.split('.')[0]


assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"
