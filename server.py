from flask import Flask, render_template, request, redirect
from is_valid_url import is_valid_url

app = Flask(__name__)
app.secret_key = "iLoveSlack"


@app.route('/', methods=['GET', 'POST'])
def homepage(url=None):
	if request.method == 'POST':
		url = request.form['url']

		if url[:8] != "http://" or url[:9] != "https://":
			url = "http://" + url
			msg = ""

		if not is_valid_url(url):
			url = ""
			msg = "Please enter a valid URL"

		return render_template('homepage.html', url=url, msg=msg)

	else:
		return render_template('homepage.html')


if __name__ == "__main__":
	app.run(debug=True)