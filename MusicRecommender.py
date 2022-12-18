#
# Group Project - Music Reccomender
#
# Group Members: Jing Ngo, Collin Shen, Noah Kupershteyn
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
#
# Extra Credit: Show Preferences, Get Recommendations Bug Fix
#

info_file = "musicrecplus.txt"

def main():
    """
    Jing Ngo
    This function is called to run the program. It loads the data of past users in the program, and checks if they are a new user.
    If they are a new, they will be prompted with an input to write in their music preferences, and then taken to the menu.
    If they are not a new user, they will be directly taken to the menu.
    """
    username = input("Enter your name ( put a $ symbol after your name if you wish your preferences to remain private ):")
    user_database = read_users(info_file)
    if username in user_database:
        return menu(username, user_database)
    else:
        preferences = get_preferences(username, user_database)
        user_database[username] = preferences
        return menu(username, user_database)

def read_users(filename):
    """
    takes a file and loads a database with users and their preferred artists and returns a list in the format
    "UserName : Artist1 , Artist2 , Artist3 ,..."
    """
    user_info = {}
    try:
        with open(filename, "r") as f:
            for line in f:
                [username, artist] = line.strip().split(":")
                artist_list = artist.split(",")
                user_info[username] = artist_list
        return user_info
    except:
        f = open(filename, "w")
        f.close()
        return user_info


def menu(username, user_list):
    """
    Jing Ngo, Collin Shen
    """
    while True:
        print("Enter a letter to choose an option:")
        print("e - Enter preferences\nr - Get recommendations\np - Show most popular artists\nh - How popular is the most popular\nm - Which user has the most likes\ns - Show preferences\nq - Save and quit")
        option = input()
        if option == 'e':
            preferences = get_preferences(username, user_list)
            user_list[username]=preferences
        elif option == 'r':
            if get_recommendations(username, user_list)==[]:
                print("No recommendations available at this time.")
            else:
                reccomended = get_recommendations(username, user_list)
                for i in reccomended:
                    print(i)
        elif option == 'p':
            if mostPopularArtist() == []:
              print("Sorry, no user found.")
            else:
                a = mostPopularArtist()
                for i in a:
                  print(i)
        elif option == 'h':
            howPopularIsDaBaby()
        elif option == 'm':
            mostLikes(user_list)
        elif option == 's':
            show_prefs(username, user_list)
        elif option == 'q':
            save_preferences(user_list, info_file)
            exit()
        else:
            print("Please enter a valid letter.")


def get_preferences(username, user_list):
    """
    Jing Ngo
    takes a username and user_list and asks user to input preferred artists. When the user hits enter, 
    it makes a list of their preferences, and then sorts it.
    """
    user_list[username] = []
    new_pref =input("Enter an artist that you like (Enter to finish):\n")
    while new_pref!="":
        if new_pref in user_list[username]:
            continue
        user_list[username].append(new_pref.strip().title())
        new_pref =input("Enter an artist that you like (Enter to finish):\n")
    user_list[username].sort()
    return user_list[username]


def get_recommendations(current, user_list):
    """
    Jing Ngo

    """
    most_similar = similar_user(current, user_list)
    rec_list = []
    for x in user_list[most_similar]:
        if x not in user_list[current]:
            rec_list.append(x)
    rec_list.sort()
    return rec_list


def similar_user(current, user_list):
    '''
    CShen: creates a list of users that share preferences with the current user but are not an exact match.
    then, finds the user with the greatest number of matches 
    '''
    similar = []
    filtered_users = filter(lambda x: "$" not in x, user_list)

    for user_x in filtered_users:
        num_matches = matches(user_list[current], user_list[user_x])
        if num_matches>=1 and num_matches!=len(user_list[current]):
            similar.append([user_x,num_matches])
    #checks for the user with the most amount of num_matches
    max = 0
    maxUser = ""
    for i in similar:
      if i[1] > max:
        max = i[1]
        maxUser = i[0]
    return maxUser


def matches(user1, user2):
    """
    CShen: counts number of shared preferences between two users
    """
    match_num = 0
    for i in user1:
        if i in user2:
            match_num +=1
    return match_num

def mostPopArtistDict():
    '''
    Noah Kupershteyn
    Uses a for loop to coun the nyumber of times an artist appears and then puts it into a dictionary defined as d
    '''
    count = 0
    d = {}
    for i in d:
        if i[-1] !="$":
            for element in d[1]:
                if element in d:
                    d[element] += 1
                else:
                    d[element] = 1
    return d

def mostPopularArtist():
    '''
    Noah Kupershteyn
    Uses the dictionary and a for loop to find the top three artists and display them
    '''
    count = mostPopArtistDict()
    a = 0
    b = 0
    c = 0
    a1 = ''
    b1 = ''
    c1 = ''

    for i in count:
        if count[i]>a or a == '':
            a = count[i]
            a1 = i
            lst[0] = a1
        if count[i]>b or b == '':
            b = count[i]
            b1 = i
            lst[1] = b1
        if count[i]>c or c == '':
            c = count[i]
            c1 = i
            lst[2] = c1
    return lst

def howPopularIsDaBaby(): #I'll finish this when our database is figured out, then I can work on how to address keys in their tuples
    """
    cshen: This function will return the top number of likes each of the top arists has
    """
    Phineas = 0 
    Ferb = ""
    Doof = 0
    Platypus = ""
    Candace = 0
    Flynn = ""

    likeStorage = mostPopArtistDict()
    for perry in likeStorage:

        if likeStorage[perry]>Phineas or Phineas == '':
            Phineas = likeStorage[perry]
            Ferb = perry


        elif likeStorage[perry]>Doof or Doof == '':
            Doof = likeStorage[perry]
            Platypus = perry

        elif likeStorage[perry]>Candace or Candace == '':
            Candace = likeStorage[perry]
            Flynn = perry
    print
    print
    print


def mostLikes(user_list):
    """
    Cshen: filters users with the most likes and returns the top prospect
    """
    filtered_users = filter(lambda x: "$" not in x, user_list)
    highest_num = 0
    best_user = ""

    for i in filtered_users:
        if len(filtered_users[i])>highest_num:
            highest_num = filtered_users[i]
            best_user = filtered_users[i]
    return best_user

  
def show_prefs(username, user_list):
  '''
  Cshen: displays selected users music preferences
  '''
    print(user_list[username])

def save_preferences(user_list, filename):
  '''
  Cshen : saves the users preferences into the file directory.
  '''
    f = open(filename, "w")
    for i in user_list:
        save_pref = str(i) + ":" + ",".join(user_list[i]) + "\n"
        f.write(save_pref)
    f.close()
