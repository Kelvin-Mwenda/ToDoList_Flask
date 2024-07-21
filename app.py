#import os
#import sys

# Add the project root to the sys.path
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'website')))

from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
    