import uuid
import json
import pprint

# Location ID Dictionary
global location_ids
location_ids = {}


class Identification:
    """ An Identification object that generates an ID for a given location. This is used
    to identify the location in place of it's name throughout the program.

    Attributes:
        location: Holds the given location for the object
        identification: Holds the ID number of the location

    """

    def __init__(self, location):
        self.location = location
        self.identification = " "

    def return_id(self):
        return self.identification

    @staticmethod
    def print_dict():
        pprint.pprint(location_ids)

    def return_location(self):
        return self.location

    @staticmethod
    def choice_check(choice):
        if choice == "":
            choice = 'y'
        while choice != 'y' or 'n':
            choice = input("Please enter only y or n: ")
        return choice

    @staticmethod
    def write_dict():  # writes changes to the dictionary file
        with open('LocationDictionary.json', 'w') as f:
            json.dump(location_ids, f)

    @staticmethod
    def read_dict():  # Refreshes ID Dictionary from file
        Identification.write_dict()
        with open('LocationDictionary.json') as f:
            global location_ids
            location_ids = json.load(f)

    def get_existing_id(self, query):
        self.read_dict()
        return location_ids.get(query, default=None)

    def add_to_dict(self, location, id_num):  # Adds locations and their new IDs to the ID Dictionary
        self.read_dict()
        global location_ids
        if id_num in location_ids:
            return 1

        if location in location_ids:
            return 1

        global location_ids
        location_ids.update({location: id_num})
        self.write_dict()
        return 0

    @staticmethod
    def lookup(query):  # searches the dictionary for given variable
        Identification.read_dict()
        choice = 'y'
        while choice == 'y':
            if query in location_ids:
                print()
            if query not in location_ids:
                print(str(query) + " is not in the dictionary!")
                choice = input("Would you like to search again? (y/n)")
                choice = Identification.choice_check(choice)

    @staticmethod
    def quick_check(query):
        if query in location_ids:
            return True
        else:
            return False

    def generate_id(self):          # Generates a new id, if one for that location already exists, it returns it's ID
        location = self.location    # Gets the objects location
        preexists = self.quick_check(location)   # Checks if it exists already
        new_id = ""
        if not preexists:               # If it doesn't exist, generate an ID.
            check = 1                        # value will change on outcome of add_to_dict
            print("Generating ID...")
            while check == 1:
                new_id = str(uuid.uuid4())[:6]  # Creates a new random alphanumeric ID 7 characters long
                print(new_id)
                check = self.add_to_dict(location, new_id)  # Check is add_to_dict outcome.
                if check == 1:  # If check is still equal to 1, notify user of error and regenerate ID
                    print("Error: Duplicate ID exists!")
                    print("Generating new ID...")
                if check == 0:  # If check is 0, break the loop
                    break
            print("The identification number for " + location + " is: " + new_id)
            return new_id       # Return the new ID
        if preexists:
            print("This location already has an ID")
            new_id = self.get_existing_id(location)
            print("The identification number for " + location + " is: " + new_id)
            return new_id   # If the ID exists, return it.

