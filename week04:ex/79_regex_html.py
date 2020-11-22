import re
TAG_RE = re.compile(r'<[^>]+>')
def remove_tags(text):
    return TAG_RE.sub('', text)

print(remove_tags("<h1>hello</h1> <p>hello</p>"))
print(remove_tags("<html lang = 'pl' ><body> content of body </body> ...</html>"))
print(remove_tags(""))
print(remove_tags("hello"))
print(remove_tags("<<><>>><>"))
