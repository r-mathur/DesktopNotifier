import http.client
import json


def fetch_quote():




	try:
		conn = http.client.HTTPSConnection("quote-garden.herokuapp.com")
		payload = ''
		headers = {}
		conn.request("GET", "/api/v3/quotes/random", payload, headers)
		res = conn.getresponse()
		data = res.read()
		result = data.decode("utf-8")  # this is response
		json_data = json.loads(result)

		status = json_data['statusCode']

	except Exception as e:		
		status = 420    # if internet is not working or active
	else:
		pass
	


	quote = ""


	if status == 200:		# if everithing works fine

		data = json_data['data'][0]['quoteText']

		author =  json_data['data'][0]['quoteAuthor']

		quote = data + " - By : "+author

		return quote
		


	else:			

		quote = "Hey! I need internet connection to boost you with some Quotes"

		return quote 
	

