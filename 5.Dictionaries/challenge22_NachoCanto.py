print("\n Welcome to the Hasura Database ")

login = {
    "admin00": "admin00",
    "user1": "user1",
    "user2": "user2",
    "user3": "user3",
    "user4": "user4",
    "user5": "user5"
    }

usuario = input("\n\tEnter your user name :\t").lower()

if usuario in login:
    contraseña = input("\n\tEnter your password:\t")
    if contraseña == login[usuario]:
        print(f"\n\tHello {usuario}! You`re now logged In")
        if usuario == "admin00":
            print(f"\n\tHere is the current user database:\t")
            for key, value in login.items():
                print(f"\t{key} - {value}")
        else:
            opc = input("\n\tWould you like to change your password? (y/n):\t").lower()
            if opc == "y":
                nueva_contraseña = input("\n\tWhat would you like your new password to be (8 characters long):\t")
                if len(nueva_contraseña) >= 8:
                    login[usuario] = nueva_contraseña
                    print(f"\n\t{usuario} your password is {nueva_contraseña}.")
                else:
                    print(f"\n\t{nueva_contraseña} not the minimun eight characters")
            else:
                print("\n\tOk! GoodBye. You`re logged out!")
    else:
        print(f"\tpassword incorrect!")
else:
    print("\n\tusuario not in database, goodbye")