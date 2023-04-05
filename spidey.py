import hashlib
import sys
import pyfiglet

ascii_banner = pyfiglet.figlet_format("SPIDEY HASH CRACKER")
print(ascii_banner)

welcoming = input("welcome to the spidey world: ")

print("Algorithms available: MD5 | SHA1 |  SHA224 | SHA512 | SHA256 | SHA384")

hash_type = input("Enter hash type? ")
wordlist_location = input("enter wordlist location: ")
hashed_password = input("enter encryptiony: ")

word_list = open(wordlist_location, "r", encoding='utf-8', errors='ignore').read().splitlines()

if hash_type == "MD5":
     for word in word_list:
         hash_object = hashlib.md5(word.encode('utf-8'))
         hash_digest = hash_object.hexdigest()
         if hashed_password == hash_digest:
            print(f"\033[1;32m HASH FOUND: {word} \n")
            break
elif hash_type == "SHA1":
     for word in word_list:
         hash_object = hashlib.sha1(word.encode('utf-8'))
         hash_digest = hash_object.hexdigest()
         if hashed_password == hash_digest:
            print(f"\033[1;32m HASH FOUND: {word} \n")
            break
elif hash_type == "SHA224":
     for word in word_list:
         hash_object = hashlib.sha224(word.encode('utf-8'))
         hash_digest = hash_object.hexdigest()
         if hashed_password == hash_digest:
            print(f"\033[1;32m HASH FOUND: {word} \n")
            break
elif hash_type == "SHA512":
     for word in word_list:
         hash_object = hashlib.sha512(word.encode('utf-8'))
         hash_digest = hash_object.hexdigest()
         if hashed_password == hash_digest:
            print(f"\033[1;32m HASH FOUND: {word} \n")
            break
elif hash_type == "SHA256":
     for word in word_list:
         hash_object = hashlib.sha256(word.encode('utf-8'))
         hash_digest = hash_object.hexdigest()
         if hashed_password == hash_digest:
            print(f"\033[1;32m HASH FOUND: {word} \n")
            break
elif hash_type == "SHA384":
     for word in word_list:
         hash_object = hashlib.sha384(word.encode('utf-8'))
         hash_digest = hash_object.hexdigest()
         if hashed_password == hash_digest:
            print(f"\033[1;32m HASH FOUND: {word} \n")
            break
else:
    print("please choose from the given option.")
