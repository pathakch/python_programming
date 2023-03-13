import logging

logging.basicConfig(filename = 'demo.log',filemode='w')

logging.debug('this is a debug message')
logging.info('this is a information message')
logging.warning('this is a warning message')
logging.error('This is an Error message')
logging.critical('This is a critical message')

"""
Output :-->> (There is no output as such , one log file is generated here, this is just to understand the 
working of code)

demo.log file content :
WARNING:root:this is a warning message
ERROR:root:This is an Error message
CRITICAL:root:This is a critical message

Explanation :-->>
we can see that there are only three messages logged in 'demo.log' file bcz
we have not defined any level while calling 'basicConfig' (line 3)and 
the default level in logging is 'warning'  so its printing all the messages after 'warning'
this is working according to level hierarchy defined in module 'logging' 

We can see that there is no format in the messges written in demo.log file 
to provide required formt we can use 'format' parameter while calling basicConfig function 
like : format = "%(asctime)s - "

Exxplanation about 'root' in messages written:
This 'root' is a default logger in logging module 
since we have not defined our own logger that's why here default logger is 'root'
we will  
"""

"""
***************************************** Define our own logger *******************************
There is a problem with 'root' logger (explained above )that's why we will define our own root logger
"""
# creating logger
logger = logging.getLogger(__name__)
# setting logger level
logger.setLevel(logging.DEBUG) # here we can set any level not only 'DEBUG'
# setting format
fmt = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
# setting file : or this need to create a file handler
file_handler = logging.FileHandler('file_name')
#setting fomatter in file handler
file_handler.setFormatter(fmt)
# adding file handler to the logger 
logger.addHandler(file_handler)
# All set now , in place of logging everywhere in our code we need to write 'logger'