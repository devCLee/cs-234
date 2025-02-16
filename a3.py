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
