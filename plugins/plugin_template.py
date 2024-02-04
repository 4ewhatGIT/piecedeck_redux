import libraryidk


def other_func():
    print("You can use other functions from the same file too!")


def script():
    """
    Main function of any plugin for PieceDeck for both custom and stock plugins.
    Main functionality (anything you want to do when plugin is selected on the program selection screen)
    goes here, it can use anything you want (as long as it is in the same folder/file)
    """
    print("Your functionality goes here!")
    other_func()
    libraryidk.sex()
