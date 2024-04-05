from flask import Flask, render_template

app = Flask(__name__)

# Example blog posts
posts = [
    {
        'author': 'Author One',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 1, 2024'
    },
    {
        'author': 'Author Two',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 2, 2024'
    }
]

@app.route("/")
@app.route("/home")
def home():
    print ("Here from app.py")
    return render_template('index.html', posts=posts, content="This is a test.")

if __name__ == '__main__':
    app.run(debug=True)