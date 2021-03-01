def IsPal(s):
    return s == s[::-1]

s = ["anna","hannah","ashish"]

for i in s:
    if IsPal(i):
        print("Yes, " + i + " is palindrome.")
    else:
        print("No, " + i + " is not palindrome.")