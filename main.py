import time
from notification import notification_popup
from get_quotes import fetch_quote


while True:

	quote = fetch_quote()
	title = "Hey! Please Drink Water."
	notification_popup(title,quote)

	time.sleep(10)




