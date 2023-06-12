from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)
print(__name__)

@app.route("/")
def myport():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_csv(data):
    with open('data.csv',mode='a') as database2:
        name=data['Name']
        email=data['Email']
        message=data['Message']
        csv_writer=csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,message])
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method =='POST':
        data=request.form.to_dict()
        write_to_csv(data)
        return redirect("/thanku.html")
    else:
        return 'nooooooooooooo'

