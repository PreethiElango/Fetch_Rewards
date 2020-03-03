from flask import Blueprint
from flask import request
from validate_email import validate_email

home_view = Blueprint('home_view', __name__)

@home_view.route('/', methods = ['POST'])  # Route for the page
def display_home_page():
	if request.is_json:
		emails = request.get_json()['emails']
		processed = []
		for i in emails:
			if validate_email(i):
				s = i.split('@')
				temp = s[0].split('+', 1)[0]
				temp = temp.replace('.', '')
				s[0] = temp
				s = s[0] + '@' + s[1]
				processed.append(s)

		k = set(processed)
		return {"unique_count":len(k)}
	else:
		return {"error": "Please send the data in JSON format"}