numbers = input()
Wordings = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four"
}
output = ""
for i in numbers:
    output += Wordings.get(i, "!") + " "
print(output)