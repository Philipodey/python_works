def nokia_function():
    print(""""
          ******************
          1. PhoneBook
          2. Messages
          3. Chats
          4. Call register
          5. Tones
          6. Settings
          7. Call divert
          8. Games
          9. Calculator
          10. Reminders
          11. Clock
          12. Profiles
          13. Sim services
          *****************
          
    """)

    nokia = int(input("Select an option: "))
    if nokia == 1:
        print(phone_book())
    elif nokia == 2:
        print(messages())
    elif nokia == 3:
        print(call())
    elif nokia == 4:
        print()


def phone_book():
    print(""""
                      ***************
                      1. Search
                      2. Service Nos
                      3. Add name
                      4. Erase
                      5. Edit
                      6. Assign
                      7. Send b' card
                      8. Options
                      9. speed dials
                      10. Voice tags
                      11. Back to menu
                      ***************
                      """)
    phone_book_input = int(input("Select an option: "))
    if phone_book_input == 1:
        print("search")
    elif phone_book_input == 2:
        print("Service Nos")
    elif phone_book_input == 3:
        print("Erase")
    elif phone_book_input == 4:
        print("Edit")
    elif phone_book_input == 5:
        print("Assign tone")
    elif phone_book_input == 6:
        print("Assign tone")
    elif phone_book_input == 7:
        print("Send b' card ")
    elif phone_book_input == 8:
        print("Options")
        print(""""
                  **********************
                  1. Type of view
                  2. Memory status
                  3. Back to phoneBook
                  4. Back to menu
                  *********************
        """)
        option_input = int(input("Select an option: "))
        if option_input == 1:
            print("Type of view")
        elif option_input == 2:
            print("Memory status")
        elif option_input == 3:
            print(phone_book())
        elif option_input == 4:
            print(nokia_function())
    elif phone_book_input == 9:
        print("Speed dials")
    elif phone_book_input == 10:
        print("Voice tags")
    elif phone_book_input == 11:
        print(nokia_function())


def messages():
    print("Messages")
    print("""
             ****************************
             1. Write messages
             2. Inbox
             3. Outbox
             4. Picture messages
             5. Templates
             6. Smileys
             7. Messages settings
             8. Info service
             9. Voice mailbox number
             10. Service command editor
             11. Back to menu
             ***************************
    """)
    message = int(input("Select an option: "))
    if message == 1:
        print("Write messages")
    elif message == 2:
        print("Inbox")
    elif message == 3:
        print("Picture messages")
    elif message == 4:
        print("Templates")
    elif message == 5:
        print("Smileys")
    elif message == 6:
        print("Message settings")
        print(""""
                  **********************
                  1. Set
                  2. Common
                  3. Back to messages
                  4. Back to main menu
                  *********************
        """)
        message_settings = int(input("Select an option: "))
        if message_settings == 1:
            print("Set")
            print("""
                     *************************
                     1. Message centre number
                     2. Messages sent as
                     3. Message validity
                     4. BacK to Messages
                     5. Back to main menu
                     ************************
            """)
            set = int(input("Select an option: "))
            if set == 1:
                print("Message centre number")
            elif set == 2:
                print("Messages sent as")
            elif set == 3:
                print("Message validity")
            elif set == 4:
                print(messages())
            elif set == 5:
                print(nokia_function())

        elif message_settings == 2:
            print("Common")
            print(""""
                      *************************
                      1. Delivery
                      2. Reply via same centre
                      3. Character support
                      4. Back to messages
                      5. Back to main menu
                      **************************
            """)
            common = int(input("Select an option: "))

        elif message_settings == 3:
            print(messages())
        elif message_settings == 4:
            print(nokia_function())


def calls():
    print("Calls")


print(nokia_function())
