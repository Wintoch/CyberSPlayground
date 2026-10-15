from flask import Flask, redirect

def redirection(sitename):
    app = Flask(__name__)
    @app.route('/', defaults={'path':''})
    @app.route('/<path:path>')
    def catchAll(path):
        return redirect(sitename, code=302)

    app.run('0.0.0.0', port=80)
        
#'http://http.badssl.com'