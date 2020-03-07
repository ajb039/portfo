from flask import Flask, render_template, request, send_from_directory, redirect, url_for
import os
import csv


app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
	return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)
 
def write_to_file(data):
	try:
		with open("database.txt", mode='a') as outFile:
			username = data['username']
			email = data['email']
			subject = data['subject']
			message = data['message']
			outFile.write(f'\n{username},{email},{subject},{message}')
		# Do something with the file
	except (FileNotFoundError, IOError):
		print("File not accessible")
	finally:
		outFile.close()
		print('File has closed')
	

def write_to_csv(data):
	try:
		with open("database.csv", mode='a',newline='') as outFile:
			username = data['username']
			email = data['email']
			subject = data['subject']
			message = data['message']
			csv_writer = csv.writer(outFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
			csv_writer.writerow([username,email,subject,message])
		# Do something with the file
	except (FileNotFoundError, IOError):
		print("File not accessible")
	finally:
		outFile.close()
		print('file has closed')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			#write_to_file(data)
			write_to_csv(data)
			#print(data)
			return redirect('thankyou.html')
		except:
			return 'Did not save to database'		
	else:
		return 'something went wrong'


