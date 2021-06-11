from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from wtforms import SubmitField,StringField
from wtforms.validators import DataRequired,Length,ValidationError

class ImageForm(FlaskForm):
    cell_img=FileField('Upload Cell Image',validators=[FileAllowed(['jpg','png'])])
    submit=SubmitField("Generate report")

