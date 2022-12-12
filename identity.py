final_form = {}

def build_an_identity():
    current_identity = {}
    total = 0.00
    
    
    answer = input("hello!! welcome to the build an identity store. Would you like to build, return, examine, or leave? ")


    while answer != 'leave':
           
            while True:
                assembling = input("which numbered quality can I get you to assemble your identity? ")
                if assembling.isdigit():
                    if int(assembling) > 5:
                        print("please enter a valid number 1-5 ")
                    if int(assembling) <= 5: 
                        assembled = on_the_menu[assembling]['name']
                    else:
                        assembling = input("please enter a valid number 1-5 ")

               
         
            
                    multiplier = input("How many of said attribute? ")
                    multiplied = (on_the_menu[assembling]['price']*int(multiplier))
       
         
                    final_form[assembled] = multiplied
           
                    ask_again = input("would you like to do something else? yes/no ")
                    if ask_again == 'no':
                        break
            
                    if ask_again == 'yes':
                        next_ans = input("would you like to return, examine, or leave? ")
                        if next_ans == 'return':
                            ret_id = input("which quality would you want to return? ")
                            final_form.pop(ret_id)
                            break
                        if next_ans == "examine":
                            print("this is what is in your cart")
                            print(final_form)
                            break
                        elif next_ans == 'leave':
                            answer = input("To confirm you're leaving, please type 'leave' ")
                            print("Okay, thank you for visiting! Here's your receipt ")
                            
                            for stuff, money in final_form.items():
                                print(f'{stuff}, ${money}')
                            
                            
                            list_o_keys = [key for key in final_form]
                            final_key = (', '.join(list_o_keys))
                            vals = [val for val in final_form.values()]
                            sum_of_vals = sum(vals)
                            print(f'You bought {final_key} for ${sum_of_vals}')
                            break
                            
                            
build_an_identity()