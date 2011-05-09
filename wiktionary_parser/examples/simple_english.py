# -*- coding: utf-8 -*-
"""
This example extracts a number of words from the simple.wiktionary xml file.
"""

from wiktionary_parser.xml_parser import XMLPageParser
from wiktionary_parser.languages.simple.page import simplePage

xml_file = open('../../wiktionary_data/simplewiktionary-20110505-pages-articles.xml')
xml_parser = XMLPageParser(xml_file, simplePage)

# The words we want to extract
wanted_words = set([u'fox', u'robust'])

found_words = set([])

for title, page in xml_parser.from_titles(wanted_words):
    page.parse()
    # Print out a summary of the want
    for word in page.words:
        print word.summary()
        print('')
    # Display any alerts that the parser raised.
    # Alerts indicate bugs in the parser or errors on the wiktionary page.
    all_alerts = page.get_alerts()
    if all_alerts:
        print('--------')
        print(page.title)
        print('--------')        
        for alert in all_alerts:
            print(alert.description)
            if hasattr(alert, 'message'):
                print(alert.message)
    
