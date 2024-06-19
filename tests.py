#!/usr/bin/python

import collection_neighbors as cn

def test_get_content():
    a = cn.get_content('123')
    b = cn.get_content('124')
    c = cn.get_content('123')
    if (a != 'a'):
        print('get_content does not return "a" for the first value')
    if (b != 'b'):
        print('get_content does not return correct following key')
    if (c != 'a'):
        print('get_content returns different keys for equal values')

if __name__ == "__main__":
    test_get_content()

