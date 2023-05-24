from flask import Flask, render_template, request
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:@localhost/contact'
db = SQLAlchemy(app)



class Contact_info(db.Model): #CLASS NAME SHOULD BE THE SAME AS TABLE NAME
    #S.No,Phone_Number,Name
    S_No = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(80), unique=False, nullable=False)
    Phone_Number = db.Column(db.String(12), unique=True, nullable=False)

@app.route("/", methods = ['GET', 'POST'])
def contact():
    if(request.method=='POST'):
        '''ADD ENTRY TO THE DATABASE'''
        name = request.form.get('Name')
        phone = request.form.get('phone_number')

        entry = Contact_info(Name=name,Phone_Number=phone)
        db.session.add(entry)
        db.session.commit()
        return render_template('successful.html')
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0',port=5000)
