from wtforms import FileField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Regexp
from flask_wtf.file import FileAllowed


# Form to submit a .jpg or .png file only
class ImageSubmission(FlaskForm):
    image = FileField(
        "Upload Image",
        validators=[
            DataRequired(),
            FileAllowed(["jpg", "png"], "Only .jpg and .png files are allowed!")
        ],
    )
