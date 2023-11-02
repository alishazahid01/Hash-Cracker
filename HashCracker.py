# Hash Cracker / password cracker
import hashlib

# Decorator for printing messages
def print_message(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"{func.__name__} completed.")
        return result
    return wrapper


# HashCracker Class
class HashCracker:

    # Constructor 
    def __init__(self, hash_file, password_file, cracked_pass):
        self.hash_file = hash_file
        self.password_file = password_file
        self.cracked_pass = cracked_pass
        self.hashes = None
        self.passwords = None
      
    # Password and hash file reading
    @print_message
    def hash_file(self):
        # Reading hash_file 
        try:
            with open(self.hash_file, "r") as hash_file:
                self.hashes = hash_file.read().splitlines()
        except FileNotFoundError:
            print("Hash File not Found")
        
    @print_message 
    def wordlist_file(self):
        # Reading Wordlist file 
        try:
            with open(self.password_file, "r") as pwd_file:
                self.passwords = pwd_file.read().splitlines()
        except FileNotFoundError:
            print("Passwords/wordlist file not Found")
    
    # Cracking hashes 
    @print_message
    def hash_crack(self):
        for password in self.passwords:
            for algorithm in ["md5", "sha1", "sha256"]:
                hash_object = hashlib.new(algorithm)
                hash_object.update(password.encode('utf-8'))
                hashed_password = hash_object.hexdigest()
                
                if hashed_password in self.hashes:
                    with open(self.cracked_pass, "w") as cracked_pwd:
                        cracked_pwd.write(password)
                    print("Password Found Successfully :)")
                    return
        print("Password cracking completed. No matching password found.")


if __name__ == "__main__":
    hash_file = "pwd_hash.txt"
    password_file = "pwd_dict.txt"
    cracked_pass = "cracked_pass.txt"

    class_obj = HashCracker(hash_file, password_file, cracked_pass)
    class_obj.hash_file()
    class_obj.wordlist_file()
    class_obj.hash_crack()
