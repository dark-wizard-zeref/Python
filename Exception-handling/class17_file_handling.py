# File path matters!
# Python looks for files relative to where the script is run from.
# Always double-check the path.

f = open(r"Exception-handling\class16_exception_handling.py")
print(f.read())
f.close()   # Always close the file after you're done


# Safer & recommended way (auto-closes the file)
with open(r"Exception-handling\class16_exception_handling.py") as f:
    print(f.read())
# File is automatically closed after this block


"""
File open modes (most commonly used)

'r'  → Read file (file must exist)
'a'  → Append to file (adds data at the end, creates file if not present)
'w'  → Write to file (overwrites file, creates file if not present)
'x'  → Create a new file (error if file already exists)
"""


# Write mode: creates or overwrites the file
f = open(r"Exception-handling\demo.txt", 'w')
f.write("This is a demo file created using write mode.\n")
f.close()


# Append mode: adds content to the end of the file
with open(r"Exception-handling\demo.txt", 'a') as f:
    f.write("This line is added using append mode.\n")