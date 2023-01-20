#      
#=======================================================      
#   Aarya Shah, 20944383      
#   CS 116 Winter 2022      
#  Assignment 8, Question 3   
#=======================================================      
#     

import check

def anagram_checker(los):
  '''
  anagram_checker(los) mutates los to find out each element in the string. It 
  helps determine whether there is an anagram.
  
  Effects: Mutates los
  
  anagram_checker: (listOf Str) -> (listOf (listOf Str))
  '''
  if los == []:
    return []
  else:
    return [sorted(los[0])] + anagram_checker(los[1:])


def anagram_sort(los):
  '''
  anagram_sort(los) mutates los so that the list is in the following order:
  1. Strings that are anagrams of each other are adjacent to each other and in 
  alphabetical order.
  2. Let's call all strings that are anagrams of each other a block. Then the 
  previous comment implies that each block must be in alphabetical order. These 
  final blocks must also be sorted in alphabetical order according to the first 
  elements in each block.
  
  Effects: Mutates los
  
  anagram_sort: (listOf Str) -> None
  
  Examples:
  L = ["z", "a", "papel", "seer", "eres", "apple", "zamply"]
  anagram_sort(L) => None
  and the list L is mutated to 
  ["a", "apple", "papel", "eres", "seer", "z", "zamply"]
  
  L = []
  anagram_sort(L) => None
  and the list L is mutated to []
  '''
  los.sort(reverse = False)
  
  for i in range(1, len(los)):
    
    while sorted(los[i - 1]) > sorted(los[i]):
      if sorted(los[i]) in anagram_checker(los[:i]):
        los[i], los[i - 1] = los[i - 1], los[i]
        i = i - 1
      else:
        i = i - 1

##Examples
L = ["z", "a", "papel", "seer", "eres", "apple", "zamply"]
check.expect("Example 1", anagram_sort(L), None)
check.expect("Mutation", L, 
["a", "apple", "papel", "eres", "seer", "z", "zamply"])

M = []
check.expect("Example 2", anagram_sort(M), None)
check.expect("Mutation", M, []) 

##Tests
N = ["hell", "app", "pear", "zion", "ape", "apple", "hello"]
check.expect("Test 1", anagram_sort(N), None)
check.expect("Mutation", N, 
['ape', 'app', 'apple', 'hell', 'hello', 'pear', 'zion'])

O = ["b", "bell", "base", "brown", "brick"]
check.expect("Test 1", anagram_sort(O), None)
check.expect("Mutation", O, ['b', 'base', 'bell', 'brick', 'brown'])
