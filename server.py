from flask import Flask, render_template, request, redirect
import csv 

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>.html')
def html_page(page_name):
    return render_template(page_name)

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/paintings.html')
def paintings():
    return render_template('paintings.html')

@app.route('/trips.html')
def works():
    return render_template('trips.html')

@app.route('/thankyou.html')
def thankyou():
    return render_template('thankyou.html')

def write_to_file(data):
    with open('database.txt',mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subject}, {message}')
        
def write_to_csv(data):
    with open('database.csv',newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    try:
        if request.method == 'POST':
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
    except:
        return 'Ops! Something went wrong'
    else:
        return 'something went wrong'