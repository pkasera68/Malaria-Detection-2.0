from flask import Flask ,render_template

app=Flask(__name__)
#app.config['']

from Project import routes
