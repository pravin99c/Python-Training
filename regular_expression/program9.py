# Filter all elements that contain a sequence of lowercase alphabets followed 
# by - followed by digits. They can be optionally surrounded by {{ and }}. 
# Any partial match shouldn't be part of the output.
# ample input: ['{{apple-150}}', '{{mango2-100}} ', '{{cherry-200', 'grape-87']
# Sample output: ['{{apple-150}}', 'grape-87']

import re
list_and=['{{apple-150}}','{{mango2-100}}','{{charry-200','grape-87']


reg=r'^{{+[a-z]+[-]+[0-9]+}}|^[a-z]+[-]+[0-9]'

for i in list_and:
    if re.findall(reg,i):
        print(i)