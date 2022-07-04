import random, operator

authenticated_users = {"user_1": "password1", "user_2": "password2", "user_3": "password3", "user_4": "password4", "user_5": "password5"} #a dictionary of all the authentic users that can log in saved under the name authenitcated_users
songs = {}
score = 0

file = open("Other\GCSE_NEA\songs.txt") #Open the external file named songs.txt
for line in file:
    key, value = line.split(',')
    songs[key] = value.strip() #Save the data of the external file to a dictionary

while True:
    user = str(input('Username: '))
    user_password = str(input('Password: '))

    if user in authenticated_users and user_password == authenticated_users[user]: #Check if user is authentic
        guesses = 0
        score = 0

        items = list(songs.items())  # List of tuples of (key,values)
        random.shuffle(items)

        current_song = next(iter(items)) #Select the song

        while guesses != 2: #Make sure you can only get 2 incorrect guesses
            guesses += 1
            song_name = current_song[0]
            first_name_letter, song_artist = str(current_song[0])[0], str(current_song[1])
            print(f"First letter of the song: {first_name_letter} \nArtist = {song_artist}")
            guess = str(input('Your guess of the name of the song: '))

            if guess.lower() == song_name.lower() and guesses == 1: #If the guess is correct first try
                score += 3
                print(f"Correct! score: {score}")
                random.shuffle(items)
                current_song = next(iter(items))
                guesses = 0
                continue

            if guess.lower() == song_name.lower() and guesses != 1: #If the guess is correct the second time
                score += 1
                print(f"Correct! score: {score}")
                random.shuffle(items)
                current_song = next(iter(items))
                guesses = 0
                continue

            else: #If the guess is wrong
                print('Try Again')

        print(f"Game Over, you got it wrong 2 times in a row! The correct answer was {str(current_song[0])}. You scored: {score}!") #End the game

        username = str(input('Nickname that you want displayed on the leaderboard: '))
        with open(f"Other\GCSE_NEA\scores.txt", 'a') as file: #opens the external file scores.txt and saves the score of the person
            file.write(f"\n{username}-{score}")
            file.close()

        file = open("Other\GCSE_NEA\scores.txt") 
        lb = {}
        for line in file:
            if line == '\n':
                pass
            else:
                key, value = line.split('-')
                lb[key] = int(value.strip())
        sorted_lb = dict(sorted(lb.items(), key=lambda item: item[1], reverse=True)) #sorts the leaderboard dictionary
        if len(sorted_lb) >= 5:
            print({k: sorted_lb[k] for k in list(sorted_lb)[:5]})
        if len(sorted_lb) < 5:
            print(sorted_lb)

    else:
        print(f"{user} is not authenticated") #printed if the user is not in the authenticated_users dictionary