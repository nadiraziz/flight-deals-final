from twilio.rest import Client
import smtplib
account_sid = "ACcf5b9ee7e3c0d76bcd8477bd41efc644"
auth_token = "ef6377aa349267659613c52173e73983"


class NotificationManager:

    def __init__(self):
        self.client =  Client(account_sid, auth_token)

    def send_sms(self, message):
        message = self.client.messages \
            .create(
            body=message,
            from_='+17632251469',
            to='+919995957505'
        )
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(EMAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr="nadiraziziyah@gmail.com",
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )




