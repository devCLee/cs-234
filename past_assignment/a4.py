"""
Purpose: Solution for assignment 4 - Part 2
Author: Daniel Lee
Date: February 23, 2025
CS 234, Spring 2025
References: https://docs.python.org/3/library/re.html
"""
import re

def findPhones(text):
    
    #result = re.findall(r"\({,1}\d{3}\){,1}(?:[\-\. ]{,1})\d{3}(?:[\-\. ]{,1})\d{4}", text) #! (?:[\-\.\s]{,1}) ???
    result = re.findall(r"\d{3}(?:[\-\. ]{,1})\d{3}(?:[\-\. ]{,1})\d{4}|\({1}\d{3}\){1}(?:[\-\. ]{,1})\d{3}(?:[\-\. ]{,1})\d{4}", text) #! (?:[\-\.\s]{,1}) ???

    print(result)
    
    return result

#! 1-234567890 (123-456-7890   123)-456-7890

#! assert findPhones("(123-456-7890") == []
#! assert findPhones("+1-123-456-7890") == []
#! assert findPhones("123-456-7890 abc") == []

#findPhones("(123)456-7890123-456-7890(123).45678901-234567890123)-456-7890123 456 7890(123-456-78901234567890")

findPhones("(123) 456-7890 123-456 7890 (123) 4567890 1-234567890 123)-456-7890 123 456 7890 (123 456-7890 1234567890 +1-123-456-7890 123-456-7890 abc")

def findEmails(text):
    
    #! empty string at the start and end of the email???
    result = re.findall(r"[\w\-]+(?:\.[\w\-]+)*@[\w\-]+(?:\.[\w\-]+)*", text)  #! behaviour of (?:R), (?:R)* ???
    
#! [.@]{0}[\w-]+(?:\.[\w-]+)*@[\w-]+(?:\.[\w-]+)*[.@]{0} ???
    print(result)
    
    return result

#! findEmails("username@domain.co.ukusername@domain.co.ukusername@domain.co.ukusername@domain.co.uk")
#! findEmails("username@domain")


text = "@$$$: -a-@-a-, .user@domain.com, user@domain.com., user..name@domain.com, test.user+user@domain.co.uk, invalid@.com, valid.email@domain.co.uk, @domain.co.uk, user@domain..com, user@domain.co!.uk"
#! print(findEmails(text))  # Output: ['valid.email@domain.co.uk']


#findEmails(text)