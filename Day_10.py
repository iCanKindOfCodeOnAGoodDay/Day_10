"""

    Scott Quashen
    London App Brewery
    100 Days of Python Code: Day 10
    May 02 2024

    ------
    Description:    Console Calculator - 100 Lines of code
    ------
    
    ------
    Inputs:         Console input (math commands, numbers) Note ** Does not handle errors, only accepts the 4 most basic math commands
    ------
    
    ------
    Outputs:        Console output (winner)
    ------
    
    ------
    Dependencies:   None.
    ------

    ------
    Assumptions:    Developed and tested using Spyder 5.15.7, Python version 3.11.5 on macOS 14.4.1
    ------
    
"""

# Constant declared as global variable instead of cluttering main
global_art = """
    
 ____              ___                    ___             __                         __             
/\  _`\           /\_ \                  /\_ \           /\ \__  __                 /\ \            
\ \ \/\_\     __  \//\ \     ___   __  __\//\ \      __  \ \ ,_\/\_\    ___     ___ \ \/    ____    
 \ \ \/_/_  /'__`\  \ \ \   /'___\/\ \/\ \ \ \ \   /'__`\ \ \ \/\/\ \  / __`\ /' _ `\\/    /\_ ,`\  
  \ \ \L\ \/\ \L\.\_ \_\ \_/\ \__/\ \ \_\ \ \_\ \_/\ \L\.\_\ \ \_\ \ \/\ \L\ \/\ \/\ \     \/_/  /_ 
   \ \____/\ \__/.\_\/\____\ \____\\ \____/ /\____\ \__/.\_\\ \__\\ \_\ \____/\ \_\ \_\      /\____\
    \/___/  \/__/\/_/\/____/\/____/ \/___/  \/____/\/__/\/_/ \/__/ \/_/\/___/  \/_/\/_/      \/____/
                                                                                                    
                                                                                                    
 ____                            ___           __                                                   
/\  _`\   __                    /\_ \         /\ \__                                                
\ \,\L\_\/\_\    ___ ___   _____\//\ \      __\ \ ,_\   ___     ___                                 
 \/_\__ \\/\ \ /' __` __`\/\ '__`\\ \ \   /'__`\ \ \/  / __`\ /' _ `\                               
   /\ \L\ \ \ \/\ \/\ \/\ \ \ \L\ \\_\ \_/\  __/\ \ \_/\ \L\ \/\ \/\ \                              
   \ `\____\ \_\ \_\ \_\ \_\ \ ,__//\____\ \____\\ \__\ \____/\ \_\ \_\                             
    \/_____/\/_/\/_/\/_/\/_/\ \ \/ \/____/\/____/ \/__/\/___/  \/_/\/_/                             
                             \ \_\                                                                  
                              \/_/                                                                  
    """

def main():
    """
    
    Description -   Runs a very simple console calculator
    ----------
    Input -         Console **Does not handle errors
    ----------
    Output -        Console
    -------

    """ 
        
    starting_num = 0   
    user_num = 0
    
    command = '+'
    
    while True:
        
        print(global_art)
        
        user_num = float(input('type a number'))      
        
        r = perform_math( starting_num, command, user_num )
        
        print(r)

        command = input('type a command \n+\n-\n/\nx ')       
            
        starting_num = r
        user_num = 0
        

def perform_math( left_num, command, right_num  ):
    """
    
    Description -   Handles math for the calculator
    ----------
    Input -         Console **Does not handle errors
    ----------
    Output -        Console
    -------

    """ 
    
    if command == '+':
        return left_num + right_num
    elif command == '-':
        return left_num - right_num
    elif command == 'x':
        return left_num * right_num
    elif command == '/':
        return left_num / right_num
        
# run code 
if __name__ == '__main__':
    main()