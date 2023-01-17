import pathlib
import sys
import os

#Initalize counters and flags
food_lst = []
item_cnt = 0


#Check for previously entered list
def existing_lst():
    import os.path
    file_path = r'C:\Users\Pookie\Downloads\python\grocery_list.txt'
    flag = os.path.isfile(file_path)
    if flag:
        print(f'The file {file_path} exists')

#If file exist, ask user if they wish to continue existing list
        modify = input('Looks like you already have a grocery list started. Would you like to continue this list? Y/N: ')
        if modify == 'Y':
            fp = open (r'C:\Users\Pookie\Downloads\python\grocery_list.txt', 'r')
            for line in fp:
                item = line[:-1]
                food_lst.append(item)
            print('This is your current shopping list: ', food_lst)
            user_lst()


#Promt user to enter new list if 'N' is entered
        elif modify == 'N':
            create = input('Would you like to create a new list? Y/N: ')

# If Y create list
            if create == 'Y':
                user_lst()

# If N print "Have a great day" & end script
            elif create == 'N':
                print('Thanks for stopping by! Have a great day :)')
                sys.exit(0)

#If file does not already exist
    else:
        print(f'The file {file_path} does not exist')

#Promt user to enter new list
        create = input('Would you like to start a new list? Y/N: ')

#If Y create list
        if create == 'Y':
            user_lst()

#If N print "Have a great day" & end script
        elif create == 'N':
            print('Thanks for stopping by! Have a great day :)')
            sys.exit(0)


#Promt user to enter grocery list
def user_lst():
#Set seen_done(list flag) to false. When seen_done is true, input is while loop exited
    seen_done = False
    print("Enter food items on seperate lines. To end input type 'done': ")
#While loop for user list entry
    while (seen_done == False):
        item = input()
        if (item in ['Done', 'done']):
            seen_done = True
        else:
            food_lst.append(item)
    return food_lst

def save_lst():
#If no existing list, then save list
#If existing list, prompt user to save as new list or replace existing list?

#Prompt user to save list
    save = input('Would you like to save this list? Y/N: ')
#If user selects to save new list
    if save == 'Y':
        fp = open(r'C:\Users\Pookie\Downloads\python\grocery_list.txt', 'w')
#Save each item in list on a new line in .txt
        for item in food_lst:
            fp.write("%s\n" % item)
        print(f"List Saved")
#If user selects not to save their list
    elif save == 'N':
        print("List erased")


def item_count():
    item_cnt = len(food_lst)
    return item_cnt


def main():
    existing_lst()
    groceries = food_lst
    item_count()
    print('Your current grocery list contains the following', item_count(),'items: ', groceries)
    save_lst()
    print('Thanks for stopping by! Have a great day :)')

main()
