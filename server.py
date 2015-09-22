from flask import Flask, render_template, request, redirect
from is_valid_url import is_valid_url
from get_tags_and_count import get_tags_and_count
import re

app = Flask(__name__)
app.secret_key = "iLoveSlack"


@app.route('/', methods=['GET', 'POST'])
def homepage(url=None):
	if request.method == 'POST':
		url = request.form['url']

		if url[:8] != "http://" or url[:9] != "https://":
			url = "http://" + url
			msg = ""

		is_valid, source_code = is_valid_url(url)

		if not is_valid:
			url = ""
			msg = "Please enter a valid URL"
			source_code = ""

		# source_code_transformed = transform_html(source_code)
		tags_and_count = get_tags_and_count(source_code)
		print tags_and_count
		return render_template('homepage.html', url=url, msg=msg, source_code=source_code)

	else:
		return render_template('homepage.html')


# def transform_html(source_code):
# 	res = re.sub(r'<(/?)(\S+)(.*?)>', r'<div class="\2">&lt;\1\2\3&gt;</div>', source_code)
# 	res = res.replace('\n', " ")
# 	return res.replace("'" , '"')


if __name__ == "__main__":
	app.run(debug=True)