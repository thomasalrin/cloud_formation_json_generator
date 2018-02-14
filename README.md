prerequisites 
=============

	pip install Flask

	pip install wtforms

	pip install flask-bootstrap

	pip install troposphere

Steps to run
------------

clone this repo 

	git clone https://github.com/thomasalrin/cloud_formation_json_generator.git

Go to the home directory of this repo

	cd cloud_formation_json_generator

run the code
	
	python hello.py


If it shows any dependency issue, install all the dependencies.
Thats it, application can be explored in browser with the below address,

	http://127.0.0.1:5000/


It will show a form, in which you need to enter vpcId, amiId(eg: `ami-79873901`) and ec2 instance type(eg: `t2.micro`).


After submitting the form, you can get `json` with a flsh message.

You can use the online json parser http://json.parser.online.fr/, to parse the json string.



