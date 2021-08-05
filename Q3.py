inp = list(input().split())

def countingValleys(inp):
    level = 0
    valleys = 0
    for direction in inp:
        if direction == "U":
            level += 1
            if level == 0:
                valleys += 1
        else:
            level -= 1
             
    return valleys

if __name__ == "__main__":
    print(countingValleys(inp))
    

        
        
    
    
    
