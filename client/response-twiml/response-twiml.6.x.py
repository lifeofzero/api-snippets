from flask import Flask, Response
from twilio import twiml

app = Flask(__name__)


@app.route("/voice", methods=['POST'])
def get_voice_twiml():
    """Respond to incoming calls with a simple text message."""

    resp = twiml.Response()
    resp.say("Thanks for calling!")

    return Response(str(resp), mimetype='text/xml')

if __name__ == "__main__":
    app.run(debug=True)
