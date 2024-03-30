import hashlib

class URLShortener:
    def __init__(self):
        self.url_mapping = {}

    def shorten_url(self, long_url):
        # Generate a hash of the long URL
        hash_object = hashlib.sha1(long_url.encode())
        hash_hex = hash_object.hexdigest()
        
        # Take the first 8 characters of the hash to create the shortened URL
        short_url = hash_hex[:8]
        
        # Store the mapping of short URL to long URL
        self.url_mapping[short_url] = long_url
        
        return short_url

    def expand_url(self, short_url):
        # Retrieve the long URL from the mapping
        long_url = self.url_mapping.get(short_url)
        if long_url:
            return long_url
        else:
            return "Shortened URL not found."

if __name__ == "__main__":
    shortener = URLShortener()
    long_url = input("Enter the long URL: ")
    short_url = shortener.shorten_url(long_url)
    print("Shortened URL:", short_url)
    expanded_url = shortener.expand_url(short_url)
    print("Expanded URL:", expanded_url)
