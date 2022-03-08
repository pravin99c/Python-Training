# Split the given input string on one or more repeated sequences of cat using regex
# Sample input: firecatlioncatcatcatbearcatcatparrot
# Sample output: ['fire', 'lion', 'bear', 'parrot']

import re

str= "firecatlioncatcatcatbearcatcatparrot"
word_list =re.split(r"(?:cat)+", str)
print(word_list)