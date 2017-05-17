# -*- coding: utf-8 -*-
"""
Created on Wed May 17 19:12:12 2017

@author: Nayadmk
"""

import regex as re
import nltk

def remove_non_ascii(text):
    return ''.join(i for i in text if ord(i) < 128)
    
def ie_preprocess(document):
    sentences = nltk.sent_tokenize(document)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    return sentences

def extract_names(document):
    names = []
    sentences = ie_preprocess(document)
    for tagged_sentence in sentences:
        for chunk in nltk.ne_chunk(tagged_sentence):
            if type(chunk) == nltk.tree.Tree:
                if chunk.label() == 'PERSON':
                    names.append(' '.join([c[0] for c in chunk]))
    return names

"""def extract_organizations(document):
   organizations = []
   sentences = ie_preprocess(document)
   for tagged_sentence in sentences:
       for chunk in nltk.ne_chunk(tagged_sentence):
           if type(chunk) == nltk.tree.Tree:
               if chunk.label() == 'ORGANIZATION':
                   organizations.append(' '.join([c[0] for c in chunk]))
   return organizations
"""
entity = []
for i in range(0, 9):
  file = open(str(i) + ".txt", "r")
  string = remove_non_ascii(file.read())
  names = extract_names(string)
  names = list(set(names))
  entity.append(names)

print(entity)