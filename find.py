#!/usr/bin/python3

import sys
import hashlib




def findText(pattern,stringText):
    """
        This function use open addresing algorithms
        (karp-rabin) to find patern in string text.
        
        This function find the exact match of patern in 
        text and return starting index.
    """
    
    if(pattern == "" or stringText == ""):
        return -1
    
    pattern_hash = hashlib.sha256(pattern.encode()).hexdigest()
    
    pattern_length = len(pattern)
    
    for i in range(len(stringText)):
        check_hash = hashlib.sha256(stringText[i:i+pattern_length].encode()).hexdigest()
        
        if(check_hash == pattern_hash):
            return i
        
    return -1
    





if __name__ == '__main__':
    if(len(sys.argv) <3):
        print("Example usage:\npython3 find.py [file name] [string to find]")
    else:
        with open(sys.argv[1], "r") as file:
            stringText =  file.read()
        
        pattern = sys.argv[2]
        
        index = findText(pattern,stringText)
        print("String Found")
        print(pattern + " ---------> " + str(index))
        
        
    



    
    




    
    
