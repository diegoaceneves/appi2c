from appi2c.ext.device.device_models import Device
from flask_wtf import FlaskForm
from wtforms import (StringField,
                     SubmitField,
                     SelectField,
                     IntegerField)
from wtforms.validators import InputRequired, Length, ValidationError
from wtforms_sqlalchemy.fields import QuerySelectField
from appi2c.ext.group.group_controller import choice_query
from flask_login import current_user
from wtforms.widgets import HiddenInput


def validator_data_select(form, field):
    if field.data is None:
        raise ValidationError('Select an option')


def validator_topic(form, field):
    if len(field.data) > 120:
        raise ValidationError('Max 120 digits')
    if '/' not in field.data:
        raise ValidationError('Invalid topic')


def validator_topic_not_imput(form, field):
    if len(field.data) > 0:
        if len(field.data) > 120:
            raise ValidationError('Max 120 digits')
        if '/' not in field.data:
            raise ValidationError('Invalid topic')
    else:
        pass


class DeviceSwitchForm(FlaskForm):
    groups = QuerySelectField('Group', validators=[InputRequired(), validator_data_select], query_factory=choice_query, get_label='name')
    name = StringField('Name', validators=[InputRequired(), Length(min=5, max=60, message=('Max 60 digits'))])
    topic_pub = StringField('Topic Publish', validators=[InputRequired(), validator_topic])
    last_will_topic = StringField('Topic Last Will', validators=[validator_topic_not_imput])
    command_on = StringField('On Command', validators=[InputRequired(), Length(max=60, message=('Max 60 digits'))])
    command_off = StringField('Off Command', validators=[InputRequired(), Length(max=60, message=('Max 60 digits'))])
    qos = SelectField("Qos", choices=[(0, 0), (1, 1), (2, 2)], validators=[InputRequired()])
    retained = SelectField('Retained', choices=[(False, False), (True, True)], default=True)
    icon_id = IntegerField('icon_id', default=1)
    submit = SubmitField('Insert')

    def validate_name(self, name):
        device = Device.query.filter_by(name=name.data).filter_by(user_id=current_user.id).first()
        if device is not None:
            raise ValidationError('Please use a different device name.')


class DeviceSensorForm(FlaskForm):
    groups = QuerySelectField('Group', validators=[InputRequired(), validator_data_select], query_factory=choice_query, get_label='name')
    name = StringField('Name', validators=[InputRequired(), Length(min=1, max=60, message=('Max 60 digits'))])
    topic_sub = StringField('Topic Subscrib', validators=[InputRequired(), validator_topic])
    measure = StringField('Measure', validators=[Length(min=3, max=60, message=('Min 3 and Max 60 digits'))])
    postfix = StringField('Postfix', validators=[Length(max=3, message=('Max 3 digits'))])
    last_will_topic = StringField('Topic Last Will', validators=[validator_topic_not_imput])
    qos = SelectField("Qos", choices=[(0, 0), (1, 1), (2, 2)], validators=[InputRequired()])
    icon_id = IntegerField('icon_id')
    submit = SubmitField('Insert')

    def validate_name(self, name):
        device = Device.query.filter_by(name=name.data).filter_by(user_id=current_user.id).first()
        if device is not None:
            raise ValidationError('Please use a different device name.')


class EditSwitchForm(FlaskForm):
    id = IntegerField(widget=HiddenInput())
    groups = QuerySelectField('Group', validators=[InputRequired(), validator_data_select], query_factory=choice_query, get_label='name')
    name = StringField('Name', validators=[InputRequired(), Length(max=60, message=('Max 60 digits'))])
    topic_pub = StringField('Topic Publish', validators=[InputRequired(), validator_topic])
    last_will_topic = StringField('Topic Last Will', validators=[validator_topic_not_imput])
    command_on = StringField('On Command', validators=[InputRequired(), Length(max=60, message=('Max 60 digits'))])
    command_off = StringField('Off Command', validators=[InputRequired(), Length(max=60, message=('Max 60 digits'))])
    qos = SelectField("Qos", choices=[(0, 0), (1, 1), (2, 2)], validators=[InputRequired()], default=0)
    retained = SelectField('Retained', validators=[InputRequired(), validator_data_select], choices=[("False", False), ("True", True)])
    icon_id = IntegerField('icon_id')

    submit = SubmitField('Confirm')

    def validate_name(self, name):
        device = Device.query.filter_by(name=name.data).filter_by(user_id=current_user.id).first()
        if device is not None:
            if self.id.data != device.id:
                raise ValidationError('Please use a different device name.')


class EditSensorForm(FlaskForm):
    id = IntegerField(widget=HiddenInput())
    groups = QuerySelectField('Group', validators=[InputRequired(), validator_data_select], query_factory=choice_query, get_label='name')
    name = StringField('Name', validators=[InputRequired(), Length(max=60, message=('Max 60 digits'))])
    topic_sub = StringField('Topic Subscrib', validators=[InputRequired(), validator_topic])
    measure = StringField('Measure', validators=[Length(min=3, max=60, message=('Min 3 and Max 60 digits'))])
    postfix = StringField('Postfix', validators=[Length(max=10, message=('Max 10 digits'))])
    last_will_topic = StringField('Topic Last Will', validators=[validator_topic_not_imput])
    qos = SelectField("Qos", choices=[(0, 0), (1, 1), (2, 2)], validators=[InputRequired()])
    icon_id = IntegerField('icon_id')

    submit = SubmitField('Confirm')

    def validate_name(self, name):
        device = Device.query.filter_by(name=name.data).filter_by(user_id=current_user.id).first()
        if device is not None:
            if self.id.data != device.id:
                raise ValidationError('Please use a different device name.')
