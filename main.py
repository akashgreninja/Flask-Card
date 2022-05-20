from flask import Flask, render_template
from post import Post


post=Post()
wadu=post.get_json()
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html",wadu=wadu)


@app.route("/post/<num>")
def page_1(num):
    return render_template("post.html",param=num,wadu=wadu)







if __name__ == "__main__":
    app.run(debug=True)
