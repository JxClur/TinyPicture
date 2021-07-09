import tinify
import sys

API_KEY = "<API KEY>"
tinify.key = API_KEY

try:
	with open(sys.argv[1], 'rb') as source:
		source_data = source.read()
		result_data = tinify.from_buffer(source_data).to_buffer()
		with open(sys.argv[2], 'wb') as dst:
				dst.write(result_data)
				dst.close()
		source.close()
		
except tinify.errors.AccountError:
	print('Invalid API Key.')
except tinify.errors.ConnectionError:
	print('Please check your internet connection.')
except tinify.errors.ClientError:
	print('File type is not supported.')
