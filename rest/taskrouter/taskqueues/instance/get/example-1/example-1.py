# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import TwilioTaskRouterClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token  = "your_auth_token"
workspace_sid = "WSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
taskqueue_sid = "WQXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

client = TwilioTaskRouterClient(account_sid, auth_token)

taskqueue = client.taskqueues(workspace_sid).get(taskqueue_sid)
print(taskqueue.friendly_name)