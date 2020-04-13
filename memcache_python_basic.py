#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

from pymemcache.client import base

# server parameter of base.client is held as a tuple (host, port)
client = base.Client(('localhost', 11211))

def query_for_data():
    """   
    Returns:
        json encoded data structure
    """
    
    data_structure = {
        "langauge": "python",
        "system":"POSIX"
    }
    # we convert the dict into a string, as this is how the client.set method recieves it's data
    return json.dumps(data_structure)

def main():
    # data keys and values are always stored as strings
    result = client.get('data_from_query')

    if result is None:

        result = query_for_data()

        client.set('data_from_query', result)

    print(result)

    return

if __name__ == __main__:
    main()
