from flask import Flask, request, jsonify
from sms_service import send_sms
from unlock_logic import get_unlock_steps
import random

app = Flask(__name__)

@app.route("/send_otp", methods=["POST"])
def send_otp():
    data = request.json
    phone_number = data.get("phone_number")
    otp = str(random.randint(100000, 999999))
    
    if phone_number:
        send_sms(phone_number, otp)
        return jsonify({"message": "OTP sent successfully!", "otp": otp})
    return jsonify({"error": "Invalid phone number"}), 400

@app.route("/unlock_info", methods=["GET"])
def unlock_info():
    return jsonify({"message": get_unlock_steps()})

if __name__ == "__main__":
    app.run(debug=True)
