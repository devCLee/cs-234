"""
Purpose: Solution for assignment 3 - Part 2
Author: Daniel Lee
Date: February 9, 2025
CS 234, Spring 2025
References: https://www.programiz.com/python-programming/methods/built-in/frozenset
https://www.programiz.com/python-programming/methods/built-in/set
https://www.programiz.com/python-programming/methods/set/add
https://www.w3schools.com/python/gloss_python_loop_set_items.asp
https://www.geeksforgeeks.org/python-check-if-list-empty-not/
"""


def acceptNFA(fiveTuple, string):

    fiveTuple = convertNFAtoDFA(fiveTuple)


    currentStringIndex = 0
    
    currentState = fiveTuple[3]
    
    transFuncList = list(fiveTuple[2])
    
    
    while currentStringIndex < len(string):
        
        for i in range(len(transFuncList)):
            funcRel = transFuncList[i][0]
            
            if funcRel[0] == currentState and funcRel[1] == string[currentStringIndex]:
                currentState = transFuncList[i][1]
                
                break
        
        currentStringIndex += 1

    if currentState in list(fiveTuple[4]):
        return True
    else:
        return False


def convertNFAtoDFA(fiveTuple):

    Q_N, sigma, delta_N, q0, F_N = fiveTuple

    # Line 1, 2
    initState = frozenset({q0})
    Q_D = {initState}
    delta_D = set()
    
    undefDFAStateList = [initState]

    # Line 3
    while undefDFAStateList:
        currentState = undefDFAStateList.pop(0)
        
        for inputSymbol in sigma:
            # Line 4
            nextStateSet = set()
            
            for state in currentState:

                for transFunc in delta_N:
                    
                    funcRel, nextStates = transFunc
                    
                    if funcRel[0] == state and funcRel[1] == inputSymbol:
                        
                        for i in nextStates:
                            
                            nextStateSet.add(i)
            
            newState = frozenset(nextStateSet)

            # Line 5, 6
            if newState not in Q_D:
                Q_D.add(newState)
                undefDFAStateList.append(newState)

            # Line 7
            delta_D.add(((currentState, inputSymbol), newState))

    
    F_D = set() # Line 8
    # Line 9, 10, 11
    for dfaState in Q_D:
        
        accept = False
        
        for state in dfaState:
            if state in F_N:
                accept = True
                break
        
        if accept:
            F_D.add(dfaState)

    # Line 12
    return (Q_D, sigma, delta_D, initState, F_D)


def collectEpsilon(state, delta_N):

    stateCollection = set(state)
    stateTrackingList = list(state)
    
    while stateTrackingList:
        
        currentState = stateTrackingList.pop(0)
        
        for transFunc in delta_N:
            
            funcRel, nextStates = transFunc
            
            if funcRel[0] == currentState and funcRel[1] == "":
                
                for i in nextStates:
                    
                    if i not in stateCollection:
                        
                        stateCollection.add(i)
                        stateTrackingList.append(i)
    
    return frozenset(stateCollection)


def acceptENFA(fiveTuple, string):
    
    Q_N, sigma, delta_N, q0, F_N = fiveTuple

    # Line 1, 2
    initState = collectEpsilon({q0}, delta_N)
    Q_D = {initState}
    delta_D = set()
    
    undefDFAStateList = [initState]

    # Line 3
    while undefDFAStateList:
        currentState = undefDFAStateList.pop(0)
        
        for inputSymbol in sigma:
            # Line 4
            nextStateSet = set()
            
            for state in currentState:

                for transFunc in delta_N:
                    
                    funcRel, nextStates = transFunc
                    
                    if funcRel[0] == state and funcRel[1] == inputSymbol:
                        
                        for i in nextStates:
                            
                            nextStateSet.add(i)
            
            newState = collectEpsilon(nextStateSet, delta_N)

            # Line 5, 6
            if newState not in Q_D:
                Q_D.add(newState)
                undefDFAStateList.append(newState)

            # Line 7
            delta_D.add(((currentState, inputSymbol), newState))

    
    F_D = set() # Line 8
    # Line 9, 10, 11
    for dfaState in Q_D:
        
        accept = False
        
        for state in dfaState:
            if state in F_N:
                accept = True
                break
        
        if accept:
            F_D.add(dfaState)

    # Line 12
    newFiveTuple = (Q_D, sigma, delta_D, initState, F_D)

    currentStringIndex = 0
    
    currentState = newFiveTuple[3]
    
    transFuncList = list(newFiveTuple[2])
    
    
    while currentStringIndex < len(string):
        
        for i in range(len(transFuncList)):
            funcRel = transFuncList[i][0]
            
            if funcRel[0] == currentState and funcRel[1] == string[currentStringIndex]:
                currentState = transFuncList[i][1]
                
                break
        
        currentStringIndex += 1

    if currentState in list(newFiveTuple[4]):
        return True
    else:
        return False

"""
res = convertNFAtoDFA(({"q0", "q1", "q2", "q3"}, {'0', '1'}, {(("q0", '0'), frozenset()), (("q0", '1'), frozenset({"q1", "q2"})), (("q1", '0'), frozenset()), (("q1", '1'), frozenset({"q1"})), (("q2", '0'), frozenset({"q3"})), (("q2", '1'), frozenset()), (("q3", '0'), frozenset()), (("q3", '1'), frozenset({"q2"}))}, "q0", {"q1", "q3"}))

#print(len(res[2]))
"""
"""
#! NFA in Example 4.3 (p.50)
res = convertNFAtoDFA(({"q0", "q1", "q2"}, {'0', '1'}, {(("q0", '0'), frozenset({"q1"})), (("q0", '1'), frozenset()), (("q1", '0'), frozenset({"q2"})), (("q1", '1'), frozenset()), (("q2", '0'), frozenset({"q2"})), (("q2", '1'), frozenset({"q2"}))}, "q0", {"q2"}))

#! Accepting Input string: 00, 0000, 0011, 000111
#! Rejecting Input string: 10101
print(acceptNFA(({"q0", "q1", "q2"}, {'0', '1'}, {(("q0", '0'), frozenset({"q1"})), (("q0", '1'), frozenset()), (("q1", '0'), frozenset({"q2"})), (("q1", '1'), frozenset()), (("q2", '0'), frozenset({"q2"})), (("q2", '1'), frozenset({"q2"}))}, "q0", {"q2"}), "10101"))
print(acceptNFA(({"q0", "q1", "q2"}, {'0', '1'}, {(("q0", '0'), frozenset({"q1"})), (("q0", '1'), frozenset()), (("q1", '0'), frozenset({"q2"})), (("q1", '1'), frozenset()), (("q2", '0'), frozenset({"q2"})), (("q2", '1'), frozenset({"q2"}))}, "q0", {"q2"}), "00"))
print(acceptNFA(({"q0", "q1", "q2"}, {'0', '1'}, {(("q0", '0'), frozenset({"q1"})), (("q0", '1'), frozenset()), (("q1", '0'), frozenset({"q2"})), (("q1", '1'), frozenset()), (("q2", '0'), frozenset({"q2"})), (("q2", '1'), frozenset({"q2"}))}, "q0", {"q2"}), "0000"))
print(acceptNFA(({"q0", "q1", "q2"}, {'0', '1'}, {(("q0", '0'), frozenset({"q1"})), (("q0", '1'), frozenset()), (("q1", '0'), frozenset({"q2"})), (("q1", '1'), frozenset()), (("q2", '0'), frozenset({"q2"})), (("q2", '1'), frozenset({"q2"}))}, "q0", {"q2"}), "0011"))
print(acceptNFA(({"q0", "q1", "q2"}, {'0', '1'}, {(("q0", '0'), frozenset({"q1"})), (("q0", '1'), frozenset()), (("q1", '0'), frozenset({"q2"})), (("q1", '1'), frozenset()), (("q2", '0'), frozenset({"q2"})), (("q2", '1'), frozenset({"q2"}))}, "q0", {"q2"}), "000111"))
"""
"""
print(res[0])
print(res[1])
print(res[2])
print(res[3])
print(res[4])
"""
#! Accepting Input string: 1, 11111, 10, 101010
#! Rejecting Input string: 10101
"""
print(acceptNFA(({"q0", "q1", "q2", "q3"}, {'0', '1'}, {(("q0", '0'), frozenset()), (("q0", '1'), frozenset({"q1", "q2"})), (("q1", '0'), frozenset()), (("q1", '1'), frozenset({"q1"})), (("q2", '0'), frozenset({"q3"})), (("q2", '1'), frozenset()), (("q3", '0'), frozenset()), (("q3", '1'), frozenset({"q2"}))}, "q0", {"q1", "q3"}), "10101"))
print(acceptNFA(({"q0", "q1", "q2", "q3"}, {'0', '1'}, {(("q0", '0'), frozenset()), (("q0", '1'), frozenset({"q1", "q2"})), (("q1", '0'), frozenset()), (("q1", '1'), frozenset({"q1"})), (("q2", '0'), frozenset({"q3"})), (("q2", '1'), frozenset()), (("q3", '0'), frozenset()), (("q3", '1'), frozenset({"q2"}))}, "q0", {"q1", "q3"}), "1"))
print(acceptNFA(({"q0", "q1", "q2", "q3"}, {'0', '1'}, {(("q0", '0'), frozenset()), (("q0", '1'), frozenset({"q1", "q2"})), (("q1", '0'), frozenset()), (("q1", '1'), frozenset({"q1"})), (("q2", '0'), frozenset({"q3"})), (("q2", '1'), frozenset()), (("q3", '0'), frozenset()), (("q3", '1'), frozenset({"q2"}))}, "q0", {"q1", "q3"}), "11111"))
print(acceptNFA(({"q0", "q1", "q2", "q3"}, {'0', '1'}, {(("q0", '0'), frozenset()), (("q0", '1'), frozenset({"q1", "q2"})), (("q1", '0'), frozenset()), (("q1", '1'), frozenset({"q1"})), (("q2", '0'), frozenset({"q3"})), (("q2", '1'), frozenset()), (("q3", '0'), frozenset()), (("q3", '1'), frozenset({"q2"}))}, "q0", {"q1", "q3"}), "10"))
print(acceptNFA(({"q0", "q1", "q2", "q3"}, {'0', '1'}, {(("q0", '0'), frozenset()), (("q0", '1'), frozenset({"q1", "q2"})), (("q1", '0'), frozenset()), (("q1", '1'), frozenset({"q1"})), (("q2", '0'), frozenset({"q3"})), (("q2", '1'), frozenset()), (("q3", '0'), frozenset()), (("q3", '1'), frozenset({"q2"}))}, "q0", {"q1", "q3"}), "101010"))
"""

"""
#! NFA in Example 4.6 (p.52)
print(acceptNFA(
    ({"q0", "q1", "q2", "q3"},
      
     {'0', '1'}, 
     
     {(("q0", '0'), frozenset({})), 
      (("q0", '1'), frozenset({"q1", "q2"})), #! (("q0", '1'), frozenset({"q1"})), (("q0", '1'), frozenset({"q2"}))     ?????
      (("q1", '0'), frozenset({})), 
      (("q1", '1'), frozenset({"q1"})), 
      (("q2", '0'), frozenset({"q3"})), 
      (("q2", '1'), frozenset({})), 
      (("q3", '0'), frozenset({})), 
      (("q3", '1'), frozenset({"q2"}))}, 
     
     "q0", 
     
     {"q1", "q3"}),
     
    "0"))
"""


"""
#! ENFA in Example 4.13 (p.57)
print(acceptENFA(({"q0", "q1", "q2", "q3"}, {'0', '1'}, {(("q0", '0'), frozenset()), (("q0", '1'), frozenset()), (("q0", ""), frozenset({"q1", "q2"})), (("q1", '0'), frozenset({"q1"})), (("q1", '1'), frozenset()), (("q1", ""), frozenset()), (("q2", '0'), frozenset()), (("q2", '1'), frozenset({"q3"})), (("q2", ""), frozenset()),(("q3", '0'), frozenset()), (("q3", '1'), frozenset({"q2"})), (("q3", ""), frozenset())}, "q0", {"q1", "q3"}), ""))

print(acceptENFA(({"q0", "q1", "q2", "q3"}, {'0', '1'}, {(("q0", '0'), frozenset()), (("q0", '1'), frozenset()), (("q0", ""), frozenset({"q1", "q2"})), (("q1", '0'), frozenset({"q1"})), (("q1", '1'), frozenset()), (("q1", ""), frozenset()), (("q2", '0'), frozenset()), (("q2", '1'), frozenset({"q3"})), (("q2", ""), frozenset()),(("q3", '0'), frozenset()), (("q3", '1'), frozenset({"q2"})), (("q3", ""), frozenset())}, "q0", {"q1", "q3"}), ""+"00"))

print(acceptENFA(({"q0", "q1", "q2", "q3"}, {'0', '1'}, {(("q0", '0'), frozenset()), (("q0", '1'), frozenset()), (("q0", ""), frozenset({"q1", "q2"})), (("q1", '0'), frozenset({"q1"})), (("q1", '1'), frozenset()), (("q1", ""), frozenset()), (("q2", '0'), frozenset()), (("q2", '1'), frozenset({"q3"})), (("q2", ""), frozenset()),(("q3", '0'), frozenset()), (("q3", '1'), frozenset({"q2"})), (("q3", ""), frozenset())}, "q0", {"q1", "q3"}), ""+"00000"))

print(acceptENFA(({"q0", "q1", "q2", "q3"}, {'0', '1'}, {(("q0", '0'), frozenset()), (("q0", '1'), frozenset()), (("q0", ""), frozenset({"q1", "q2"})), (("q1", '0'), frozenset({"q1"})), (("q1", '1'), frozenset()), (("q1", ""), frozenset()), (("q2", '0'), frozenset()), (("q2", '1'), frozenset({"q3"})), (("q2", ""), frozenset()),(("q3", '0'), frozenset()), (("q3", '1'), frozenset({"q2"})), (("q3", ""), frozenset())}, "q0", {"q1", "q3"}), ""+"1"))

print(acceptENFA(({"q0", "q1", "q2", "q3"}, {'0', '1'}, {(("q0", '0'), frozenset()), (("q0", '1'), frozenset()), (("q0", ""), frozenset({"q1", "q2"})), (("q1", '0'), frozenset({"q1"})), (("q1", '1'), frozenset()), (("q1", ""), frozenset()), (("q2", '0'), frozenset()), (("q2", '1'), frozenset({"q3"})), (("q2", ""), frozenset()),(("q3", '0'), frozenset()), (("q3", '1'), frozenset({"q2"})), (("q3", ""), frozenset())}, "q0", {"q1", "q3"}), ""+"111"))

print(acceptENFA(({"q0", "q1", "q2", "q3"}, {'0', '1'}, {(("q0", '0'), frozenset()), (("q0", '1'), frozenset()), (("q0", ""), frozenset({"q1", "q2"})), (("q1", '0'), frozenset({"q1"})), (("q1", '1'), frozenset()), (("q1", ""), frozenset()), (("q2", '0'), frozenset()), (("q2", '1'), frozenset({"q3"})), (("q2", ""), frozenset()),(("q3", '0'), frozenset()), (("q3", '1'), frozenset({"q2"})), (("q3", ""), frozenset())}, "q0", {"q1", "q3"}), ""+"11"))
"""
