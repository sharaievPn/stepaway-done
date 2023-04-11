from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_session import Session
import script

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config['PERMANENT_SESSION_LIFETIME'] = 1200  # Set lifespan to 20 minutes
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route('/')
def starting_page():
    return redirect(url_for('home_ukrainian'))


@app.route('/ua/', methods=['GET', 'POST'])
@app.route('/ua', methods=['GET', 'POST'])
def home_ukrainian():
    user_agent = request.headers.get('User-Agent')
    if request.method == 'GET':
        if 'Mobi' in user_agent:
            return render_template('main_ukrainian_mobile.html')
        else:
            return render_template('main_ukrainian.html')
    else:
        data = request.get_json()
        lat = data['latitude']
        lng = data['longitude']
        session['lat'] = lat
        session['lng'] = lng
        return jsonify({'success': True})


@app.route('/ua/map', methods=['GET', 'POST'])
@app.route('/ua/map/', methods=['GET', 'POST'])
def introduce_ukrainian():
    user_agent = request.headers.get('User-Agent')
    chrome = 'Chrome' in user_agent
    mobile = 'Mobi' in user_agent
    try:
        filter_list = []
        lat = session.get('lat', None)
        lng = session.get('lng', None)

        if request.method == 'GET':
            return script.create_map_ukrainian(lat, lng, filter_list, chrome, mobile)
        else:
            checkbox1 = request.form.get('shelter') == 'on'
            checkbox2 = request.form.get('unbreakpoint') == 'on'
            checkbox3 = request.form.get('drugstore') == 'on'
            checkbox4 = request.form.get('hospital') == 'on'
            checkbox5 = request.form.get('police_departments') == 'on'
            filter_list = []
            if checkbox1:
                filter_list.append("shelter")
            if checkbox2:
                filter_list.append("unbreakable")
            if checkbox3:
                filter_list.append("drugstores")
            if checkbox4:
                filter_list.append("hospitals")
            if checkbox5:
                filter_list.append("police")
            return script.create_map_ukrainian(lat, lng, filter_list, chrome, mobile)
    except ValueError:
        if mobile:
            return render_template('error_internal_ukrainian_mobile.html')
        return render_template('error_internal_ukrainian.html')


@app.route('/en/', methods=['GET', 'POST'])
@app.route('/en', methods=['GET', 'POST'])
def home_english():
    user_agent = request.headers.get('User-Agent')
    if request.method == 'GET':
        if 'Mobi' in user_agent:
            return render_template('main_english_mobile.html')
        else:
            return render_template('main_english.html')
    else:
        data = request.get_json()
        lat = data['latitude']
        lng = data['longitude']
        session['lat'] = lat
        session['lng'] = lng
        return jsonify({'success': True})


@app.route('/en/map/', methods=['GET', 'POST'])
@app.route('/en/map', methods=['GET', 'POST'])
def introduce_english():
    user_agent = request.headers.get('User-Agent')
    chrome = 'Chrome' in user_agent
    mobile = 'Mobi' in user_agent
    try:
        filter_list = []
        lat = session.get('lat', None)
        lng = session.get('lng', None)

        if request.method == 'GET':
            return script.create_map_english(lat, lng, filter_list, chrome, mobile)
        else:
            checkbox1 = request.form.get('shelter') == 'on'
            checkbox2 = request.form.get('unbreakpoint') == 'on'
            checkbox3 = request.form.get('drugstore') == 'on'
            checkbox4 = request.form.get('hospital') == 'on'
            checkbox5 = request.form.get('police_departments') == 'on'
            filter_list = []
            if checkbox1:
                filter_list.append("shelter")
            if checkbox2:
                filter_list.append("unbreakable")
            if checkbox3:
                filter_list.append("drugstores")
            if checkbox4:
                filter_list.append("hospitals")
            if checkbox5:
                filter_list.append("police")
            return script.create_map_english(lat, lng, filter_list, chrome, mobile)
    except ValueError:
        if mobile:
            return render_template('error_internal_english_mobile.html')
        return render_template('error_internal_english.html')


@app.route('/ua/about-us/', methods=['GET'])
@app.route('/ua/about-us', methods=['GET'])
def about_us_ukrainian():
    user_agent = request.headers.get('User-Agent')
    mobile = 'Mobi' in user_agent
    if mobile:
        return render_template('about_us_ukrainian_mobile.html')
    return render_template('about_us_ukrainian.html')


@app.route('/en/about-us/', methods=['GET'])
@app.route('/en/about-us', methods=['GET'])
def about_us_english():
    user_agent = request.headers.get('User-Agent')
    mobile = 'Mobi' in user_agent
    if mobile:
        return render_template('about_us_english_mobile.html')
    return render_template('about_us_english.html')


@app.route('/ua/policies/', methods=['GET'])
@app.route('/ua/policies', methods=['GET'])
def policies_ukrainian():
    user_agent = request.headers.get('User-Agent')
    mobile = 'Mobi' in user_agent
    if mobile:
        return render_template('policies_ukrainian_mobile.html')
    return render_template('policies_ukrainian.html')


@app.route('/en/policies/', methods=['GET'])
@app.route('/en/policies', methods=['GET'])
def policies_english():
    user_agent = request.headers.get('User-Agent')
    mobile = 'Mobi' in user_agent
    if mobile:
        return render_template('policies_english_mobile.html')
    return render_template('policies_english.html')


@app.route('/ua/error/', methods=['GET'])
@app.route('/ua/error', methods=['GET'])
def error_ukrainian():
    user_agent = request.headers.get('User-Agent')
    mobile = 'Mobi' in user_agent
    if mobile:
        return render_template('error_geolocation_ukrainian_mobile.html')
    return render_template('error_geolocation_ukrainian.html')


@app.route('/en/error/', methods=['GET'])
@app.route('/en/error', methods=['GET'])
def error_english():
    user_agent = request.headers.get('User-Agent')
    mobile = 'Mobi' in user_agent
    if mobile:
        return render_template('error_geolocation_english_mobile.html')
    return render_template('error_geolocation_english.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
