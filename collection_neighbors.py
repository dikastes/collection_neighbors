#!/usr/bin/python3

import sys
import xml.etree.ElementTree as ET
import urllib.request

content_keys = {}

if __name__ == "__main__":
    # read rism id from command line argument
    rism_id = sys.argv[1]
    main(rism_id)

def main(rism_id):
    # querying content work nodes of the collection from rism
    works = get_works(rism_id)
    # calculating abcd.. signature for collection
    signature = get_signature(works)
    print('the signature of the collection is ' + signature)
    # querying candidate collections from rism
    collection_lists = [ get_collections(work) for work in works ]
    # getting a flat list with unique entries
    collections = { collection for collection_list in collection_lists for collection in collection_list }
    # querying content work nodes for every candidate collection
    work_lists = { collection: get_works(collection) for collection in collections }
    # calculating signatures for candidate collections
    #signatured_collections = { collection: { 'works': works, 'signature': get_signature(collection) for collection: works in work_lists }

    # calculating distance measures
                              #measured_collections = { collection: {
                              #'works': works['works'], 'signature': works['signature'], 'equal': count_equal(works['signature'], signature), 'levenshtein': levenshtein(works['signature'], signature) }
                              #for collection in signatured_collections }
                              #print(measured_collections)

def count_equal(str1, str2):
    equals = {char for char in str1 if char in str2}
    return len(equals)

levenshtein_buffer = {}

def memoised_levenshtein(str1, str2):
    if str1 not in levenshtein_buffer or str2 not in levenshtein_buffer[str1]:
        levenshtein_buffer[str1] = { str2: levenshtein(str1, str2) }
        levenshtein_buffer[str2] = { str1: levenshtein(str1, str2) }
    return levenshtein_buffer[str1][str2]

def levenshtein(str1, str2):
    if len(str1) == 0:
        return len(str2)
    if len(str2) == 0:
        return len(str1)
    if str1[0] == str2[0]:
        return levenshtein(str1[1:], str2[1:])
    dist1 = 1 + levenshtein(str1, str2[1:])
    dist2 = 1 + levenshtein(str1[1:], str2)
    dist3 = 1 + levenshtein(str1[1:], str2[1:])
    return min(dist1, dist2, dist3)

def get_signature(collection):
    return ''.join([ get_content(work) for work in collection ])

def get_works(rism_id):
    print(f"Querying items of collection https://opac.rism.info/id/rismid/{rism_id}?format=marc")
    resource = urllib.request.urlopen(f"https://opac.rism.info/id/rismid/{rism_id}?format=marc").read()
    parsed_resource = ET.fromstring(resource)
    collection_items = [ retrieve_w_subfield(item) for item in parsed_resource if 'tag' in item.attrib and item.attrib['tag'] == '774']
    works = [retrieve_work_node(item) for item in collection_items]
    return [work for work in works if work != None]

def retrieve_work_node(item):
    # TODO DRYify next 3 lines
    print(f"Querying work_node of item https://opac.rism.info/id/rismid/{item}?format=marc")
    resource = urllib.request.urlopen(f"https://opac.rism.info/id/rismid/{item}?format=marc").read()
    parsed_resource = ET.fromstring(resource)
    work_field = [field for field in parsed_resource if 'tag' in field.attrib and field.attrib['tag'] == '930']
    if len(work_field):
        return [subfield for subfield in work_field[0] if 'code' in subfield.attrib and subfield.attrib['code'] == '0' and subfield.text.isnumeric()][0].text
    else:
        return None

def retrieve_w_subfield(item):
    subfield_w = [subfield for subfield in item if 'code' in subfield.attrib and subfield.attrib['code'] == 'w']
    return subfield_w[0].text

def get_characteristics(collection):
    return []

def get_content(rism_id):
    if rism_id in content_keys:
        return content_keys[rism_id]
    if len(content_keys):
        max_value = max(content_keys.values())
        new_value = chr(ord(max_value) + 1)
    else:
        new_value = 'a'
    content_keys[rism_id] = new_value
    return new_value

