from twilio.rest import Client

account_sid = "ACcf5b9ee7e3c0d76bcd8477bd41efc644"
auth_token = "ef6377aa349267659613c52173e73983"


class NotificationManager:

    def __init__(self):
        self.client = client = Client(account_sid, auth_token)

    def send_sms(self, message):
        message = self.client.messages \
            .create(
            body=message,
            from_='+17632251469',
            to='+919995957505'
        )
        print(message.sid)




