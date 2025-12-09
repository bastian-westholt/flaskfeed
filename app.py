import json
from flask import Flask, render_template, request, redirect, url_for

with open('data/storage.json', 'r') as reader:
    blog_posts = json.loads(reader.read())

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', posts=blog_posts)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        author = request.form.get('author')
        title = request.form.get('title')
        content = request.form.get('content')

        blog_posts.append({"id": len(blog_posts)+1, "author": author, "title": title, "content": content})
        with open('data/storage.json', 'w') as writer:
            writer.write(json.dumps(blog_posts))

        return redirect(url_for('index'))

    return render_template('add.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)