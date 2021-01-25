def vowels(s):
    for c in s:
        if c.lower() in 'aeiouy':
            yield c


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)