from wtforms import Form, StringField, validators


class MainForm(Form):
    link = StringField('Link', [validators.Length(min=3, max=55), validators.Required(), validators.URL()])
