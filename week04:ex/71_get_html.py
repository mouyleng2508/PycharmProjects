import requests
def get_html(url):
    myobj = {'somekey': 'somevalue'}
    x = requests.get(url, data=myobj)
    return x.text

print(get_html('https://www.youtube.com/'))
