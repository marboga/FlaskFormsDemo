from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "aejksbtskh4tbk4jhsevgkjagcvkj4s3vkhfetkjfewv"

@app.route('/')
def index():
    print "in index route"
    return render_template('index.html')

@app.route('/process_form', methods=['POST'])
def process():
    print "processing form"
    print request.form
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    return redirect('/result')

@app.route('/result', methods=['GET'])
def result():
    try:
        print session['first_name']
    except KeyError:
        session['first_name'] = "Unknown User"  
    return render_template('result.html')




app.run(debug=True)