# Log types.
DEBUG = 'DEBUG' # Used for general information.
INFO = 'INFO' # Used for odd cases.
WARNING = 'WARNING' # Used for problems that do not halt the system.
ERROR = 'ERROR' # Used for problems that halt the system.

# the default log value for string logs
MESSAGE = 'MESSAGE'

# The current logging level. Any errors below this level will not be logged.
LOG_LEVEL = INFO

# format string to user for client logger.
LOG_FORMAT = '[%(asctime)s]: %(message)s'

# file to use for client logger
from config import LOG_FILE

import traceback
import logging

class logger(object):
	'''
	Logger singleton to log all client side information
	'''
	__initialized = False
	__logger = None
	__handler = None
	__formatter = None

	def __init__(self):
		'''
		Initialize logging objects
		'''
		if not logger.__initialized:
			logger.__initialized = True
			logger.__logger = logging.getLogger()
			logFile = LOG_FILE
			logger.__handler = logging.FileHandler(logFile)
			logger.__formatter = logging.Formatter(LOG_FORMAT)
			logger.__handler.setFormatter(logger.__formatter)
			logger.__logger.addHandler(logger.__handler)
			logger.__logger.setLevel(logging.INFO)

	def info(self, message):
		'''
		Log an 'info'.
		'''
		logger.__logger.info(message)

def log(type, input, trace = ''):
	'''
	Produce a local log for debugging and info. Local logs are possible in
	command mode but not in service mode.
	'''
	# get a dictionary from the input
	inDict = getInputDict (input)

	# log everything to a file for now, if we have a string.
	logger().info (str(input))

	# also print everything for now...
	print str(input)

def debug(input = None):
	'''
	Log a debug message. Used for general information.
	'''
	log(DEBUG, input)

def info(input = None):
	'''
	Log an info message.
	'''
	log(INFO, input)

def warning(input = None):
	'''
	Log a warning message.
	'''
	log(WARNING, input)

def error(input = None):
	'''
	Log a error message.
	'''
	# Get the error trace.
	trace = traceback.format_exc()

	# if there is no input, use the trace
	if input == None:
		input = trace

	# Log the error.
	log(ERROR,input,trace)

def getInputDict (input):
	'''
	Get an input of unknown type and return a dictionary that can be logged.
	'''
	if isinstance(input, str) == True:
		# if it's a string input, create a dictionary containing one string message.
		inDict = {}
		inDict[MESSAGE] = input
	elif isinstance(input, dict) == True:
		# otherwise, just use the input dictionary.
		inDict = input
	else:
		inDict = {}

	return inDict
