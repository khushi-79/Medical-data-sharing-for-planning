
account_sid = 'AC3d249e025558fc37178aac0b9c1f8fa7'
auth_token = '181c1d0edfaffdc2a753425b5a8be705'
from twilio.rest import Client
client = Client(account_sid, auth_token)

message = client.messages.create(
# body='Name : Ayushman Bharat Yojana: Required Document : Family members aadhar card Mobile number Ration card Domicile, etc. Last Date : No Last Date https://mera.pmjay.gov.in/search/login',
body= 'from yash ....This is for testing if sms feature is working for not',
from_='+12057079156',
to='+918866221613'
)


print("\nfrom msg.py")