# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token  = "your_auth_token"
client = TwilioRestClient(account_sid, auth_token)

call = client.calls.create(url="http://www.example.com/sipdial.xml",
    to="sip:kate@example.com?hatchkey=4815162342",
    from_="Jack")
print(call.sid)
