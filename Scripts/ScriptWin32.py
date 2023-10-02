import win32net
import win32netcon
import sys

def create_user(username, password):
    user_info = {
        'name': username,
        'password': password,
        'priv': win32netcon.USER_PRIV_USER,
        'home_dir': None,
        'comment': None,
        'flags': win32netcon.UF_SCRIPT,
        'script_path': None
    }
    win32net.NetUserAdd(None, 1, user_info)

def delete_user(username):
    win32net.NetUserDel(None, username)

def create_group(groupname):
    group_info = {
        'name': groupname,
        'comment': None
    }
    win32net.NetLocalGroupAdd(None, 1, group_info)

def delete_group(groupname):
    win32net.NetLocalGroupDel(None, groupname)

def join_group(username, groupname):
    member_info = {
        'domainandname': username
    }
    win32net.NetLocalGroupAddMembers(None, groupname, 3, [member_info])

def main():
    while True:
        print("\nSelect an option:")
        print("1. Create a user")
        print("2. Delete a user")
        print("3. Create a group")
        print("4. Delete a group")
        print("5. Join a group")
        print("6. Exit")

        choice = int(input("Enter the number of your choice: "))

        if choice == 1:
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            create_user(username, password)
            print("User created successfully.")
        elif choice == 2:
            username = input("Enter the username: ")
            delete_user(username)
            print("User deleted successfully.")
        elif choice == 3:
            groupname = input("Enter the group name: ")
            create_group(groupname)
            print("Group created successfully.")
        elif choice == 4:
            groupname = input("Enter the group name: ")
            delete_group(groupname)
            print("Group deleted successfully.")
        elif choice == 5:
            username = input("Enter the username: ")
            groupname = input("Enter the group name: ")
            join_group(username, groupname)
            print("User joined the group successfully.")
        elif choice == 6:
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
