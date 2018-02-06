from wtforms import Form, \
					BooleanField, \
					StringField, \
					PasswordField, \
					DateTimeField, \
					validators

class Validator(Form):

	def get_error_messages(self):
		message = []
		return self.errors;
		# for field_name, error_messages in form_data:
		# 	for err in error_messages:
		# 		message.append(err)
		# return message

class ArticleForm(Validator):
	title = StringField('Title', [validators.Length(min=4, max=25)])
	content = StringField('Content', [validators.DataRequired()])
	post_date = DateTimeField('Date', [validators.DataRequired()])
