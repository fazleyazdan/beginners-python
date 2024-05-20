# here in this task we will generate different types of hashes for a file

''' In simple terms, a hash is like a fingerprint for data. Just as each person has a unique fingerprint, 
each piece of data (like a file or a piece of text) has a unique hash. 

Imagine you have a magic machine that takes any object you give it—let's say a book—and it squishes it down into a small, 
fixed-size piece of metal. No matter how big the book is, the piece of metal is always the same size. 
This piece of metal is the hash.

Now, if you change even a tiny bit of the book—like adding or removing a single word—the hash will look completely different.
It's as if changing one word in the book would completely change the shape of the piece of metal.

So, hashes are used to verify if data has changed. For example, if you download a file from the internet, you can calculate its hash and compare it to the hash provided by the original source. If they match, it means the file is exactly the same as when it was originally created. 
If they don't match, it means the file has been altered in some way.

Hash cannot be reversed to retrieve the original data.
'''

import hashlib
from munch import Munch

def hash_file(file_path: str) -> Munch:
    
    #* the arrow in function definition shows that its return type is 'munch'
    #* file_path: str : means that file_path should be in string format
    
    """
    Generate hashes of a file using multiple hash algorithms.

    Args:
        file_path (str): Path to the file.

    Returns:
        Munch: A Munch object containing various hash values of the file.
    """
    try:
        with open(file_path, "rb") as file:
            sha1_hash = hashlib.sha1()
            sha256_hash = hashlib.sha256()
            md5_hash = hashlib.md5()
            blake2b_hash = hashlib.blake2b(digest_size=32)
            while True:
                data = file.read(65536)  # Read file in chunks of 64KB
                if not data:
                    break
                sha1_hash.update(data)
                sha256_hash.update(data)
                md5_hash.update(data)
                blake2b_hash.update(data)
            all_hashes = Munch(
                sha1=sha1_hash.hexdigest(),
                sha256=sha256_hash.hexdigest(),
                md5=md5_hash.hexdigest(),
                blake2b_256=blake2b_hash.hexdigest()
            )
        return all_hashes
    
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: File '{file_path}' not found.")

# Example usage:
file_path = r"C:\Users\Fazle Yazdan\Desktop\My_projects\generate_hash\test_data\Django-1.10.8-py2.py3-none-any.whl"
hash_value = hash_file(file_path)
if hash_value:
    print(f"\nSHA-1 hash of the file: {hash_value.sha1}")
    print(f"\nSHA-256 hash of the file: {hash_value.sha256}")
    print(f"\nMD5 hash of the file: {hash_value.md5}")
    print(f"\nBlake2b-256 hash of the file: {hash_value.blake2b_256}")
    print(hash_value)