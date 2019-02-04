from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('signin_form.html')


@app.route('/', methods=['POST', 'GET'])
def user_signin():

    username = request.form['un']
    password = request.form['pw']
    verify_password = request.form['vpw']
    email = request.form['e']

    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''

    if len(username) > 20 or len(username) < 3:
        username_error = "Usernames must be within 3-20 characters."
    else:
        for char in username:
            if char == ' ':
                username_error = "Usernames can not contain a space character."

    if len(password) > 20 or len(password) < 3:
        password_error = "Passwords must be within 3-20 characters."
    else:
        for char in password:
            if char == ' ':
                password_error = "Passwords can not contain a space character."

    if verify_password != password:
        verify_password_error = "Passwords must match."

    if len(email) != 0:
        if len(email) > 20 or len(email) < 3:
            email_error = "Emails must be within 3-20 characters."
        else:
            for char in email:
                if char == ' ':
                    email_error = "Emails can not contain a space character."

    if not username_error and not password_error and not verify_password_error and not email_error:
        return redirect('/welcome?username={0}'.format(username))

    else:
        return render_template('signin_form.html', username_error=username_error, password_error=password_error, verify_password_error=verify_password_error, email_error=email_error)


@app.route('/welcome')
def valid_time():
    username = request.args.get('username')
    return '''<h1>Welcome, {}!</h1>'''.format(username)


app.run()
