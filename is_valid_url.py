import requests

def is_valid_url(url):
	"""
	Given a string, returns True if string is a valid URL; returns False otherwise
	
	>>> is_valid_url("http://www.facebook.com")
	True

	>>> is_valid_url("http://facebook.com")
	True

	>>> is_valid_url("http://thisisnotaurl")
	False

	>>> is_valid_url("http://www.alsonotavalidurl.com")
	False
	"""
	if url is None:
		return None

	try:
		response = requests.get(url)
		if response.status_code == requests.codes.ok:
			return True
		return False
	except requests.exceptions.ConnectionError:
		return False

#################################################################################

if __name__ == "__main__":
	import doctest
	doctest.testmod()