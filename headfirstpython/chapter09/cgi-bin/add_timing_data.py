import os
import time
import sys
import yate
import cgi

# print(yate.start_response("txt/plain"))
print(yate.start_response())
addr = os.environ['REMOTE_ADDR']
host = os.environ['REMOTE_HOST']
method = os.environ['REQUEST_METHOD']
cur_time = time.asctime(time.localtime())
print(host + ', ' + addr + ", " + cur_time + ": " + method, end='<br>')

form = cgi.FieldStorage()
for each_form_item in form.keys():
    print (each_form_item + "->" + form[each_form_item].value, end='', file=sys.stderr)
print(file=sys.stderr)
print('OK', end='\n')