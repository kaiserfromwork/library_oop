import hashlib

class HashDict:

    def __init__(self, name, surname):
        unique_id = f"{name}{surname}"
        return hashlib.sha256(unique_id.encode()).hexdigest()