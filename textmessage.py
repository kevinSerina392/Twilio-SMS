from twilio.rest import Client

account_sid = 'AC518b5df10c8345ae3e50c496308c3dc0'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
    messaging_service_sid='MGd46cdf9f2cbb32b2ef15d475780006aa',
    body='Sending this message from my Python program using Twilio!',
    to='+(Phone Number)'
)

print(message.sid)
