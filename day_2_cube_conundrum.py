import math

def getFile(file_name):
    with open(file_name, 'r') as f:
        return f.readlines()

def firstPart(input_):
    possible = {'red':12, 'green':13, 'blue':14}
    total = 0
    for i, line in enumerate(input_):
        
        #flag in case there is a draft that makes the game impossible
        impossible = False
        #Discards the beginning ot the sentence and divides for each game
        for game in line[7+len(str(i))::].strip().split(';'):
        
            draft = {'red':0, 'green':0, 'blue':0}
            #This is the draft array but each element is a string so it will be turned into an array.
            for k in game.strip().split(','):
                draft_l = [j for j in k.strip().split(' ')]
                #Puts the values onto the dictionary of the draft.
                draft[draft_l[1]] = int(draft_l[0])

            #Check if draft made game impossible.
            if draft['red'] > possible['red'] or draft['green'] > possible['green'] or draft['blue'] > possible['blue']:
                impossible = True
        #Counts if the game is possible
        if not impossible:
            total += i+1
        
    return total

def secondPart(input_):
    possible = {'red':12, 'green':13, 'blue':14}
    total = 0
    for i, line in enumerate(input_):
        
        #the powerof the game (multipling all minimums)
        power = 0
        #Draft of minimums
        draft = {'red':0, 'green':0, 'blue':0}
        #Discards the beginning ot the sentence and divides for each game
        for game in line[7+len(str(i))::].strip().split(';'):

            #This is the draft array but each element is a string so it will be turned into an array.
            for k in game.strip().split(','):
                draft_l = [j for j in k.strip().split(' ')]
                
                #Checks if the value is lower than the current draft minimum and puts there if it is.
                if(int(draft_l[0]) > draft[draft_l[1]]):
                    draft[draft_l[1]] = int(draft_l[0])
        print(f'Game {i+1}: {draft}')
        total += draft['red']*draft['blue']*draft['green']
        
    return total
    
ipt = getFile('day_2_input_file.txt')
#print(firstPart(ipt))
print(secondPart(ipt))
            
            
