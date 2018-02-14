from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import os
import subprocess


# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
 
class ReusableForm(Form):
    vpc = TextField('Vpc:', validators=[validators.required()])
    ec2_ami = TextField('Ec2Ami:', validators=[validators.required(), validators.Length(min=8, max=15)])
    ec2_type = TextField('Ec2Type:', validators=[validators.required(), validators.Length(min=5, max=15)])
 
 
@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
 
    print form.errors
    if request.method == 'POST':
        vpc=request.form['vpc']
        ec2_ami=request.form['ec2_ami']
        ec2_type=request.form['ec2_type']
        print vpc, " ", ec2_ami, " ", ec2_type
 
        if form.validate():
            # Save the comment here.
	    command='python generate_json.py --vpc='+str(vpc)+' --ami='+str(ec2_ami)+' --type='+str(ec2_type)
	    print command
            #flash(os.system(command))

	    proc = subprocess.Popen(command ,stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
	    json = str(proc.communicate()[0])


	    #json=os.system(command)
	    print "============================================3463463456================================================"
	    print json
	    print "============================================3463463456================================================"	    
	    #flash("TEST comapleted " + command)
	    flash(str(json))
        else:
            flash('Error: All the form fields are required. ')
 	
	#os.system('python generate_json.py')

    return render_template('hello.html', form=form)

if __name__ == "__main__":
    app.run()
