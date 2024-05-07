import time, sys, subprocess, random


def get_title():
    project_title = r"""
    888888ba             dP               888888ba  oo          dP         dP      888888ba                    oo       dP                   
    88    `8b            88               88    `8b             88         88      88    `8b                            88                   
    88     88 .d8888b. d8888P .d8888b.    88     88 dP .d8888b. 88d888b. d8888P    88     88 .d8888b. .d8888b. dP .d888b88 .d8888b. 88d888b. 
    88     88 88'  `88   88   88ooood8    88     88 88 88'  `88 88'  `88   88      88     88 88ooood8 88'  `"" 88 88'  `88 88ooood8 88'  `88 
    88    .8P 88.  .88   88   88.  ...    88     88 88 88.  .88 88    88   88      88    .8P 88.  ... 88.  ... 88 88.  .88 88.  ... 88       
    8888888P  `88888P8   dP   `88888P'    dP     dP dP `8888P88 dP    dP   dP      8888888P  `88888P' `88888P' dP `88888P8 `88888P' dP       
                                                            .88                                                                              
                                                        d8888P
        """
    return project_title


def get_data_usage_message():
    """Tells users the danger (or lack thereof) of submitting data"""
    return "**All information submitted is kept secure and is only used internally**"


def print_tagline():
    """Tells users why to use product"""
    print("For when you want to go on a date but you don't want to make the choice on what to do yourself!")


def get_random_index(input_list):
    """Selects random index for choice selection"""
    if len(input_list) == 0:
        return "ERROR: No items in database."
    else:
        return random.randint(0, len(input_list) - 1)


def get_random_movie():  # TO DO ----------------------------------------------------- <
    """returns random movie"""
    return


def movie_menu():
    """Selection menu for movie options"""
    user_movie_input = input("Please type and enter either 1 for add movie, 2 for undo, 3 for view all, 4 to go back, or "
                       "9 for clear all: ")
    while True:
        if user_movie_input == "1":
            return add_movie()
        elif user_movie_input == "2":
            return undo_movie()
        elif user_movie_input == "3":
            return view_all_movies()
        elif user_movie_input == "4":
            return user_main_menu_input()
        elif user_movie_input == "9":
            return clear_all_movies()
        else:
            print("ERROR: Incorrect input. Please try again.")
            movie_menu()


def add_movie():
    movie = input("Please enter name of movie to add: ")
    movies_file = open("movies.txt", "w")
    movies_file.write(movie)
    movies_file.close()
    time.sleep(2)
    print(f"{movie} added to database!")
    return


def undo_movie():  # TO DO --------------------------- <
    return


def view_all_movies():
    return


def clear_all_movies():
    return


def dinner_menu():
    user_dinner_input = input(
        "Please type and enter either 1 for add restaurant, 2 for undo, 3 for view all, 4 to go back, or "
        "9 for clear all: ")
    while True:
        if user_dinner_input == "1":
            return add_dinner()
        elif user_dinner_input == "2":
            return undo_dinner()
        elif user_dinner_input == "3":
            return view_all_dinners()
        elif user_dinner_input == "4":
            return user_main_menu_input()
        elif user_dinner_input == "9":
            return clear_all_dinners()
        else:
            print("ERROR: Incorrect input. Please try again.")
            dinner_menu()


def add_dinner():
    dinner = input("Please enter name of restaurant to add: ")
    dinners_file = open("dinners.txt", "w")
    dinners_file.write(dinner)
    dinners_file.close()
    time.sleep(2)
    print(f"{dinner} added to database!")
    return


def undo_dinner():
    return


def view_all_dinners():
    return


def clear_all_dinners():
    return


def date_menu():
    user_date_input = input(
        "Please type and enter either 1 for add date, 2 for undo, 3 for view all, 4 to go back, or "
        "9 for clear all: ")
    while True:
        if user_date_input == "1":
            return add_date()
        elif user_date_input == "2":
            return undo_date()
        elif user_date_input == "3":
            return view_all_dates()
        elif user_date_input == "4":
            return user_main_menu_input()
        elif user_date_input == "9":
            return clear_all_dates()
        else:
            print("ERROR: Incorrect input. Please try again.")
            date_menu()


def add_date():
    date = input("Please enter name of date to add: ")
    dates_file = open("dates.txt", "w")
    dates_file.write(date)
    dates_file.close()
    time.sleep(2)
    print(f"{date} added to database!")
    return


def undo_date():
    return


def view_all_dates():
    return


def clear_all_dates():
    return


def help_menu():
    return


def user_main_menu_input():
    """Asks for and logs user selection from main menu"""
    user_menu_input = input('Please type and enter either 1 for movie, 2 for dinner, 3 for date, 4 for help, or press Enter to quit: ')
    user_menu_input.lower()
    return user_menu_input


def process_main_menu_selection(user_menu_input):
    if user_menu_input == "":
        return exit_sequence()
    elif user_menu_input == "1" or user_menu_input == "movie":
        return movie_menu()
    elif user_menu_input == "2" or user_menu_input == "dinner":
        return dinner_menu()
    elif user_menu_input == "3" or user_menu_input == "date":
        return date_menu()
    elif user_menu_input == "4" or user_menu_input == "help":
        return help_menu()
    else:
        print("ERROR: Incorrect input. Please try again.")
        return


def exit_sequence():
    """Says bye to user and exits program"""
    print("Thank you! Hope this helped!")
    sys.exit()


if __name__ == "__main__":
    random.seed(1337)
    print(get_title())
    print_tagline()
    print(get_data_usage_message())
    print("\n \n")
    while True:
        user_input = user_main_menu_input()
        process_main_menu_selection(user_input)
