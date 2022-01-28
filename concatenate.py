import glob

menu = """
========================
File Concatenate Program
========================

1: Concatenate Files
2: Exit
"""
done = False

while not done:

    print(menu)
    selection = input("Select what you would like to do: ")
    print()

    
    if selection == '1':
        files = []
        files = glob.glob('app.*.log')

        o = open('output.txt', 'w')
    
        for filename in files:
            with open(filename) as f:
                o.write(f.read())

    elif selection == '2':
        done = True

    else:
        print("{} is not a valid selection.".format(selection))
        print("Please select an avaialable option.")
