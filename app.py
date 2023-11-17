from flask import Flask, render_template, request
import requests

app = Flask(__name__, template_folder="templates")


# Function to fetch country data from REST Countries API
def get_country_info(country_name):
    base_url = "https://restcountries.com/v2/name/"
    response = requests.get(base_url + country_name)
    return response.json()


@app.route("/", methods=["GET", "POST"])
def index():
    country_info = None

    if request.method == "POST":
        country_name = request.form["country_name"]
        country_info = get_country_info(country_name)

    return render_template("index.html", country_info=country_info)


if __name__ == "__main__":
    app.run(debug=True)
