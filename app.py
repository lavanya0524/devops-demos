from flask import Flask,render_template

app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/welcome")
def welcome():
    return "welcome to Flask"

@app.route("/Login")
def Login():
    return render_template('Login.html')



@app.route("/register")
def register():
    return render_template('register.html')


if __name__=='__main__':
    app.run(debug=True)