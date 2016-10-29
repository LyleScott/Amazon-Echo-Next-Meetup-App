
def build_response(speechlet_response, session_attributes=None):
    session_attributes = session_attributes or {}
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response,
    }


def build_speechlet_response(speech, card_title='PyStPete', card_content='',
                             should_end_session=True):
    output = {
        'outputSpeech': {
            'type': 'PlainText',
            'text': speech,
        },
        'shouldEndSession': should_end_session,
    }

    if card_title:
        output['card'] = {
            'type': 'Simple',
            'title': card_title,
            'content': card_content,
        }

    return output
