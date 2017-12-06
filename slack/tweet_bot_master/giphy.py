import time
import giphy_client
from giphy_client.rest import ApiException
from pprint import pprint

def text_to_gif(s):
    # create an instance of the API class
    api_instance = giphy_client.DefaultApi()
    api_key = 'p2L2ikMV8YGQgiu1xgpYEG1ngAZmrbKZ' # str | Giphy API Key.
    #s = 'ryan gosling' # str | Search term.

    try:
        # Translate Endpoint
        api_response = api_instance.gifs_translate_get(api_key, s)
        #pprint(api_response.data.bitly_gif_url)
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_translate_get: %s\n" % e)
    return api_response.data.bitly_gif_url
