import re
from urllib.parse import urlparse

def extract_url_features(url):
    parsed = urlparse(url)

    url_length = len(url)
    dot_count = url.count('.')
    special_char_count = len(re.findall(r'[@\-?=]', url))
    has_ip = 1 if re.search(r'\d+\.\d+\.\d+\.\d+', url) else 0
    https_present = 1 if parsed.scheme == "https" else 0
    subdomain_count = parsed.netloc.count('.') - 1
    digit_count = sum(char.isdigit() for char in url)

    return [
        url_length,
        dot_count,
        special_char_count,
        has_ip,
        https_present,
        subdomain_count,
        digit_count
    ]
