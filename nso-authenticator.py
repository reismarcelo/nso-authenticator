#! /usr/bin/env python
import csv


def credentials():
    """
    Capture credentials on stdin as “[<user>;<password>;]\n” and return username and password
    :return: <username>, <password> tuple
    """
    username, password, _ = input().lstrip('[').split(';')
    return username, password


def user_groups(username, auth_filename='auth.csv'):
    """
    Return a list of user groups associated with username. Groups are constructed from roles and services associated
    to the user in the form: <group> = <role>.<service>
    :param username: string representing username
    :param auth_filename: CSV file with rows in the form <username>, <role>, <service>
    :return: list of groups associated with username
    """
    with open(auth_filename) as auth_file:
        return ['.'.join(row[1:]) for row in csv.reader(auth_file) if len(row) > 2 and row[0] == username]


if __name__ == '__main__':
    user, pwd = credentials()

    group_list = user_groups(user)

    if len(group_list) > 0:
        reply_message = "accept {groups} {uid} {gid} {home}".format(
            groups=' '.join(group_list),
            uid='65534',
            gid='65534',
            home='/tmp'
        )
    else:
        reply_message = "reject {message}".format(
            message='no groups associated with user {}'.format(user)
        )

    print(reply_message)
