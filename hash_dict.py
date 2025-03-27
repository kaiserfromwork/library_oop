# Libraries
import hashlib
import time

class HashDict:

    def hash_dict(name, surname):
        """Creates a hash string id using user's name and surname
        
        Keyword arguments:
            name (str) - user's name
            surname (str) - user's surname
        
        Return: 
            Returns a hash unique id
        """
        
        unique_id = f"{name}{surname}"  # String used to create unique hash id
        return hashlib.sha256(unique_id.encode()).hexdigest()
    

    def hash_dict_book(title, author, year):
        """Creates a hash string using book's title, author and year. Used as ID
        
        Keyword arguments:
            title (str) -- book's title
            author (str) -- book's author
            year (str) -- book's year

        Return: 
            Returns a hash string unique id
        """
        
        unique_id = f"{title}{author}{year}{time.time()}" # string used to create unique hash id
        return hashlib.sha256(unique_id.encode()).hexdigest()