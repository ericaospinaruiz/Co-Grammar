# This program will create an email inbox and allows the user to view 
# lists of emails, read selected emails and quit the program.

# Creating inbox list to store email objects later in the program.
inbox = []

class Email:
    """ Creating Email class within which I will be able to create methods to allow the program to function as needed."""

    # Initialising the has_been_read variable to false
    has_been_read = False

    def __init__(self, email_address, subject_line, email_content):
        """ Initialising a constructor, taking in arguments for email address, subjec line and email content."""
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        pass
    
    def mark_as_read(self):
        """ Creating new method to change has_been_read to true. This is a method as it is a function within a class."""
        self.has_been_read = True

def populate_inbox(inbox, email):
    """ Creating a function outside of the class which adds email objects to the list 'inbox'."""
    inbox.append(email)

def list_emails(inbox):
    """ Creating a funciton outside the class to list the inbox list with the object and its index."""
    for index, ele in enumerate(inbox):
        print(index, ele.subject_line)

def read_email():
    """Creates a function which allows the user to select an email using the index 
    values provided through the list_emails function.""" 
    user_email = int(input("Select an email."))
    user_choice = inbox[user_email]
    print(user_choice.email_address)
    print(user_choice.subject_line)
    print(user_choice.email_content)
    user_choice.mark_as_read()

# Creating email objects and using populate_inbox funcion to add to my inbox list.
easy_jet = Email("easyjet@easyjet.com", "Easter Sale Now On!", "Hi Erica, With up to £200 off...")
populate_inbox(inbox, easy_jet)

hyperion_dev = Email('hyperiondev@hyperiondev.com', 'Your deadline is approaching.', 'Hi Erica, We have noticed...')
populate_inbox(inbox, hyperion_dev)

asos = Email('asos@asos.com', 'New Season In!', 'We have lots of new...')
populate_inbox(inbox, asos)

# Assigning value of 0 to user_selection which is used later within while loop.
user_selection = 0

# If user selects option 1 or 2, the loop continues. If the user selects 3, the loop ends as they have chosen to quit the application.
while user_selection != 3:
    print("""
        1. Read an email
        2. View unread emails
        3. Quit application
        """)

    # Prompting the user to select an option from the menu using the index - input set to 'int' value.
    user_selection = int(input("Select an option."))

    # Creating conditional statements to allow the user to interact with the user 
    # depending on the menu option they have selected.
    # If the user selects option 1, list_emails function is called, followed by read_email 
    # to allow the user to select which email they wish to read.
    if user_selection == 1:
        list_emails(inbox)
        read_email()
    # If user selects menu option 2, any emails within inbox list which have not had the 
    # function mark_as_read passed will be printed along with their index.
    elif user_selection == 2:
        for index, ele in enumerate(inbox):
            if ele.has_been_read == False:
                print(index, ele.subject_line)
    # If user selects option 3 (only other option), they are alerted that they have quit the 
    # application and the while loop ends as the condition is now true.
    else:
        print("You have now quit the application.")
