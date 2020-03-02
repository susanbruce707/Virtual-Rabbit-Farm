# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 08:31:51 2020
Virtual rabbit farm module, rabbit_menu_select.
displays program menu.
recieves input from user (program selection)
message Rabbit class with choice from user input and return to main().
@author: susan
"""
from rabbit_class import Rabbit
def main():
    """
    __main__
    print program menu
    get input from user selection
    message Rabbit class with selection.
    """
    choice = None
    select = ('0', '1', '2', '3', '4', '5')
    while choice not in select:
        print(
"""
0 Exit program
1 Load rabbits
2 Create rabbit
3 List rabbits
4 Display rabbit
5 Save rabbits
"""
        )
        choice = input('Select option >')
        print('--')
        if choice not in select:
            print('    unvalid selection made')
            choice = None
    if choice == '0':
        print('*___Program exited by user___*')
        pass
    elif choice == '5':
        print('Save rabbits')
        Rabbit.save_rabbits()
        print('*--------------^^^--------------*')
        main()
    elif choice == '4':
        print('Display rabbit')
        num = int(input('Enter number of rabbit >'))
        print(Rabbit.obj_dic[num].display_rabbit())
        print('*--------------^^^--------------*')
        main()
    elif choice == '3':
        print('List rabbits')
        Rabbit.list_rabbits()
        print('-----------------^------^^^^^')
        main()
    elif choice == '2':
        print('Create rabbit')
        Rabbit.create_rabbit()
        print('*--------------^^^--------------*')
        main()
    elif choice == '1':
        print('Load rabbits')
        Rabbit.load_rabbits()
        print('*--------------^^^--------------*')
        main()
if __name__ == '__main__':
    main()
    ans = input('Do you want to save rabbits? ')
    if ans in ('y', 'Y', 'yes', 'YES', 'Yes'):
        Rabbit.save_rabbits()
    print('\n*-------Program ended--------*')    
