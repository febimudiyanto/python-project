from flask import Flask, request, redirect, render_template

app = Flask(__name__)

# In-memory storage of snippets (reset on every restart)
snippets = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        content = request.form.get("content")
        if content:
            snippets.append(content)
        return redirect("/")
    return render_template("index.html", snippets=snippets)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
