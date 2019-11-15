import requests
from requests.exceptions import HTTPError
from requests_oauthlib import OAuth2Session
import pandas as pd


@pd.api.extensions.register_dataframe_accessor("phd")
class AddFunction:
    """
    Class to add the functionality of pandas dataframe. Pandas offer options for extending their functionality.
    Check the following page:
        https://pandas.pydata.org/pandas-docs/stable/development/extending.html

    To learn more about accessors 
    """
    def __init__(self, pandas_obj):
        self._obj = pandas_obj

    def unique_cols(self):
        """
        Get the unique values for each column of a pandas dataframe.

        Returns
        -------
        dict
            A dictionary containing the unique values for each column.
        """

        res_dict = {}
        for column in self._obj.columns:
            res_dict[column] = self._obj[column].unique()

        return res_dict


'''
def getResp(url, params, headers):
    """
    Gets the info from a RESTful API and returns it in JSON format. If the response
    contains invalid JSON, then it raises an error. It can also use the OAuth2
    authorisation framework.

    Parameters
    ----------
    url: str
        The url of the API.
    params: dict
        A dictionary of strings that provides data to the URL's query string.

    Returns
    -------
    A json . If the
    """

    # Use or not OAuth 2.0 authorisation
    if

    # Get the response object
    resp = requests.get(url, params=params, headers=, timeout=3)

    # Raise HTTPError if status_code != 200
    resp.raise_for_status()

    #
    for todo_item in resp.json():
        print('{} {}'.format(todo_item['id'], todo_item['summary']))

    return
'''
