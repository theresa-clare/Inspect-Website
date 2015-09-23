import requests

def is_valid_url(url):
	if url is None:
		return None, None

	try:
		response = requests.get(url)
		if response.status_code == requests.codes.ok:
			response_html = response.text
			return True, response_html
		return False, None
	except requests.exceptions.ConnectionError:
		return False, None