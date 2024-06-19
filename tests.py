#!/usr/bin/python3

import collection_neighbors as cn

def test_get_content():
    print('test get_content')
    a = cn.get_content('123')
    b = cn.get_content('124')
    c = cn.get_content('123')
    if (a != 'a'):
        print('get_content does not return "a" for the first value')
    else:
        print('. ', end = '')
    if (b != 'b'):
        print('get_content does not return correct following key')
    else:
        print('. ', end = '')
    if (c != 'a'):
        print('get_content returns different keys for equal values')
    else:
        print('. ')

def test_count_equal():
    print('test count_equal')
    if (cn.count_equal('halo', 'man') != 1):
        print('count equal returns wrong count for 1 equal letter')
    else:
        print('. ', end = '')
    if (cn.count_equal('halo', 'maler') != 2):
        print('count equal returns wrong count for several equal letters')
    else:
        print('. ', end = '')
    if (cn.count_equal('halo', 'mund') != 0):
        print('count equal returns wrong count for zero equal letters')
    else:
        print('. ', end = '')
    if (cn.count_equal('', 'mond') != 0):
        print('count equal returns wrong count for comparison to empty string')
    else:
        print('. ')

def test_levenshtein():
    print('test levenshein')
    if (cn.levenshtein('halo', 'man') != 3):
        print('levenshtein returns wrong count for several operations')
    else:
        print('. ', end = '')
    if (cn.levenshtein('halo', 'halm') != 1):
        print('levenshtein returns wrong count for single substitution')
    else:
        print('. ', end = '')
    if (cn.levenshtein('halo', 'hal') != 1):
        print('levenshtein returns wrong count for single deletion')
    else:
        print('. ', end = '')
    if (cn.levenshtein('halo', 'halom') != 1):
        print('levenshtein returns wrong count for single insertion')
    else:
        print('. ', end = '')
    if (cn.levenshtein('halo', 'halo') != 0):
        print('levenshtein returns wrong count for equal words')
    else:
        print('. ')

def test_get_signature():
    print('test get_signature')
    a = '123'
    b = '124'
    c = '125'
    if (cn.get_signature([a]) != 'a'):
        print('get_signature does not yield "a" for first given single work collection')
    else:
        print('. ', end = '')
    if (cn.get_signature([a,b]) != 'ab'):
        print('get_signature does not yield "ab" for first two work collection')
    else:
        print('. ', end = '')
    if (cn.get_signature([a,c]) != 'ac'):
        print('get_signature does not yield "ac" for second two work collection')
    else:
        print('. ')

def test_get_works():
    print('test get_works')
    if(cn.get_works('993121470')[0] != '1236'):
        print('get_works retrieves other work node than "1236" for collection with id "993121470"')
    else:
        print('. ')

if __name__ == "__main__":
    test_get_content()
    test_count_equal()
    test_levenshtein()
    test_get_signature()
    test_get_works()
    print('Tests executed. If no warnings showed up, everything works fine!')

