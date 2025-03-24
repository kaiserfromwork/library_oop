import hashlib

class HashDict:

    def hash_dict(name, surname):
        unique_id = f"{name}{surname}"
        return hashlib.sha256(unique_id.encode()).hexdigest()