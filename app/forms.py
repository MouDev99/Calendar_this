from flask_wtf import FlaskForm
from wtforms import (
    StringField, DateField, TimeField, TextAreaField, BooleanField, SubmitField
)
from wtforms.validators import DataRequired, ValidationError
from datetime import datetime

class AppointmentForm(FlaskForm):
    name = StringField("Name")
    start_date = DateField("Start date", validators=[DataRequired()])
    start_time = TimeField("Start time", validators=[DataRequired()])
    end_date = DateField("End date", validators=[DataRequired()])
    end_time = TimeField("End time", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    private = BooleanField("Private?")
    submit = SubmitField("create an appointment")

    def validate_end_date(form, field):
        start = datetime.combine(form.start_date.data, form.start_time.data)
        end = datetime.combine(form.end_date.data, form.end_time.data)

        if start >= end:
            raise ValidationError("End date/time must come after start date/time")
