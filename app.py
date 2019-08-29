"""Main file"""
import os
from flask import Flask, render_template, request, jsonify

from grandpy.apiwiki import Wiki
from grandpy.gmaps import GMaps
from grandpy.parseur import Parseur
from grandpy.stop_word import STOP_WORDS
from grandpy.messages import *
from config import API_KEY, ADDRESS_MSG, SUMMARY_MSG, FAILURE_MSG




app = Flask(__name__)

google_api_key = API_KEY

parser = Parseur(STOP_WORDS)
gmap = GMaps(google_api_key)
wiki = Wiki()


@app.route('/_get_json')
def get_json():
    """Recover in json format informations to return"""
    user_input = request.args.get("question", type=str)
    parsed_input = parser.get_relevant_word(user_input)
    if parsed_input == "":
        failure_msg = return_failure()
        return jsonify(message1=failure_msg,
                       error=True)

    gmap_place = gmap.get_position(parsed_input)
    if gmap_place != "no result":
        wiki_result = wiki.get_wiki_result(
            gmap_place["latitude"], gmap_place["longitude"], parsed_input)
        msg_adress = return_address(gmap_place["address"])

        if wiki_result != "no result":
            msg_summary = return_story(wiki_result['summary'])

            return jsonify(lat=gmap_place["latitude"],
                           lng=gmap_place["longitude"],
                           message1=msg_adress,
                           message2=msg_summary,
                           url=wiki_result["url"],
                           error=False)

        failure_msg = return_failure()
        return jsonify(message1=failure_msg,
                       error=True)

    failure_msg = return_failure()
    return jsonify(message1=failure_msg,
                   error=True)


@app.route('/')
@app.route('/home')
def index():
    """Show home page"""
    return render_template('home.html', api_key=google_api_key)


if __name__ == "__main__":
    app.run(debug=True)
