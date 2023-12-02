def getFile(file_name):
    with open(file_name, 'r') as f:
        return f.readlines()

def firstPart(input_):
    
    total = 0
    for line in input_:
        digits = [0, 0]
        first_digit_flag = True
        for i, char in enumerate(line):
            if (ord(char) >= 48 and ord(char) <= 57) and first_digit_flag == True:
                digits[0] = ord(char)-48
                first_digit_flag = False
            if (ord(char) >= 48 and ord(char) <= 57) and first_digit_flag == False:
                digits[1] = ord(char)-48
        total += digits[0]*10 + digits[1]
    return total

def secondPart(input_):
    numbers_tree = {'z':(('ero', 3, 0),), 'o':(('ne', 2, 1),), 't':(('wo', 2, 2), ('hree', 4, 3)), 'f':(('our', 3, 4), ('ive', 3, 5)), 's':(('ix', 2, 6), ('even', 4, 7)), 'e':(('ight', 4, 8),), 'n':(('ine', 3, 9),)}
    
    total = 0
    for i, line in enumerate(input_):
        s = 0
        digits = [0, 0]
        first_digit_flag = True
        while(s < len(line)):
            
            #Check if char is a number while there is no first digit
            if (ord(line[s]) >= 48 and ord(line[s]) <= 57) and first_digit_flag == True:
                digits = [ord(line[s])-48, ord(line[s])-48]
                first_digit_flag = False
                
            #Check if the char is a string while there is no first digit
            elif line[s] in numbers_tree and first_digit_flag == True:
                for node in numbers_tree[line[s]]:
                    #Does the check for the entire word, if true, assign digits and increase s for the number of chars in the number string
                    if(line[s+1:s+node[1]+1] == node[0]):
                        digits = [node[2], node[2]]
                        first_digit_flag = False
            
            #Check if the char is a number for the second digit
            elif (ord(line[s]) >= 48 and ord(line[s]) <= 57) and first_digit_flag == False:
                digits[1] = ord(line[s])-48
                
            #Check if the char is a string for the second digit
            elif line[s] in numbers_tree and first_digit_flag == False:
                for node in numbers_tree[line[s]]:
                    if(line[s+1:s+node[1]+1] == node[0]):
                        digits[1] = node[2]
            
            s += 1
        total += digits[0]*10 + digits[1]
    return total
    
ipt = getFile('day_1_input_file.txt')
#print(firstPart(ipt))
print(secondPart(ipt))
            
            
