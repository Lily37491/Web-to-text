from flask import Flask, render_template, request, url_for
import trafilatura
import csv
import textwrap

app = Flask(__name__)

# Define the maximum width for text wrapping
max_width = 80

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/extract_text', methods=['POST'])
def extract_text():
    url = request.form['url']
    download = trafilatura.fetch_url(url)
    text = trafilatura.extract(download)
    return render_template('display_text.html', text=text)

if __name__ == '__main__':
    app.run(debug=True)
