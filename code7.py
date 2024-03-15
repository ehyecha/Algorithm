str = input()
str = [s for s in str]
conv_str = [ s.lower() if s.isupper() else s.upper() for s in str]
print(''.join(conv_str))