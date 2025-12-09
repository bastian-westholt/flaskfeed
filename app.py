import json
from flask import Flask, render_template, request

with open('data/storage.json', 'r') as reader:
    blog_posts = json.loads(reader.read())



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', posts=blog_posts)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        pass
    return render_template('add.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)