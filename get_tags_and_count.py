from lxml import html

def get_tags_and_count(source_code):
	"""
	Given a string of html, returns a dictionary with tags as keys and the
	number of times it appears as its value; otherwise, returns None.
	
	>>> import requests
	>>> page = requests.get("http://www.theresacay.com")
	>>> get_tags_and_count(page.text)
	{'p': 7, 'h2': 4, 'h3': 4, 'h1': 1, 'h4': 30, 'meta': 2, 'span': 23, 'img': 9, 'script': 4, 'li': 5, 'html': 1, 'nav': 1, <built-in function Comment>: 1, 'body': 1, 'head': 1, 'hr': 20, 'link': 5, 'br': 1, 'a': 12, 'title': 1, 'ul': 1, 'div': 35}

	>>> get_tags_and_count("")

	"""
	try:
		tree = html.fromstring(source_code)
	except:
		tree = None

	tags_and_count = {}

	if tree is None:
		return None

	for element in tree.iter():
		tags_and_count[element.tag] = tags_and_count.get(element.tag, 0) + 1

	return tags_and_count

#################################################################################

if __name__ == "__main__":
	import doctest
	doctest.testmod()