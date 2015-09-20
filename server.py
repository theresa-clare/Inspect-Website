from flask import Flask, render_template, request, flash, redirect

app = Flask(__name__)
app.secret_key = "iLoveSlack"


@app.route('/')
def index():
	return render_template('homepage.html')


if __name__ == "__main__":
	app.run(debug=True)