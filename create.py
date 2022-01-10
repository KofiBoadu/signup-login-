#CREATING AN ACCOUNT AND LOGGING INTO YOUR ACCOUNT.




print("PLEASE CREATE YOUR BANK ACCOUNT BELOW")


#COLLECTING PERSONAL INFORMATION FROM USER


name= input("ENTER FULL NAME : ")

age= input("HOW OLD ARE YOU: ")

phone=input("PHONE NUMBER: ")



state,city,zip_code= input("STATE: "),input("CITY"),input("ZIPCODE: ")

store_username= [ ]

store_username.append(   input("CREATE A USERNAME: ")   )


#ASKED THE USER TO CREATE THEIR USERNAME AND STORED IT INTO AN EMPTY LIST

store_password= [  ]

store_password.append(  input("CREATE A PASSWORD: ")  )


#ASKED THE USER TO CREATE THEIR PASSOWRD AND STORED IT INTO AN EMPTY LIST 


    
    


while True:
    
    print(f"WELCOME TO LAMBDA BANK !{name}")
    
    
    
#USING THE WHILE LOOP TO VALIDATE LOGIN

    
    
    
    print("PLEASE LOGIN INTO YOUR ACCOUNT BELOW")
    
    
    
    
    
    print("ENTER YOUR USERNAME: ")
    
    username=input()
    
#ASKED THE USER TO NOW LOGIN IN WITH THE USERNAME THEY CREATED ABOVE 
    
    print("ENTER YOUR PASSWORD:  ")
    
    password= input()
    
#ASKED USER TO ENTER THE PASSWORD THEY CREATED ABOVE 
    
    if username==store_username[0] and password==store_password[0]:
        

#USING THE IF CONDITION TO CHECK IF THE LOGIN DETAILS ARE CORRECT OR NOT 
        
        
        break 

        
print("YOU HAVE SUCCESSFULLY CREATED YOUR LAMBDA SAVINGS  BANK  ACCOUNT!")
        
      
            
        
        

