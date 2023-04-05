# spidey_cracker

# About:

This is a Python script that can be used for cracking password hashes using various hash algorithms. The script uses the hashlib library to generate the hash objects and pyfiglet library to generate the ASCII banner.

When the script is executed, it prompts the user to select a hash algorithm from a list of available options (MD5, SHA1, SHA224, SHA512, SHA256, SHA384). It then asks for the location of a wordlist file that will be used to generate candidate passwords, and the hash value that needs to be cracked.

The script reads the wordlist file and generates a hash object for each word in the list using the selected hash algorithm. It then compares the generated hash with the target hash and if there is a match, the password is printed to the screen.

The script is suitable for ethical hacking and penetration testing purposes, but it can also be used for malicious purposes. Therefore, it should only be used with proper authorization and in compliance with applicable laws and regulations.


# installation

# 1 install git:
    ( apt install git )
 ![IMG_20230405_143529](https://user-images.githubusercontent.com/122730895/230036308-462f9a68-71ca-4d4a-9b67-36895c5ee65e.png)
    
    
# 2 cmd: git clone ( copy paste the given code )    

# 3 cd spidey_cracker

# 4 python3 spidey.py

# 5 Enter the hash  type 

# 6 mention the path of wordlist

# 7 and finally input the hash value.
