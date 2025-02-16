"""
Purpose: Solution for assignment 2 - Part 2
Author: Daniel Lee
Date: January 31, 2025
CS 234, Spring 2025
"""

#! print(isFun({((1,1), 2), ((1,1), 4), (5, 6)}))

#! {'0', '1'} or {0, 1}
#! ({"q0", "q1", "q2"}, {'0', '1'}, {(("q0", '0'), "q0"), (("q0", '1'), "q1"), (("q1", '0'), "q2"), (("q1", '1'), "q0"), (("q2", '0'), "q1"), (("q2", '1'), "q2")}, "q0", {"q0"})
#! Accepting Input string: 11, 1001, 10101
#! Rejecting Input string: 1, 10, 1010, 10100


#fiveTuple = ({"q0", "q1", "q2"}, {'0', '1'}, {(("q0", '0'), "q0"), (("q0", '1'), "q1"), (("q1", '0'), "q2"), (("q1", '1'), "q0"), (("q2", '0'), "q1"), (("q2", '1'), "q2")}, "q0", {"q0"})

#string = "11"

def acceptDFA(fiveTuple, string):

    currentStringIndex = 0
    
    currentState = fiveTuple[3]
    
    transFuncList = list(fiveTuple[2])
    
    
    while currentStringIndex < len(string):
        
        for i in range(len(transFuncList)):
            funcRel = transFuncList[i][0] #! (('q0', '1'), 'q1')[0] == ('q0', '1')
            
            print(funcRel)
            
            if funcRel[0] == currentState and funcRel[1] == string[currentStringIndex]:
                currentState = transFuncList[i][1]
                print("found!")
                print(currentState)
                print("\n")
                
                break
        
        currentStringIndex += 1

    if currentState in list(fiveTuple[4]):
        return True
    else:
        return False


fiveTuple = ({"q0", "q1", "q2"}, {'0', '1'}, {(("q0", '0'), "q0"), (("q0", '1'), "q1"), (("q1", '0'), "q2"), (("q1", '1'), "q0"), (("q2", '0'), "q1"), (("q2", '1'), "q2")}, "q0", {"q0", "q1"})
print("q0" in list(fiveTuple[4]))


print(frozenset({}))

# print(len(({"q0", "q1", "q2"}, {'0', '1'}, {(("q0", '0'), "q0"), (("q0", '1'), "q1"), (("q1", '0'), "q2"), (("q1", '1'), "q0"), (("q2", '0'), "q1"), (("q2", '1'), "q2")}, "q0", {"q0"})))
#! DFA for binary divisibility by three (p.30)
# print(acceptDFA(({"q0", "q1", "q2"}, {'0', '1'}, {(("q0", '0'), "q0"), (("q0", '1'), "q1"), (("q1", '0'), "q2"), (("q1", '1'), "q0"), (("q2", '0'), "q1"), (("q2", '1'), "q2")}, "q0", {"q0"}), "10101"))

#! Accepting Input string: 11, 1001, 10101
#! Rejecting Input string: 1, 10, 1010, 10100


#! DFA for a vending machine (p.23)
#print(acceptDFA(({"q0", "q5", "q10", "q15", "q20"}, {'N', 'D'}, {(("q0", 'N'), "q5"), (("q0", 'D'), "q10"), (("q5", 'N'), "q10"), (("q5", 'D'), "q15"), (("q10", 'N'), "q15"), (("q10", 'D'), "q20"), (("q15", 'N'), "q20"), (("q15", 'D'), "q20"), (("q20", 'N'), "q20"), (("q20", 'D'), "q20")}, "q0", {"q20"}), "NDN"))

#! Accepting Input string: NDN, DD, DDDD, NDND, DND
#! Rejecting Input string: NN, ND, NNN, DN


