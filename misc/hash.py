import hashlib

# Create a SHA-256 hash object
sha256_hash = hashlib.sha256()

# Convert the string to bytes and update the hash object
string_to_hash = "hello world"
sha256_hash.update(string_to_hash.encode('utf-8'))

# Get the hexadecimal representation of the hash
hex_digest = sha256_hash.hexdigest()

# Print the resulting hash
print("SHA-256 hash of '{}': {}".format(string_to_hash, hex_digest))