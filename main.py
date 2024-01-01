import http.client
from fastapi import FastAPI
import json

app = FastAPI()


class Test_response:
    tran = None

    def __init__(self, tran):
        self.tran = tran


@app.post('/')
async def trans(payload: dict):
    conn = http.client.HTTPSConnection("text-translator2.p.rapidapi.com")

    payload = "source_language=en&target_language=id&text=What%20is%20your%20name%3F"

    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'X-RapidAPI-Key': "a5bae056dfmshab48a57f0d0a5fcp1fe870jsn1176b75e8e3e",
        'X-RapidAPI-Host': "text-translator2.p.rapidapi.com"
    }

    conn.request("POST", "/translate", payload, headers)
    res = conn.getresponse()
    data = res.read()
    x = json.loads(data)
    data_list = []
    for item in x:
        data_list.append(item.get('data'))

    conn.close()

    return data_list
