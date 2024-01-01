import http.client
from fastapi import FastAPI

app = FastAPI()


@app.post('/searches/organizations')
def search():
    conn = http.client.HTTPSConnection("crunchbase-crunchbase-v1.p.rapidapi.com")

    payload = {
        "field_ids": [
            "identifier",
            "location_identifiers",
            "short_description",
            "rank_org"
        ],
        "limit": 50,
        "order": [
            {
                "field_id": "rank_org",
                "sort": "asc"
            }
        ],
        "query": [
            {
                "field_id": "location_identifiers",
                "operator_id": "includes",
                "type": "predicate",
                "values": [
                    "6106f5dc-823e-5da8-40d7-51612c0b2c4e"
                ]
            },
            {
                "field_id": "facet_ids",
                "operator_id": "includes",
                "type": "predicate",
                "values": [
                    "company"
                ]
            }
        ]
    }

    headers = {
        'content-type': "application/json",
        'X-RapidAPI-Key': "a5bae056dfmshab48a57f0d0a5fcp1fe870jsn1176b75e8e3e",
        'X-RapidAPI-Host': "crunchbase-crunchbase-v1.p.rapidapi.com"
    }

    conn.request("POST", "/searches/organizations", payload, headers)
    res = conn.getresponse()
    data = res.read()
    return data.decode("utf-8")
