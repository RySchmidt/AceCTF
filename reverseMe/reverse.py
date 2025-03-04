# Open the file in binary mode, read all its content, reverse the bytes, and save it back
with open('Reverseme.png', 'rb') as file:
    content = file.read()

# Reverse the binary content
reversed_content = content[::-1]

# Write the reversed content to a new file
with open('reversed.png', 'wb') as file:
    file.write(reversed_content)
