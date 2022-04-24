import requests as http

rv = http.post(
    url='http://localhost:5005/webhooks/rest/webhook',
    json={
        "sender": "test_user",
        "message": "Hi"
    }
)

print(rv.json())
