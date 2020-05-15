# -*- coding: utf-8 -*-
"""
Created on Thu May 14 17:29:09 2020

@author: 10139
"""
# Import some important libraries
import xml.dom.minidom 
import pandas as pd

print('There is still some time before the program is complete, please wait a second. Thank you!')
gene_ontology = xml.dom.minidom.parse('go_obo.xml') # Parse the XML file into a DOM document 
collection = gene_ontology.documentElement # Get the root element of the document
terms = collection.getElementsByTagName('term') # Make a list of "term" elements
dic = {'id':[], 'name':[], 'definition':[], 'childnodes':[]} # Make a dictionary to store four kinds of information
for term in terms: 
    defstr_nodelist = term.getElementsByTagName('defstr')[0]
    defstr = defstr_nodelist.childNodes[0].data # Get the text between <defstr> and </detftr>
    if defstr.find('autophagosome')>=0: # Find the key word "autophagosome"
        go_id_nodelist = term.getElementsByTagName('id')[0] 
        go_id = go_id_nodelist.childNodes[0].data # Get the text between <id> and </id>
        dic['id'].append(go_id)
        name_nodelist = term.getElementsByTagName('name')[0]
        name = name_nodelist.childNodes[0].data # Get the text between <name> and </name>
        dic['name'].append(name)
        childnodes = 0
        related_term = [go_id] 
        flag = True
        while related_term != []: # Find all related gene ontology term
            related_term_copy = related_term
            related_term = []
            for j in related_term_copy:
                for term_copy in terms:
                    for i in term_copy.getElementsByTagName('is_a'):
                        is_a2_text = i.childNodes[0].data
                        if is_a2_text == j:
                            childnodes += 1
                            id_nodelist = term_copy.getElementsByTagName('id')[0]
                            related_term.append(id_nodelist.childNodes[0].data)
        dic['childnodes'].append(childnodes)
        dic['definition'].append(defstr)
df = pd.DataFrame(dic) # Set up a dataframe with the dictionary
df.to_excel(excel_writer='autophagosome.xlsx', encoding='utf-8', index=False, header=True) # Output an excel document
print('The output is autophagosome.xlsx, please check it.')        
        