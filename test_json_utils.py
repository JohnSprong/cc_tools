import test_data
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()

    for game_data in json_data["games"]:
            #  The loop steps through each element in the list (here the list is kids_data)
            #  and the variable kid_data represents the current element in the list
            # Make a new Kid
        gameobject = test_data.Game()
        gameplatform = test_data.Platform()
            # Get the data from from the current kid in the kids_data list
        gameobject.title = game_data["title"]
        gameobject.year = game_data["Year"]
        gameplatform.launch_year = game_data["platform"]["launch year"]
        gameplatform.name = game_data["platform"]["name"]
        gameobject.platform = gameplatform
        game_library.add_game(gameobject)


    #Loop through the json_data
        #Create a new Game object from the json_data by reading
        #  title
        #  year
        #  platform (which requires reading name and launch_year)
        #Add that Game object to the game_library
    #Return the completed game_library

    return game_library
