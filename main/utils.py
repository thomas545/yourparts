import requests


APIKEY = 'd56a256253ca2fec34597007df88aed9'

def get_weather(city):
    params = {
    'access_key': APIKEY,
    'query': str(city)
    }

    api_result = requests.get('https://api.weatherstack.com/current', params)

    api_response = api_result.json()

    # print(u'Current temperature in %s is %d℃' % (api_response['location']['name'], 
    #                                       api_response['current']['temperature']))
    return api_response
