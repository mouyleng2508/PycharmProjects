import requests
def get_fbid(fb_url):
    URL = "https://findmyfbid.com/"
    PARAMS = {'url': fb_url}
    response = requests.get(fb_url)
    tuple = ()
    try:
        req = requests.post(url=URL, params=PARAMS)
        res = response.status_code
        new_req = req.json().get("id")
        tuple = tuple + (res, new_req)
        return tuple

    except Exception:
        return ''

print(get_fbid("https://www.facebook.com/KITinstitute/"))
