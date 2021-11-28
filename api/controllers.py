import numpy as np
from flask import Flask, flash, request, render_template, redirect

from .forms import *
from .models.airline import *
from .models.airport import *
from .models.distance import *

app = Flask(__name__)

if __name__ == "__main__":
    app.run()


@app.route("/")
def home():
    return render_template('home.html')


# Airline


@app.route('/airline/index', methods=['GET', 'POST'])
def index_airline():
    results = Airline.index()
    items = []
    for result in results:
        items += result[0].values()
    return render_template('airline/index.html', items=items)


@app.route('/airline/add/', methods=['GET', 'POST'])
def add_airline():
    form = AddAirlineForm()
    if request.method == "POST":
        if form.is_submitted():
            result = request.form
            name = result['name']
            if Airline(name).add():
                flash(f"Added {name} airline")
            else:
                flash(f"{name} airline is already in the database")

    return render_template('airline/add.html', form=form)


@app.route('/airline/delete/', methods=['GET', 'POST'])
def delete_airline():
    form = DeleteAirlineForm()
    if request.method == "POST":
        if form.is_submitted():
            result = request.form
            name = result['name']
            if Airline(name).delete():
                flash(f"Deleted {name} airline")
            else:
                flash(f"{name} airline was not in the database")

    return render_template('airline/delete.html', form=form)


@app.route('/airline/hub/', methods=['GET', 'POST'])
def hub_airline():
    form = HubAirlineForm()
    if request.method == "POST":
        if form.is_submitted():
            result = request.form
            airline_name = result['airline_name']
            airport_name = result['airport_name']
            airport_city = result['airport_city']
            if Airline(airline_name).hub(Airport(airport_name, airport_city)):
                flash(f"{airport_name} in {airport_city} is now hub of {airline_name} airline")
            else:
                flash(f"{airport_name} in {airport_city} or {airline_name} does not exist")

    return render_template('airline/hub.html', form=form)


@app.route('/airline/alliance/', methods=['GET', 'POST'])
def alliance_airline():
    form = AllianceAirlineForm()
    if request.method == "POST":
        if form.is_submitted():
            result = request.form
            name = result['name']
            airline_name = result['airline_name']
            if Airline(name).alliance(Airline(airline_name)):
                flash(f"{name} is in alliance with {airline_name}")
            else:
                flash(f"{name} or {airline_name} does not exist")

    return render_template('airline/alliance.html', form=form)


@app.route('/airline/hub_info/', methods=['GET', 'POST'])
def hub_info_airline():
    form = HubInfoAirlineForm()
    if request.method == "POST":
        if form.is_submitted():
            result = request.form
            name = result['name']
            results = Airline(name).hub_info()
            if None in results[0]:
                flash(f"No hub information for {name}")
            else:
                items = []
                for result in results:
                    for r in result:
                        items += r.values()
                items = np.reshape(items, (-1, 3))
                return render_template('airline/hub_info_index.html', items=items)

    return render_template('airline/hub_info.html', form=form)


@app.route('/airline/alliance_info/', methods=['GET', 'POST'])
def alliance_info_airport():
    form = AllianceInfoAirlineForm()
    if request.method == "POST":
        if form.is_submitted():
            result = request.form
            name = result['name']
            results = Airline(name).alliance_info()
            if None in results[0]:
                flash(f"No alliance information for {name}")
            else:
                items = []
                for result in results:
                    for r in result:
                        items += r.values()
                items = np.reshape(items, (-1, 2))
                return render_template('airline/alliance_info_index.html', items=items)

    return render_template('airline/alliance_info.html', form=form)


# Airport


@app.route('/airport/index', methods=['GET', 'POST'])
def index_airport():
    results = Airport.index()
    items = []
    for result in results:
        items += result[0].values()
    items = np.reshape(items, (2, -1))
    return render_template('airport/index.html', items=items)


@app.route('/airport/add/', methods=['GET', 'POST'])
def add_airport():
    form = AddAirportForm()
    if request.method == "POST":
        if form.is_submitted():
            result = request.form
            name = result['name']
            city = result['city']
            if Airport(name, city).add():
                flash(f"Added {name} airport")
            else:
                flash(f"{name} airport in {city} is already in the database")

    return render_template('airport/add.html', form=form)


@app.route('/airport/delete/', methods=['GET', 'POST'])
def delete_airport():
    form = DeleteAirportForm()
    if request.method == "POST":
        if form.is_submitted():
            result = request.form
            name = result['name']
            city = result['city']
            if Airport(name, city).delete():
                flash(f"Deleted {name} in {city} airport")
            else:
                flash(f"{name} airport in {city} was not in the database")

    return render_template('airport/delete.html', form=form)


@app.route('/airport/distance/', methods=['GET', 'POST'])
def distance_airport():
    form = DistanceAirportForm()
    if request.method == "POST":
        if form.is_submitted():
            result = request.form
            name = result['name']
            city = result['city']
            airport_name = result['airport_name']
            airport_city = result['airport_city']
            flight_time = result['flight_time']

            if Airport(name, city).distance(Airport(airport_name, airport_city), Distance(flight_time)):
                flash(
                    f"Distance between {name} in {city} airport and {airport_name} in {airport_city} is {flight_time}h")
            else:
                flash(f"{name} airport in {city} was not in the database")

    return render_template('airport/distance.html', form=form)


@app.route('/airport/hub/', methods=['GET', 'POST'])
def hub_airport():
    return redirect('/airline/hub')


@app.route('/airport/distance_info/', methods=['GET', 'POST'])
def distance_info_airport():
    form = DistanceInfoAirportForm()
    if request.method == "POST":
        if form.is_submitted():
            result = request.form
            name = result['name']
            city = result['city']
            results = Airport(name, city).distance_info()
            if None in results[0]:
                flash(f"No distance information for {name} in {city}")
            else:
                items = []
                for result in results:
                    for r in result:
                        items += r.values()
                items = np.reshape(items, (-1, 5))
                return render_template('airport/distance_info_index.html', items=items)

    return render_template('airport/distance_info.html', form=form)


@app.route('/airport/hub_info/', methods=['GET', 'POST'])
def hub_info_airport():
    form = HubInfoAirportForm()
    if request.method == "POST":
        if form.is_submitted():
            result = request.form
            name = result['name']
            city = result['city']
            results = Airport(name, city).hub_info()
            if None in results[0]:
                flash(f"No hub information for {name} in {city}")
            else:
                items = []
                for result in results:
                    for r in result:
                        items += r.values()
                print(items)
                items = np.reshape(items, (-1, 3))
                print(items)
                return render_template('airport/hub_info_index.html', items=items)

    return render_template('airport/hub_info.html', form=form)
