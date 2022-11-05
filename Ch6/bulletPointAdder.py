import pyperclip

# put the clipboard in to a variable
text = pyperclip.paste()

# split the text variable into lists separated by \n
lines = text.split("\n")

# for every line add an * at the start
for i in range(len(lines)):
    lines[i] = "* " + lines[i]

# combine the files into a string
text = "\n".join(lines)

# copy the text back to the clipboard
pyperclip.copy(text)
