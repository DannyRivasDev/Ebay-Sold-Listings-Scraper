from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_link', methods=['POST'])
def process_link():
    search_link = request.form['search_link']
    result = subprocess.check_output(['python3', 'ebay_sold_listings.py', search_link]).decode('utf-8')
    return result

if __name__ == '__main__':
    app.run(debug=True)
