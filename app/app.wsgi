#!/root/anaconda3/bin/python
import logging
import sys

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/home/www/commandcenterbatu")
#sys.path.insert(1, "/home/www/commandcenterbatu/venv/lib/python3.9/site-packages")

# from app import monitor

# monitor.start(interval=1.0)
# monitor.track(os.path.join(os.path.dirname(__file__), 'site.cf'))

from app import app as application

sys.stdout = sys.stderr
application.secret_key = 'Rez4Y0g4sW@Ra!'
application.debug = True

'''
def application(environ, start_response):
    status = '200 OK'

    if not environ['mod_wsgi.process_group']:
        output = u'EMBEDDED MODE'
    else:
        output = u'DAEMON MODE'

    response_headers = [('Content-Type', 'text/plain'),
                        ('Content-Length', str(len(output)))]

    start_response(status, response_headers)

    return [output.encode('UTF-8')]
'''
# application.secret_key = 'Add your secret key'
