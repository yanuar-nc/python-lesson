""" Create all functions 

provides:
	response(data, status_code, status_message)

"""
def response(data, status_code=200, status_message=None):
	
	result = {
		'status': {
			'code': status_code,
			'message': status_message
		},
		'data': data,
	}

	return result