on_the_menu = {'1': {'name': 'IQ', 'price': 100},
               '2': {'name': 'confidence', 'price': 0},
               '3': {'name': 'sense of humor','price': 200 },
               '4': {'name': 'athletic ability', 'price': 150},
               '5': {'name': 'group of friends','price': 1000}
    
}

final_form = {}

def build_an_identity():
    current_identity = {}
    total = 0.00
    
    
    answer = input("hello!! welcome to the build an identity store. Would you like to build, return, exaimine, or leave?")


    while answer != 'leave':
            assembling = input("which numbered quality can I get you to assemble your identity?")
            while True:
                if assembling.isdigit():
                    if int(assembling) > 5:
                        print("please enter a valid number 1-5")
                else:
                    assembling = input("please enter a valid number 1-5")
                if int(assembling) <= 5: 
                    assembled = on_the_menu[assembling]['name']
         
            
                    multiplier = input("How many of said attribute?")
                    multiplied = (on_the_menu[assembling]['price']*int(multiplier))
       
         
                    final_form[assembled] = multiplied
           
                    ask_again = input("would you like to do something else? yes/no")
                    if ask_again == 'no':
                        break
            
                    if ask_again == 'yes':
                        next_ans = input("would you like to return, exaimine, or leave?")
                        if next_ans == 'return':
                            ret_id = input("which quality would you want to return?")
                            final_form.pop(ret_id)
                            break
                        if next_ans == "exaimine":
                            print("this is what is in your cart")
                            print(final_form)
                            break
                        elif next_ans == 'leave':
                            answer = input("To confirm you're leaving, please type leave")
                            print("Okay, thank you for visiting!")
                            
                            for quality, price in dict.items(final_form):
                                print(f'I bought {quality} for {price}')
                            break
                            
                            
build_an_identity()