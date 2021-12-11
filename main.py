from datetime import datetime
import codecs

# 1. input file name is references.txt and should be placed in the same directory as main.py
# 2. input file structure should be the following:
#   {name}, {url}
#   {name}, {url}
#   {name}, {url}
# etc...
# 3. Access Date is today


def compose(s):
    a = s.split(',')
    name = a[0]
    url = a[1]
    date = str(datetime.date(datetime.now())).replace('-', '.')
    return '%(name)s [Электронный ресурс] //URL:%(url)s (Дата обращения: %(date)s, режим доступа: свободный)\n' % \
           {"name": name, "url": url, "date": date}


f = codecs.open("references.txt", "r", "utf-8")
content = f.read()

refs = content.splitlines()
results = [compose(r) for r in refs]

f = codecs.open("references-composed.txt", "w", "utf-8")
f.write(''.join(results))
