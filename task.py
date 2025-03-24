#created a function for checking non repeating characeters
#functtion taking value from parameter text 
def nonrepeatingchar(text):
    for i in text:      #first for loop checks all the characters in string
        count = 0       #initilaze value of count variable as 0
        for j in text:  #second for loop checks the characters again and if its repeating increseas the  value of count by 1
            if i == j:
                count += 1
        if count == 1:
            return i    #if condition checks it if count is 1 then returns i and non repeating char is printed
    return None

# Test cases
print(nonrepeatingchar("swiss"))    # Output: 'w'
print(nonrepeatingchar("assam"))    # Output: 's'
print(nonrepeatingchar("porsche"))  # Output: 'p'
print(nonrepeatingchar("aabbcc"))   # Output: None