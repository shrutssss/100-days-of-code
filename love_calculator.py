def calculate_love_score(name1,name2):
    n1=0
    n2=0
    score1=0
    score2=0
    name1.lower()
    name2.lower()
    T="true"
    L="love"
    true_list=list(T)
    love_list=list(L)
    letters1=list(name1)
    letters2=list(name2)
    letters1+=letters2
    for i in letters1:
        for j in true_list:
            if i==j:
                score1+=1
        for k in love_list:
            if i==k:
                score2+=1
    print(f"{score1}{score2}")


calculate_love_score("Kanye West", "Kim Kardashian")                

    