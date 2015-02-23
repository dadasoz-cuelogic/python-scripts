import re
url = "aabbbccchhh"
p = re.compile('^(([^:/?#]+):)?(//([^/?#]*))?([^?#]*)(\?([^#]*))?(#(.*))?')
m = p.match(url)
print m