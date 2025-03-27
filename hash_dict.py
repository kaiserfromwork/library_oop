# Libraries
import hashlib
import time

class HashDict:

    def hash_dict(name, surname):
        unique_id = f"{name}{surname}"
        return hashlib.sha256(unique_id.encode()).hexdigest()
    

    def hash_dict_book(title, author, year):
        unique_id = f"{title}{author}{year}{time.time()}"
        return hashlib.sha256(unique_id.encode()).hexdigest()