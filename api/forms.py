from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class AddAirlineForm(FlaskForm):
    name = StringField("Airline name")
    submit = SubmitField("Add")


class DeleteAirlineForm(FlaskForm):
    name = StringField("Airline name")
    submit = SubmitField("Delete")


class HubAirlineForm(FlaskForm):
    airline_name = StringField("Airline name")
    airport_name = StringField("Airport name")
    airport_city = StringField("Airport city")
    submit = SubmitField("Add")


class AllianceAirlineForm(FlaskForm):
    name = StringField("Airline name")
    airline_name = StringField("2nd airline name")
    submit = SubmitField("Add")


class AllianceInfoAirlineForm(FlaskForm):
    name = StringField("Airline name")
    submit = SubmitField("Info")


class HubInfoAirlineForm(FlaskForm):
    name = StringField("Airline name")
    submit = SubmitField("Info")


# Airport

class AddAirportForm(FlaskForm):
    name = StringField("Airport name")
    city = StringField("Airport city")
    submit = SubmitField("Add")


class DeleteAirportForm(FlaskForm):
    name = StringField("Airport name")
    city = StringField("Airport city")
    submit = SubmitField("Delete")


class DistanceAirportForm(FlaskForm):
    name = StringField("Airport name")
    city = StringField("Airport city")
    airport_name = StringField("2nd airport name")
    airport_city = StringField("2nd airport city")
    flight_time = StringField("Flight time")
    submit = SubmitField("Add")


class DistanceInfoAirportForm(FlaskForm):
    name = StringField("Airport name")
    city = StringField("Airport city")
    submit = SubmitField("Info")


class HubInfoAirportForm(FlaskForm):
    name = StringField("Airport name")
    city = StringField("Airport city")
    submit = SubmitField("Info")
