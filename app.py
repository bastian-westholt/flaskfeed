import json
from flask import Flask, render_template, request, redirect, url_for

with open('data/storage.json', 'r') as reader:
    blog_posts = json.loads(reader.read())

app = Flask(__name__)


@app.route('/')
def index():
    """Display all blog posts."""
    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    """Add a new blog post."""
    if request.method == 'POST':
        author = request.form.get('author')
        title = request.form.get('title')
        content = request.form.get('content')

        blog_posts.append({
            "id": len(blog_posts) + 1,
            "author": author,
            "title": title,
            "content": content
        })
        with open('data/storage.json', 'w') as writer:
            writer.write(json.dumps(blog_posts))

        return redirect(url_for('index'))

    return render_template('add.html')


@app.route('/delete/<int:post_id>')
def delete(post_id):
    """Delete a blog post by ID."""
    for i, post in enumerate(blog_posts):
        if post['id'] == post_id:
            blog_posts.remove(blog_posts[i])
            with open('data/storage.json', 'w') as writer:
                writer.write(json.dumps(blog_posts))

            return redirect(url_for('index'))

    return f'Post with that id: {post_id}, do not exist.'


def fetch_post_by_id(post_id):
    """Fetch a post by its ID."""
    for post in blog_posts:
        if post['id'] == post_id:
            return post
    return None


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    """Update an existing blog post."""
    current_post = fetch_post_by_id(post_id)

    if current_post is None:
        return "Post not found", 404

    if request.method == 'POST':
        current_post['author'] = request.form.get('author')
        current_post['title'] = request.form.get('title')
        current_post['content'] = request.form.get('content')

        with open('data/storage.json', 'w') as writer:
            writer.write(json.dumps(blog_posts))

        return redirect(url_for('index'))

    return render_template('update.html', post=current_post)


@app.route('/like/<int:post_id>', methods=['POST'])
def like(post_id):
    """Increment like count for a post."""
    current_post = fetch_post_by_id(post_id)

    if request.method == 'POST':
        current_post['likes'] += 1

        with open('data/storage.json', 'w') as writer:
            writer.write(json.dumps(blog_posts))

        return redirect(url_for('index'))

    return render_template('index.html', post=current_post)


@app.errorhandler(404)
def page_not_found(error):
    """Handle 404 errors."""
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def internal_server_error(error):
    """Handle 500 errors."""
    return render_template('errors/500.html'), 500


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=False)
