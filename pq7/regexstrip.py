import re
a = input("Enter your string:")
strip = input("char you want to strip")
if strip == '':
    def reStrip(sampleText, char = ' '):
        stripRegex = re.compile(r'^\s+|/s+$|(^\s+&/s+$)')
        mo = re.sub(stripRegex,"",sampleText)
        print(mo)
else:
    def reStrip(sampleText, strip):
        strip2 = re.compile(rf'^{strip}+|{strip}+$|(^{strip}+&{strip}+$)')
        print(strip2)
        s = re.sub(strip2,"",sampleText)
        print(s)
reStrip(a, strip)