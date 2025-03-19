from twilio.rest import Client

TWILIO_ACCOUNT_SID = "your_account_sid"
TWILIO_AUTH_TOKEN = "your_auth_token"
TWILIO_PHONE_NUMBER = "+1234567890"

def send_sms(phone_number, otp_code):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=f"Your verification code is: {otp_code}",
        from_=TWILIO_PHONE_NUMBER,
        to=phone_number
    )
    return message.sid
