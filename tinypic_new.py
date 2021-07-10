import tinify
import argparse
import sys

"""
User Input
"""
if len(sys.argv) != 5:
	print('\nUsage: -S <ORIGINAL FILE> -O <OUTPUT FILENAME>')
	print('e.g. python3 -S abc.png -O abc_compressed.png')
	exit()

my_parser = argparse.ArgumentParser(description='Compress picture with TinyPNG API')
my_parser.add_argument('-S', '--source-file', type=str, dest='SOURCE',help="Input the original picture you want to compress.")
my_parser.add_argument('-O', '--dest-file',type=str, dest='DEST', help="Specify the location you want to save to.")
args = my_parser.parse_args()
source_file = args.SOURCE
dest_file = args.DEST


"""
Main Program
"""
def compress_image():
	try:
		with open(source_file, 'rb') as source:
			source_data = source.read()
			result_data = tinify.from_buffer(source_data).to_buffer()
			with open(dest_file, 'wb') as dst:
					dst.write(result_data)
					dst.close()
			source.close()
			
	except tinify.errors.AccountError:
		print('Invalid API Key.')
	except tinify.errors.ConnectionError:
		print('Please check your internet connection.')
	except tinify.errors.ClientError:
		print('File type is not supported.')

if __name__ == "__main__":
	API_KEY = "<API_KEY>"
	tinify.key = API_KEY
	compress_image()
