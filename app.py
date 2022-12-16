import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome to CS190B'


def main():
    '''The threaded option for concurrent accesses, 0.0.0.0 host says listen to all network interfaces 
    (leaving this off changes this to local (same host) only access, port is the port listened on
    -- this must be open in your firewall or mapped out if within a Docker container. 
    '''
    localport = int(os.getenv("PORT", 8000))
    app.run(threaded=True, host='0.0.0.0', port=localport)

if __name__ == '__main__':
    main()