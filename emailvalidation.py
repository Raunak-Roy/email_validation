import webbrowser

email = input("Enter your email: ")

k, j, d = 0, 0, 0

if len(email) >= 6:
    if email[0].isalpha():
        if "@" in email and email.count("@") == 1:
            if (email[-4] == "." or email[-3] == "."):
                for i in email:g:
                    if i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i.isupper():
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i in ["_", ".", "@"]:
                        continue
                    else:
                        d = 1

                if k == 1 or j == 1 or d == 1:
                    print("Wrong email format")
                else:
                    # Open the email address in a new tab
                    webbrowser.open_new_tab("mailto:" + email)
            else:
                print("Wrong email format")
        else:
            print("Wrong email format")
    else:
        print("Wrong email format")
else:
    print("Wrong email format")
