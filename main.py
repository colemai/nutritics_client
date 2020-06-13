#!/usr/bin/env python3
"""
Author: Ian Coleman
Purpose: Call the Nutritics API

"""

import pdb
import requests

api_address = "https://iancoleman1a:Pokemon124*@www.nutritics.com/api/v1.1/"

def get_users ():
	all_users = requests.get("{}LIST/&client".format(api_address))
	return all_users.text

def create_user (uid):
	call = requests.get("{}CREATE/&client&id={}".format(api_address, uid))
	return call


if __name__ == "__main__":
	create_user(333)
	all_users = get_users()
	print(all_users)