# Get twilio-ruby from twilio.com/docs/ruby/install
require 'twilio-ruby'

# Get your Account Sid and Auth Token from twilio.com/user/account
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'

# Initialize Twilio Client
@client = Twilio::REST::Client.new(account_sid, auth_token)

# Get the accounts with the given sid
@accounts = @client.api.v2010.accounts(account_sid)

# Get all available phone numbers that contain the string `STORM`
@numbers = @accounts.available_phone_numbers('US').local
                    .list(contains: 'STORM')

# Get the first number
@number = @numbers[0].phone_number

# Purchase the number
@accounts.incoming_phone_numbers.create(phone_number: @number)
