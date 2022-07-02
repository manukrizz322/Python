"""
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists



"""

try:
    # f=open("write.txt",'w')
    # f=open("24_Set.py",'a')
    f = open("24_Set.py",'r')
    """
    for line in f:
        print(line)
    """
    #print(f.read())
    print(f.readline())

    #f.write("\n\"\"\"***The End****\"\"\"")

except FileNotFoundError:
    print("File Not Found")

else:
    print("Thank You")
    f.close()
