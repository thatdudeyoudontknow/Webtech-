from bungalowpark.models import User, Tent
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField, SelectField, DateTimeField, DateField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, Optional
from wtforms import ValidationError
from wtforms.validators import Regexp
from flask_login import current_user



class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Gebruikersnaam', validators=[DataRequired()])
    woonplaats = StringField('Woonplaats', validators=[DataRequired()])
    huisnummer = IntegerField('Huisnummer', validators=[DataRequired()])
    toevoeging = StringField('toevoeging')
    straat = StringField('Straat', validators=[DataRequired()])
    postcode = StringField('Postcode', validators=[DataRequired(), Regexp('^\d{4}[A-Za-z]{2}$', message='Ongeldige postcode!')])
    password = PasswordField('Wachtwoord', validators=[DataRequired(), EqualTo('pass_confirm', message='Wachtwoorden moeten gelijk zijn!')])
    pass_confirm = PasswordField('Bevestig uw wachtwoord', validators=[DataRequired()])
    submit = SubmitField('Registeren!')

    def validate_woonplaats(self, field):
        if not field.data.replace('.', '').replace('-', '').isalpha():
            raise ValidationError('Ongeldige woonplaats')

    def validate_straat(self, field):
        if not field.data.replace('.', '').replace('-', '').isalpha():
            raise ValidationError('Ongeldige straatnaam.')
    
    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Dit e-mailadres staat al geregistreerd!')
    
    def check_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Deze gebruikersnaam is al in gebruik, probeer een ander naam!')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Wachtwoord', validators=[DataRequired()])
    submit = SubmitField('Inloggen')

# class BoekingForm(FlaskForm):
#     tent = StringField('tent', validators=DataRequired)
#     startdatum =  StringField('startdatum', validators=[DataRequired()])
#     einddatum =  StringField('einddatum', validators=[DataRequired()])
#     submit = SubmitField('Boek NU!')

class BoekingForm(FlaskForm):
    tent = StringField('tent', validators=[DataRequired()])
    startdatum = StringField('startdatum', validators=[DataRequired()])
    einddatum = StringField('einddatum', validators=[DataRequired()])
    submit = SubmitField('Boek NU!')

    def validate_tent(self, field):
        tent_ids = [str(tent.id) for tent in Tent.query.all()]
        if field.data not in tent_ids:
            raise ValidationError('Ongeldige tent selectie')


class AccountUpdateForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Gebruikersnaam', validators=[DataRequired()])
    woonplaats = StringField('Woonplaats', validators=[DataRequired()])
    huisnummer = IntegerField('Huisnummer', validators=[DataRequired()])
    toevoeging = StringField('toevoeging')
    straat = StringField('Straat', validators=[DataRequired()])
    postcode = StringField('Postcode', validators=[DataRequired(), Regexp('^\d{4}[A-Za-z]{2}$', message='Ongeldige postcode!')])
    password = PasswordField('Wachtwoord', validators=[DataRequired(), EqualTo('pass_confirm', message='Wachtwoorden moeten gelijk zijn!')])
    pass_confirm = PasswordField('Bevestig uw wachtwoord', validators=[DataRequired()])
    submit = SubmitField('Registeren!')

    def validate_woonplaats(self, field):
        if not field.data.replace('.', '').replace('-', '').isalpha():
            raise ValidationError('Ongeldige woonplaats')

    def validate_straat(self, field):
        if not field.data.replace('.', '').replace('-', '').isalpha():
            raise ValidationError('Ongeldige straatnaam.')

    def check_email(self, field):
        user = User.query.filter_by(email=field.data).first()
        if user and user.id != current_user.id:
            raise ValidationError('Dit e-mailadres staat al geregistreerd!')

    def check_username(self, field):
        user = User.query.filter_by(username=field.data).first()
        if user and user.id != current_user.id:
            raise ValidationError('Deze gebruikersnaam is al in gebruik, probeer een andere naam!')

class wwupdateform(FlaskForm):
    password = PasswordField('Wachtwoord', validators=[DataRequired(), EqualTo('pass_confirm', message='Wachtwoorden moeten gelijk zijn!')])
    pass_confirm = PasswordField('Bevestig uw wachtwoord', validators=[DataRequired()])
    submit = SubmitField('Verzend')