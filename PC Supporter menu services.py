# PC Support, Fixer, and Builder

REGULAR_CHECKUP = 15.00
ANTI_MALWARE_PRICE = 50.00        # Constant Prices
NORM_PC_BUILD = 1050.00
CUSTOM_PC_BUILD = 2755.00

stotal = 0.0
bought_norm_pc = False
bought_custom_pc = False

while True:
    print("\t\t|--- PC Support ", " Fixer " , " Builder ---|", sep = "|")
    print("\n1.) Regular Checkup")
    print("2.) Malware Service")                                               # Menu Layout
    print("3.) PC Build -NORM- ")
    print("4.) Custom PC Build")
    print("5.) Checkout")
    print("6.) Exit (Without Checkout)")
    
    choice = input("\nEnter The Service Wanted(1-6):").strip()              # User inputs service un-regarding whitespace
    
    if choice == "1":
        stotal += REGULAR_CHECKUP                                  # shortcut actually means stotal = stotal + REGULAR_CHECKUP
        print("Finished: Regular Checkup")
        print(f"Total Current = £{round(stotal, 2)}")          # Prints the current total to inform customers and rounds it to two places to stop over-expressive integers
                                                               # does this with every service used
    elif choice == "2":
        stotal += ANTI_MALWARE_PRICE
        print("Finished: Malware Service")
        print(f"Total Current = £{round(stotal, 2)}")
        
    elif choice == "3":
        stotal += NORM_PC_BUILD
        bought_norm_pc = True                                       # if user buys norm_pc it changes from False to True as the condition has changed from not wanting to wanting
        print("Finished: PC Build -NORM-")
        print(f"Total Current = £{round(stotal, 2)}")
        
    elif choice == "4":
        stotal += CUSTOM_PC_BUILD
        bought_custom_pc = True                                     # if user buys custom_pc it changes from False to True as the condition has changed from not wanting to wanting
        print("Finished: Custom PC Build")
        print(f"Total Current = £{round(stotal, 2)}")
    
    elif choice =="5":
        if stotal == 0:
            print("No Service Selected, Please Pick One")           # if user doesn't buy or choose any service this stops them from not or forgetting to, retelling thme to choose a service
            continue
        
        print("|---Checkout---|")
        print(f"Total = £{round(stotal, 2)}")                       # shows the checkout total pre discs
        
        auto_disc_rate = 0.0
        if stotal >= 350: 
            auto_disc_rate = 0.18                                   # introduces discounts for percent off; use of relational operators to set the discounts based on money spent
        elif stotal >= 175: 
            auto_disc_rate = 0.10

        auto_disc_amount = round(stotal * auto_disc_rate, 2)
        aft_auto = round(stotal - auto_disc_amount, 2)              # the mathematical operation to take the percentage of the total 

        if auto_disc_rate > 0:
            print(f"Automatic discount ({int(auto_disc_rate*100)}%): -£{auto_disc_amount}")
        else:
            print("Automatic discount: £0.00")                      # this is if there is no discount for how much money the user/customer spent meaning they didn't spend enough
        
        cus_disc = 0.0                                              # custom discount for buying both the norm_pc and custom one
        if bought_norm_pc and bought_custom_pc:                     # if both are True(meanning if the customer chose and bought both) give them £5.00 off and round it
            cus_disc = 5.00
            aft_auto = round(aft_auto - cus_disc, 2)
            print(f"Custom Discount (PC Build -NORM- + Custom PC Build): -£{round(cus_disc,2)}")
        else:
            print("Custom Discount: £0.00")                         # this is if the customer didn't buy both the custom discount is then £0.00
            
        promo = input("Enter Promo code (or press ENTER to skip):").strip() .upper()   # disregards whitespace and uppercase in case the customer uses lowercase letters
        p_discount = 0.0
        if promo == "PCBUILDER1000":
            p_discount = round(aft_auto * 0.15, 2)                  # adds a promo discount on top of 15% 
            aft_auto = round(aft_auto - p_discount, 2)
            print(f"Promotional discount (PCBUILDER1000 – 15%): -£{p_discount}")
        else:
            print("Promotional discount: £0.00")                    # this is for no promo code 
            
        f_total = aft_auto                                                 # this is now the full total after all the discounts and promos have either been added or not
        print(f"\nFinal total to pay: £{round(f_total, 2)}")
        print("Thank You, for using our servives. We'll see you soon!")
        break                                                              # stops program
    
    elif choice == "6":
        print("Exit without checkout. Goodbye!")
        break                                                              # stops program

    else:
        print("Invalid choice. Please enter a number from (1-6) Thank You.")         # This is if the customer didn't choose a service inbetween the numbers 1-6


    
            
            
            
            
            
            
        
            
            
            
            
        
        
        
        
        
        
    
            
        
        
        
    
        
        
        
        
    