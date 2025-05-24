
rejectState = "REJECT"




def removeTrailingBlanks(tape, blank):
    '''
        INPUT:
            tape --- a list of length-1 strings
            blank --- the length-1 string representing the blank symbol
        
        OUTPUT:
            tape but with trailing blanks removed
    '''
    newTape = tape[:]
    while len(newTape) > 0 and newTape[-1] == blank:
        newTape.pop(-1)
    return newTape




def stepTM(tm, config):
    '''
        INPUT:
            tm --- a Turing machine 7-tuple 
            config --- a Turing machine configuration 4-tuple
        
        OUTPUT:
            the next configuration of the machine
    '''
    
    pass #TODO
       



def runTM(tm, inString):
    '''
        INPUT:
            tm --- a Turing machine 7-tuple 
            inString --- the input string to the Turing machine
        
        OUTPUT:
            True if tm accepts inString
            False if tm rejects inString
            runs forever if tm runs forever on inString
    '''

    pass #TODO




# example 13.1 from the textbook
zeroNoneN = (
    {0,1,2,3,4}, #states
    {"0", "1"}, #input alphabet
    {"0", "1", " "}, #tape alphabet
    { # transition function
        ((0," "),(4," ","R")),
        ((0,"0"),(1," ","R")),
        ((1,"0"),(1,"0","R")),
        ((1,"1"),(1,"1","R")),
        ((1," "),(2," ","L")),
        ((2,"1"),(3," ","L")),
        ((3,"1"),(3,"1","L")),
        ((3,"0"),(3,"0","L")),
        ((3," "),(0," ","R"))
    },
    0, # start state
    " ", # blank symbol
    {4} # accepting states
)


# example 13.12 from the textbook
inc = (
    {0,1,2}, #states
    {"0", "1"}, #input alphabet
    {"0", "1", " "}, #tape alphabet
    { # transition function
        ((0,"0"),(0,"0","R")),
        ((0,"1"),(0,"1","R")),
        ((0," "),(1," ","L")),
        ((1,"1"),(1,"0","L")),
        ((1,"0"),(2,"1","R")),
        ((1," "),(2,"1","R")),
    },
     0, # start state
    " ", # blank symbol
    {2} # accepting states
)