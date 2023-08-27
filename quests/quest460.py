
def checkio(game):
    
    columns = game[0][0] + game[1][0] + game[2][0], game[0][1] + game[1][1] + game[2][1], game[0][2] + game[1][2] + game[2][2]
    diagonal = game[0][0] + game[1][1] + game[2][2], game[0][2] + game[1][1] + game[2][0]
    
    for line in game:
        if line != "..." and len(set(line)) == 1:
            return line[0]
    
    for line in columns: 
        if  line != "..." and len(set(line)) == 1:
            return line[0]
    
    for line in diagonal: 
        if line != "..." and len(set(line)) == 1:
            return line[0]
        
    return 'D'
    
    
    
