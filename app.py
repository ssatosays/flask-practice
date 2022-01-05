from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'secret_key'


@app.route('/')
def index():
    session["country"] = "japan"
    session["prefecture"] = "chiba"
    return render_template('index.html')

@app.route('/has-session')
def has_session():
    if "country" not in session:
        return redirect(url_for("index"))
    if "prefecture" not in session:
        return redirect(url_for("index"))
    print("---- debug")
    print(session)
    print("---- debug")
    return session["country"] + "/" + session["prefecture"]


if __name__ == '__main__':
    app.run(debug=True, port=8080)
