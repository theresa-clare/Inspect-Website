import requests

def is_valid_url(url):
	"""
	Checks if URL is valid. Returns tuple of response html and message.
	"""
	if url is None:
		return None, "URL is None"

	try:
		response = requests.get(url)
		if response.status_code == requests.codes.ok:
			response_html = response.text
			return response_html, ""
		else:
			return None, "Please check your URL once more"
	except requests.exceptions.URLRequired: 
		return None, "A valid URL is required to make a request"
	except requests.exceptions.ConnectionError: # DNS failures
		return None, "Please enter a valid URL"
	except requests.exceptions.HTTPError as e:
		return None, "An HTTP error occurred: %s" % e.message
	except requests.exceptions.ConnectTimeout:
		return None, "The request timed out while trying to connect. Please try again."
	except:
		return None, "An unexpected error occurred"