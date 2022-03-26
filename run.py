import sys
# from load_data import loadData
from eventcalendar.app import app

if __name__=="__main__":
	# if len(sys.argv) == 2:
	# 	if sys.argv[1] == 'insert_test_data':
	# 		loadData('instance/loadData')
	# else:
		app.run(debug=True)


	# export FLASK_DEBUG=1 

