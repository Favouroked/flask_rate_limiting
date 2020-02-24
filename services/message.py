from twilio.rest import Client

from common.config import ACCOUNT_SID, AUTH_TOKEN, TWILIO_NUMBER

client = Client(ACCOUNT_SID, AUTH_TOKEN)


def send_sms(data):
    for phone in data['to']:
        message = client.messages.create(
            from_=TWILIO_NUMBER,
            to=phone,
            body=data['message']
        )
        print(f'=====> Sent message to :> {phone} || Sid: {message.sid}')
