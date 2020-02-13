# import requests
# from requests.exceptions import HTTPError
# from requests_oauthlib import OAuth2Session
import pandas as pd
from functools import singledispatch


# Use the `@singledispatch` decorator to transform the function to a single-dispatch generic function.
# Unexpected behaviour when the object is a combination of lists and dictionaries
# No implementation for circular references (e.g. circular = {}; circular["self"] = circular)
@singledispatch
def depth(_, _level=0):
    """
    A generic function composed of multiple functions calculating the depth of an object (e.g. dict, list, etc.).
    Which implementation should be used during a call is determined by the dispatch algorithm. In this case the
    implementation is chosen based on the type of a single argument (first argument of the function).
    """
    return _level


# Use the the `register()` decorator to add overloaded implementations to the `depth` function
@depth.register
def _dict_depth(input_dict: dict, _level=0):
    """
    The implementation of the `depth()` generic function for dictionary type.
    """
    # Create a list that gets the depth of every node recursively
    out_list = [depth(value, _level=_level + 1) for value in input_dict.values()]

    # Return the max of the list, with 0 if it's empty.
    return max(out_list, default=0)


'''
@depth.register
def _list_depth(input_list: list, _level=0):
    """
    The implementation of the `depth()` generic function for list type.
    """
    # Create a list that gets the depth of every node recursively
    out_list = [depth(item, _level=_level + 1) for item in input_list]

    # Return the max of the list, with 0 if it's empty.
    return max(out_list, default=0)
'''


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
