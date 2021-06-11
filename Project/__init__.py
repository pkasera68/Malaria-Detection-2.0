from flask import Flask ,render_template

app=Flask(__name__)
app.config['SECRET_KEY'] ='2833b3c9901101b8a0c67eb76f7b70c5'

from Project import routes