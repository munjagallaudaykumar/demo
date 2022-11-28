from twilio.rest import Client
import keys

client = Client(keys.account_sid,keys.auth_token)

try:
	client.messages.create(from_=keys.from_number,
                       to=keys.to_number,
                       body='hello wellcome to StudentManagement system')
except:
	print("Unable to send unverified numbers need to purchase..")

