from flask import Flask, render_template, request, redirect
from user import User

app = Flask(__name__)

# Index page shows all users
@app.route('/')
def index():
    users = User.get_all()
    return render_template('read.html', users=users)

# Show page shows one user
@app.route('/users/<int:id>')
def show(id):
    user = User.get_by_id(id)
    return render_template('show.html', user=user)

# Edit page shows a form to edit a user
@app.route('/users/<int:id>/edit')
def edit(id):
    user = User.get_by_id(id)
    return render_template('edit.html', user=user)

# Update action updates a user in the database
@app.route('/users/<int:id>', methods=['POST'])
def update(id):
    data = {
        'id': id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.save(data)
    return redirect('/users/{}'.format(id))

# Delete action deletes a user from the database
@app.route('/users/<int:id>/delete', methods=['POST'])
def delete(id):
    User.delete(id)
    return redirect('/')

# Create page shows a form to create a user
@app.route('/users/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email']
        }
        id = User.save(data)
        return redirect('/')
    else:
        return render_template('create.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
