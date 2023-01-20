import re

def reStrip(sampleText, char=' '):
    stripRegex = re.compile(r'[^'+char+'].*[^'+char+']')
    mo = stripRegex.search(sampleText)
    return mo.group()

sampleText = '    this is    a test      '
text = reStrip(sampleText)
print(text)

sampleText = '             this     is      another       test      '
text = reStrip(sampleText)
print(text)

sampleText = 'iiiiiiiiiiithisiiiiiisiiiiiianotheriiiiiiitestiiiiii'
text = reStrip(sampleText, 'i')
print(text)