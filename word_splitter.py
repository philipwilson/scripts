#!/usr/bin/env python

import sys

dictionary = set([])
domain_list = []

WORDS = '/Users/wilsonp/src/english-words/words.txt'

def match(dictionary, collect, left_part, right_part, depth):
    # print("[%d] - [%s] [%s]" % (depth, left_part, right_part))

    if not left_part:
        return collect
    
    elif left_part in dictionary:
        if right_part:
            submatch = match(dictionary, [], right_part, "", depth + 1)
            if submatch:
                for matchlist in submatch:
                    collect.append([left_part] + matchlist)
        else:
            collect.append([left_part])

    return match(dictionary, collect, left_part[:-1], left_part[-1] + right_part, depth + 1)


def words_from_string(dictionary, string):
    return match(dictionary, [], string, "", 1)

with open(WORDS) as words:
    for word in words:
        word = word.rstrip().lower()
        if len(word) >= 2:
            dictionary.add(word)

with open("/Users/wilsonp/domains.txt") as domains:
    for domain in domains:
        domain_list.append(domain.rstrip())

for domain in domain_list:        
    pieces = domain.split('-')
    for piece in pieces:
        matches = match(dictionary, [], piece, "", 1)
        if matches:
            shortest = len(domain)
            for matchlist in matches:
                if len(matchlist) < shortest:
                    shortest = len(matchlist)
                
            for matchlist in matches:
                if len(matchlist) == shortest:
                    for term in matchlist:
                        if term:
                            print("\t".join([domain, term]))
                    print("")
        else:
            print(domain, file=sys.stderr)
