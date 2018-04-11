# use of function "regex". Below function replacing capital letters from A-Z with blank spaces

import re
string = "'I am not YELLING',she said"
show = re.sub('[.,\' A-Z+" "]','',string)

print(show)

# To concatenate string with the Regular expression
string = string + "6 234 - 98"
print(string)

# To print Only Numbers from the strings
new = re.sub('[^0-9]','' , string)
print(new)

