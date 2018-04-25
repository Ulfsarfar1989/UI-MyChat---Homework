from flask import Flask, render_template, flash, request, url_for, redirect

app = Flask(__name__)


@app.route('/chat/')
def chat():
    return render_template('chat.html')


@app.route('/login/', methods=["GET", "POST"])
def login_page():
    error = ''
    try:
        if request.method == "POST":
            attempted_username = request.form['username']
            attempted_password = request.form['password']

            flash(attempted_username)
            flash(attempted_password)

            if attempted_username == "admin" and attempted_password == "pass":
                return redirect(url_for('chat'))
            else:
                error = "Invalid credentials. Try again."

        return render_template("login.html", error=error)

    except Exception as e:
        flash(e)
        return render_template("login.html", error=error)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
