import requests

def get_fact(number):
    url = "http://numbersapi.com/{}".format(number)
    
    r = requests.get(url)
    if r.status_code == 200:
        return r.text
    else:
        return "Error: API call failed with error code {}".format(r.status_code)