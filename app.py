from flask import Flask, session, render_template, request, redirect, flash
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error_message = None  # Initialize error message as None
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

       
    return render_template("signup.html", error_message=error_message)



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        age = request.form['age']
        gender = request.form.get('gender')
        email = request.form['email']
        address = request.form['address']
        password = request.form['password']
        confirmpassword = request.form['confirmpassword']
        pastconditions = request.form['pastconditions']

        # Check if all required fields are filled
        if not firstname or not lastname or not age or not gender or not email or not address or not password or not confirmpassword or not pastconditions:
            return "Please fill all the required fields"

        # Check if passwords match
        if password != confirmpassword:
            return "check your passwords again"



        try:
            return render_template('index.html')
        except:
            existing_account1 = 'This email is already used'
            return render_template('index.html', exist_message=existing_account1)

    return render_template("register.html")

@app.route('/service')
def service():
    # Check if user is logged in by checking if email is stored in session
    if 'email' in session:
        return render_template("service.html")
    else:
        # User is not logged in, redirect to signup page
        flash('Please sign up to access the service.')
        return redirect('/signup')


if __name__ == '__main__':
    app.run()
