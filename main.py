from flask import Flask, render_template
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/bdnp_17')
def bdnp_17():
    return render_template('combined_map_near_sea_17.html')


@app.route('/bdnp_33')
def bdno_64():
    return render_template('combined_map_near_sea_33.html')

@app.route('/bdnp_33_autre')
def bdnp_33_autre():
    return render_template('combined_map_near_sea_33_autre.html')

@app.route('/bdnp_33_fort')
def bdnp_33_fort():
    return render_template('combined_map_near_sea_33_fort.html')

@app.route('/bdnp_40')
def bdnp_40():
    return render_template('combined_map_near_sea_40.html')

@app.route('/bdnp_64')
def bdnp_64():
    return render_template('combined_map_near_sea_64.html')



if __name__ == '__main__':
    app.run(debug=True)
