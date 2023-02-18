from flask import Flask, render_template, request, redirect
from user import User

app = Flask(__name__)

@app.route('/')
def read():
    users = User.get_all()
    return render_template('read.html', users=users)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email']
        }
        User.save(data)
        return redirect('/')
    else:
        return render_template('create.html')

if __name__ == '__main__':
    app.run(debug=True)
