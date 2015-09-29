from flask import Flask, render_template, request
from is_valid_url import is_valid_url
from get_tags_and_count import get_tags_and_count

app = Flask(__name__)
app.secret_key = "inspect_a_website"


@app.route('/', methods=['GET', 'POST'])
def homepage():
	if request.method == 'POST':
		url = request.form['url']

		if not url.startswith("http://") and not url.startswith("https://"):
			url = "http://" + url

		source_code, msg = is_valid_url(url)

		if source_code is None:
			url = ""
			source_code = ""

		tags_and_count = get_tags_and_count(source_code)

		return render_template('homepage.html', url=url, msg=msg, \
			source_code=source_code, tags_and_count=tags_and_count)
	else:
		return render_template('homepage.html', tags_and_count={})



if __name__ == "__main__":
	app.run(debug=True)