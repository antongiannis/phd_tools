import os
import secrets
import string


def credential_generator(no_accounts=1, string_length=10):
    """
    Creates credentials (username, password) for a number of accounts.

    Parameters
    ----------
    no_accounts: int, optional
        Integer showing the number of accounts.
    string_length: int, optional
        Integer showing the length of the string for password.

    Returns
    -------
    A list of username-password pairs.
    """

    # Maybe also a counter as an argument ?? ...
    string_length = int(string_length)
    username_length = int(string_length/2)

    # List of dictionaries
    credentials_list = []

    for account in range(no_accounts):
        username_rnd = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(username_length))
        password_rnd = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(string_length))
        credentials_list.append({"username": username_rnd, "password": password_rnd})

    return credentials_list


def account_generator(no_accounts=1, host="localhost"):
    """
    Generates accounts in Prosody xmpp server, for a predefined host in the config file of prosody.
    It only works for ubuntu at this stage.

    Parameters
    ----------
    no_accounts: int, optional
        Integer showing the number of agents.
    host: str, optional
        The name of the host in prosody.

    Returns
    -------
    A list of username-password pairs.
    """

    # Get the randomly generated pair of username-password pairs
    account_credentials = credential_generator(no_accounts)

    # Utilising the user 'giannis' to do a passwordless sudo. It only stands for my case!
    base_command = "sudo -H -u giannis bash -c"

    # Run commands in OS system (in this case ubuntu)
    for account in range(no_accounts):
        register_command = " 'sudo prosodyctl register " + account_credentials[account].get('username') + ' ' + host \
                           + ' ' + account_credentials[account].get('password') + "'"
        os.system(base_command + register_command)

    # Error handling to be added

    return account_credentials


def account_destructor(credentials_list, host="localhost"):
    """
    Deletes the accounts in Prosody xmpp server, for a predefined host in the config file of prosody, when provided with
    a list of username-password pairs. It only works for ubuntu at this stage.

    Parameters
    ----------
    credentials_list: list
        List of username-password pairs in dict.
    host: str, optional
        The name of the host in prosody.

    """

    # Utilising the user 'giannis' to do a passwordless sudo. It only stands for my case!
    base_command = "sudo -H -u giannis bash -c"

    for account in credentials_list:
        del_command = " 'sudo prosodyctl deluser " + account.get('username') + "@" + host + "'"
        os.system(base_command + del_command)

    # Error handling to be added
