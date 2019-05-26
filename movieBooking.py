movies = {
    'Tarzan':[15,5],
    'Finding Nemo':[12,5],
    'Avengers':[15,5]
}

seats = 0
movieName = None
while True:
    #for i in movies:
        #print('Currently Running:{}\n').format(i)
    
    movieName = input('Enter Your Choice: ').strip()
    age = int(input('How old are you? ').strip())
    seats = movies[movieName][1]
    if(age>=movies[movieName][0]):
        if(seats>0):
            seats -= 1
            print('Enjoy The Movie!')
            movies[movieName][1] = seats
        else:
            print('Housefull!')
    else:
        print('You are too young to watch the movie!')
        
