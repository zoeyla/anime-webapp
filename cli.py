from api import AnimeAPI
import os


def main():
    choice = ""
    
    animeAPI = AnimeAPI()

    while choice != "q":
        print("\nWelcome to the anime central hub!")
        print("Please select from the following options:")
        print("(a) : Find one or more animes based on a given genre")
        print("(b) : Find one or more animes based on a given average score")
        print("(c) : Find one or more animes based on a given number of episodes")
        print("(d) : Find the genre of a specific anime")
        print("(e) : Find the average user rating score of a specific anime")
        print("(f) : Find the number of episodes of a specific anime")
        print("(g) : Find the synopsis of a specific anime")
        print("(h) : Find one or more animes based on a given average score range")
        print("(i) : Find one or more animes based on a given number of episodes range")
        print("(q) : Quit this program")
        print("")
        choice = input("Make your selection: ")

        if choice not in ["a", "b", "c", "d", "e","f","g","q","h","i"]:
            print("Input a valid option.")
            
        if choice == "a":
            genre_input = input("Enter genre(s) of anime you're looking for (separated by commas): ")
            genre_list = genre_input.split(",")
            genres = []
            for genre in genre_list:
                stripped_genre = genre.strip()
                capitalized_genre = stripped_genre.capitalize()
                genres.append(capitalized_genre)
            anime = animeAPI.getTitleofAnimefromGenre(genres)
            if not anime:
                print("\nNo anime found with the given genre(s).")
            else:
                print("\nThe anime you're looking for is/are:")
                for title in anime:
                    print("- " + str(title))


        elif choice == "b":
            score = input("Enter the average rating for an anime you're looking for: ")
            score2 = str(float(score))
            anime = animeAPI.getTitleofAnimefromScore(score2)

            if not anime:
                print("\nThere is no anime found with this given score.")
            else:
                print("\nThe anime you're looking for is/are:")
                for title in anime:
                    print("- " + title)

        elif choice == "c":
            episodes = input("Enter the number of episodes for an anime you're looking for: ")
            episodes2 = str(int(episodes))
            anime = animeAPI.getTitleofAnimefromNumberOfepisodes(episodes2)
        
            if not anime:
                print("\nThere is no anime found with this given amount of episodes.")
            else:
                print("\nThe anime you're looking for is/are:")
                for title in anime:
                    print("- " + title)

        elif choice == "d":
            anime = input("Enter title of anime: ")
            expectedInput = anime.lower()            
            genre = animeAPI.getGenre(expectedInput)

            if genre is None:
                print("Sorry we could not recognize the anime you input")
            else:
                print("\nThe anime is of the following genre: " + genre[0])

        elif choice == "e":
            anime = input("Enter title of anime: ")
            expectedInput = anime.lower()            
            score = animeAPI.getScoreofAnime(expectedInput)

            if score is None:
                print("Sorry we could not recognize the anime you input")
            else:
                print("\nThe anime, " + anime + ", gets an average user rating score of " + str(score[0]) + ".")

        elif choice == "f":
            anime = str(input("Enter title of anime: "))
            expectedInput = anime.lower()            
            numOfEpisodes = animeAPI.getNumberofEpisodes(expectedInput)
            if numOfEpisodes is None:
                print("Sorry we could not recognize the anime you input")
            else:
                print("The anime, " + anime + ", has " + str(numOfEpisodes[0]) + " episodes.")

        elif choice == "g":
            anime = input(str("Enter title of anime: "))        
            synopsis = animeAPI.getSynopsis(anime)
            if synopsis is None:
                print("Sorry we could not recognize the anime you input")
            else:
                print("\nThe anime, " + anime + "'s synopsis that you requested is as follow: ")
                print("'" + str(synopsis[0]) + "'")

        elif choice == "h":
            score_range = input("Please enter a score range separated by a comma (e.g. 7.5,8.5): ")
            anime = animeAPI.getTitleofAnimefromScoreRange(score_range)

            if not anime:
                print("\nThere is no anime found within the given score range.")
            else:
                print("\nThe anime you're looking for is/are:")
                for title in anime:
                    print("- " + title)

        elif choice == "i":
            episodes_range = input("Please enter an episode range separated by a comma: ")
            anime = animeAPI.getTitleofAnimefromNumberOfepisodesRange(episodes_range)

            if not anime:
                print("\nThere is no anime found within the given episode range.")
            else:
                print("\nThe anime you're looking for is/are:")
                for title in anime:
                    print("- " + title)

  
if __name__ == "__main__":
    main()