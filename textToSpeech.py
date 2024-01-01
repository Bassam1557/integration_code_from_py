import http.client
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class TextToSpeechResponse(BaseModel):
    status: str
    result: str


@app.post('/textToSpeech')
def textSpeech():
    conn = http.client.HTTPSConnection("cloudlabs-text-to-speech.p.rapidapi.com")

    payload = "voice_code=en-US-1&text=hello%2C%20what%20is%20your%20name%3F&speed=1.00&pitch=1.00&output_type" \
              "=audio_url"

    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'X-RapidAPI-Key': "a5bae056dfmshab48a57f0d0a5fcp1fe870jsn1176b75e8e3e",
        'X-RapidAPI-Host': "cloudlabs-text-to-speech.p.rapidapi.com"
    }

    conn.request("POST", "/synthesize", payload, headers)

    res = conn.getresponse()
    data = res.read()
    conn.close()
    response = TextToSpeechResponse(status=data, result={"audio_url": data.decode("utf-8")})

    return response

