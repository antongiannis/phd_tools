import numpy as np
import json

# check for multiple root nodes
# If there are then create a new root node so it can be parsed by Vega tree function


def update_parent_key(data_dict, parent_value="", inplace=False):
    """
    Function to add a parent key, value pair to a dict. Can be used to update it too.

    Parameters
    ----------
    data_dict: list
        List of dictionaries.
    parent_value: str, optional
        The value of the "parent" key.
    inplace: bool, default False
        If True, do operation inplace and return None.

    Returns
    -------
    An updated dictionary.
    """

    if isinstance(data_dict, dict):
        if inplace:
            data_dict.update({"parent": parent_value})
        else:
            out_dict = data_dict.copy()
            out_dict.update({"parent": parent_value})

            return out_dict
    else:
        raise TypeError('The input should be a dictionary.')


def create_root_node_vega(data_list, root_name='root'):
    """
    Function to create a root node, if there are

    Parameters
    ----------
    data_list: list
        List of dictionaries.
    root_name: str, optional
        Name of the root node.

    Returns
    -------
    The number of root nodes in a nested dict.
    """

    no_root = sum(["parent" not in item for item in data_list])

    if no_root > 1:
        # Update only the root dictionaries with parent key
        out_list = [update_parent_key(item, parent_value=root_name, inplace=False)
                    if "parent" not in item else item
                    for item in data_list]

        # Append the root node to the list
        out_list.append({"id": root_name, "name": root_name})
    else:
        out_list = data_list

    return out_list


def flatten_dict_vega(data_dict, previous_key='', items_list=[]):
    """
    Function to convert a python nested dictionary to json format. It is the output needed for
    Vega tree graph. In the future could add support for additional graphs.

    The output data should have a format like the following:

    [
        {
            "id": "root_node",
            "name": "root_name"
        },
        {
            "id": "sub_node1",
            "name": "sub_node1_name",
            "parent": "root_node"
        },
        {
            "id": "sub_node2",
            "name": "sub_node2_name",
            "parent": "root_node"
        },
        {
            "id": "sub_subnode1",
            "name": "sub_subnode1_name",
            "parent": "sub_node2",
            "size": "value"
        }
    ]

    Parameters
    ----------
    data_dict: dict
        Dictionary to be used as an input.
    previous_key: str, optional
        The key of the parent node in a nested dictionary.
    items_list: list, optional
        The main list of dictionaries.

    Returns
    -------
    A list of dictionaries.
    """

    # There is a problem with the list !!
    # Maybe use immutable and convert it to list. Need to look into it!
    # problem with setting a unique ID --> maybe have the

    for key, value in data_dict.items():
        # If root node
        if not previous_key:
            # Append id to list
            items_list.append({"id": key, "name": key})
            # If nested dict call function
            if isinstance(value, dict):
                _ = flatten_dict_vega(value, key, items_list)  # Use _ for unused assignments
            else:
                pass
        # If not root node
        else:
            # Append id and parent to list
            id_key = previous_key + '_' + key  # needs to be unique
            items_list.append({"id": id_key, "name": key, "parent": previous_key})
            # If nested dict call function
            if isinstance(value, dict):
                _ = flatten_dict_vega(value, id_key, items_list)
            else:
                pass

    return items_list


def find_by_key(data_dict, target_key):
    """
    Generator function to find a value based on a key in the tree structure.
    For more info on generators see here: https://wiki.python.org/moin/Generators

    Parameters
    ----------
    data_dict: dict
        Dictionary to be used as an input.
    target_key: str
        Key for the value wanted.
    """
    for key, value in data_dict.items():
        if isinstance(value, dict):
            yield from find_by_key(value, target_key)
        elif key == target_key:
            yield value
            

def dict_struct(data_dict):
    """
    Function to get the structure of a dict. Returns a dictionary with the keys only, retaining the 
    structure at the same time.
    
    Parameters
    ----------
    data_dict: dict
        Dictionary to be used as an input.
    
    Returns
    -------
    A dictionary with the structure of the input.
    """
    
    out_dict = {} 
    for key, value in data_dict.items():
        if isinstance(value, dict):
            sub_value = dict_struct(value)
            out_dict.update({key: sub_value})
        else:
            out_dict.update({key: [np.nan]})    
    return out_dict


def flat_dict(data_dict, input_tuple=()):
    """
    Recursive function to get a nested dictionary to a dictionary of tuples.

    Parameters
    ----------
    data_dict: dict
        Input dictionary to print.
    input_tuple: tuple, optional
        Initial tuple to pass.

    Returns
    -------
    A dictionary of tuples
    """
    out_dict = {}
    for key, value in data_dict.items():
        if isinstance(value, dict):
            out_tuple = input_tuple + (key,)
            sub_value = flat_dict(value, out_tuple)
            out_dict.update(sub_value)
        else:
            out_tuple = input_tuple + (key,)
            out_dict.update({out_tuple: value})

    return out_dict


def print_tree(data_dict, level=0):
    """
    Recursive function to print the structure of a dictionary.

    Parameters
    ----------
    data_dict: dict
        Input dictionary to print.
    level: int, optional
        Integer showing the starting level for tabs.
    """
    for key, value in data_dict.items():
        if isinstance(value, dict):
            print("\t" * level, key)
            print_tree(value, level + 1)
        else:
            print("\t" * level, key)
