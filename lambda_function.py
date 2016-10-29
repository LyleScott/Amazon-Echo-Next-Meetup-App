# Lyle Scott, III
# https://ls3.io
# lyle@ls3.io

from __future__ import print_function
from datetime import datetime
import re

# Fix up PYTHONPATH to account for libs and src directories.
import sys

# This is where I put 3rd party libs I need to install. Remember, Lambda does not let you install
# things via pip, so you must package up all 3rd party application source with the Lambda code.
# To install a pip package to a directory of your choosing:
# pip install -t libs <your package>
sys.path.insert(0, 'libs')

# You may put any of your source in the following directory and use them as normal packages.
sys.path.insert(1, 'src')

# Now, we can import packages bootstrapped in the above path insertions.
import requests

# Local package imports.
from helpers import build_response, build_speechlet_response
import settings


def lambda_handler(event, context):
    """Route the incoming request based on the event."""

    # Prevent unwanted access to this Lambda function.
    app_id = event['session']['application']['applicationId']
    if settings.LAMBDA_ARN and app_id != settings.LAMBDA_ARN:
        speech = 'Permission denied!'
        build_response(build_speechlet_response(speech))

    func_map = {
        'LaunchRequest': on_launch,
        'IntentRequest': on_intent,
    }

    request = event['request']

    return func_map[request['type']](request, event['session'])


def on_launch(request, session):
    """Called when the user launches the skill without specifying what they want."""
    return intent_next_meeting()


def on_intent(request, session):
    """Called when the user specifies an intent for this skill."""
    if request['intent']['name'] == "NextMeetupIntent":
        return intent_next_meeting()


def intent_next_meeting():
    """Initialize the session to have some attributes."""
    url = '{}/events/?key={}'.format(settings.MEETUP_API_ROOT, settings.MEETUP_API_KEY)
    response = requests.get(url)
    try:
        response_json = response.json()
    except ValueError:
        speech = 'Oh, no! Invalid JSON response.'
        return build_response(build_speechlet_response(speech))

    if not len(response_json):
        speech = 'There are currently no scheduled meetups coming up, but check back soon!'
        return build_response(build_speechlet_response(speech))

    event = response_json[0]
    name = event['name']
    when = datetime.fromtimestamp(event['time'] / 1000).strftime('%A, %B %d at %I:%M %p')
    desc = re.sub('<[^<]+?>', '', event['description'])
    speech = ('The next Python Saint Pete meeting is {}. The topic is {} with a description of '
              '{}'.format(when, name, desc))

    return build_response(build_speechlet_response(
        speech, card_title='PyStPete Meetup', card_content='\n'.join((when, name, desc))))
