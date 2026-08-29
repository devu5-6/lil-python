def calculate_love_score(x,y):
    count=0
    count2=0
    letters =list((x+y).replace(' ','').lower())
    print(letters)

    count = letters.count('t') + letters.count('r') + letters.count('u') + letters.count('e')
    count2 = letters.count('l') + letters.count('o') + letters.count('v') + letters.count('e')
    print(f"{count}{count2}")
    
calculate_love_score("Kanye West", "Kim Kardashian")