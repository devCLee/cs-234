"""
Purpose: Solution for assignment 1 - Part B
Author: Daniel Lee
Date: January 26, 2025
CS 234, Spring 2025
References:
https://www.programiz.com/python-programming/methods/built-in/frozenset
https://www.almabetter.com/bytes/tutorials/python/tuples-and-sets-in-python
https://www.geeksforgeeks.org/python-tuple-len-method/
https://docs.python.org/3/tutorial/datastructures.html
"""


def encode(pair):
    if pair[0] == pair[1]:
        return {frozenset({pair[0]})}
    else:
        """
        res = set()
    
        res.add(frozenset({pair[0]}))
        res.add(frozenset({pair[0], pair[1]}))
        
        return res
        """
        print(pair[0])
        print(pair[1])
        
        return {frozenset({pair[0]}), frozenset({pair[0], pair[1]})}

#print(encode((5,5)))
#print(encode((5,"")))
#print(encode(("",5)))
#print(encode(("","")))
#print(encode((""," ")))
#print(encode((3, 3))) #{frozenset({3})}
#print(encode(("a", "a"))) #{frozenset({"a"})}
#print(encode((0, 1))) #{frozenset({0}), frozenset({0, 1})}
#!!!!!!!!!!!!!!!!!!!
#print(encode((-5, 10))) #{frozenset({-5}), frozenset({-5, 10})}
#!!!!!!!!!!!!!!!!!!!
#print(encode(("a", "b"))) #{frozenset({"a"}), frozenset({"a", "b"})}
#print(encode(("aa", "bb"))) #{frozenset({"aa"}), frozenset({"aa", "bb"})}


def decode(kpair):
    
    res = []
    otherElement = 0
    
    for i in kpair:
       res.append(list(i))
       
    print(res)
    
    if len(res) == 1:
        return (res[0][0], res[0][0])
    
    if len(res[0]) > len(res[1]):
        for i in range(2):
            if res[0][i] != res[1][0]:
                otherElement = res[0][i]
                
        print("first")
        
        return (res[1][0], otherElement)
    else:
        for i in range(2):
            if res[1][i] != res[0][0]:
                otherElement = res[1][i]
        
        print("second")
        
        return (res[0][0], otherElement)

#print(decode({frozenset({5}), frozenset({7,5})}))
#print(decode({frozenset({7,5}), frozenset({5})}))
#print(decode({frozenset({5}), frozenset({5,7})}))
#print(decode({frozenset({5,7}), frozenset({5})}))
#!!!!!!!!!!!!!!!!!!!
#print(decode({frozenset({7,5}), frozenset({5})}))
#print(decode({frozenset({8,5}), frozenset({5})}))
#!!!!!!!!!!!!!!!!!!!
#print(decode({frozenset({3})}))
#print(decode({frozenset({0}), frozenset({0, 1})}))
#print(decode({frozenset({"a"}), frozenset({"b", "a"})}))

# print(decode({frozenset({"aa"}), frozenset({"aa", "bb"})}))
# print(decode({frozenset({10, -5}), frozenset({-5})}))
# print(decode({frozenset({"a"})}))

#!! Input of set of tripples are valid input but should return false -> return false if the elts of sets are not pairs

#!! check for pairs having empty string ("")
def isFun(rel):
    
    res = True
    
    set2List = list(rel)
    
    if len(set2List) == 0:
        return res
    

    for i in range(len(set2List)):
        if len(set2List[i]) == 0 or len(set2List[i]) != 2:
            res = False
    
    for i in range(len(set2List)-1):
        if set2List[i][0] == set2List[i+1][0]:
            res = False
    
    return res

#!!!!!!!!!!!
#print(isFun(set()))
#print(isFun({frozenset()}))
#print(isFun({(1, 1)}))
#print(isFun({((1,1), 2), ((1,1), 4), (5, 6)}))
#print(isFun({(1, 5), (2, 5), (3, 5)}))

# print(isFun({(1, 2, 3)}))
# print(isFun({("a", "b", "c"), (1, 2), (3, 4, 5)}))

#!! print(isFun({(1,1), (2,)})) == print(isFun({(1,1), ("",2)}))

#print(isFun({("",1), ("",2)}))
#print(isFun({("",1), (" ",2)}))
# print(isFun({(1,1), (2,2)}))
# print(isFun({}))
# print(isFun({(1,1), (2,3), (1,2)}))
# print(isFun({()}))


def applyFun(funRel, arg):
    
    set2List = list(funRel)
    
    print(set2List)
    
    for i in range(len(set2List)):
        if set2List[i][0] == arg:
            return set2List[i][1]

print(applyFun({("a","b"), ("c","d")}, "c") )

# print(applyFun({}, None))
