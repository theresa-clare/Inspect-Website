from lxml import html

def get_tags_and_count(source_code):
	"""
	Given a string of html, returns a dictionary with tags as keys and the
	number of times it appears as its value; otherwise, returns None.
	
	>>> import requests
	>>> page = requests.get("http://www.theresacay.com")
	>>> get_tags_and_count(page.text)
	{'body': 1, 'a': 12, 'head': 1, 'h1': 1, 'span': 23, 'img': 9, 'script': 4, 'h2': 4, 'h3': 4, 'meta': 2, 'h4': 30, 'li': 5, 'hr': 20, 'ul': 1, 'html': 1, 'link': 5, 'br': 1, 'title': 1, 'div': 35, 'nav': 1, 'p': 7}

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
		if isinstance(element, html.HtmlElement):
			tags_and_count[element.tag] = tags_and_count.get(element.tag, 0) + 1

	return tags_and_count

#################################################################################

if __name__ == "__main__":
	import doctest
	doctest.testmod()