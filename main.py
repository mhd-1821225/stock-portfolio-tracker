import mysql.connector
import database
import stock_api

api_key ="PSWQM05UZEB8XXKK"
tickers = []
ticker_dict = {}
def menu():
    print()
    print("------------------------------------")
    print("press 1 to add new stocks to your portfolio")
    print("press 2 to view your portfolio")
    print("press 3 to edit your portfolio")
    print("press 4 to delete your portfolio")
    print("press 5 to logout")
    print("------------------------------------")








    
def main():
   
    if ch == 1:
        print()
        print("------------------------------------")
        print("To create user fill in the following")
        print()
        database.create_user()
    elif ch == 2:
        print()
        print("------------------------------------")
        start = database.validate_user()
        if start:
            menu()
            
            
            print()
            yea = True
            while yea:
                oove = int(input("Enter your choice: "))
                if oove == 1:
                    # Add new stocks to the portfolio
                    database.add_stock()
                    print("Stocks added successfully!")
                    menu()
                    

                    
                elif oove == 2:
                    # View the portfolio
                    database.view_portfolio()
                    print()
                    menu()
                elif oove== 3:
                    t = int(input("If you want to delete a stock press 1 if you want to edit a stock press 2: "))
                    if t == 1:
                        ticker = input("Enter the ticker you want to delete: ")
                        database.delete_stock(ticker)
                        print("Stock deleted successfully!")
                        menu()
                    elif t == 2:
                        ticker = input("Enter the ticker you want to edit: ")
                        database.edit_stock(ticker)
                        print("Stock edited successfully!")
                        menu()

                    
                elif oove == 4:
                    # Delete the portfolio
                    print("Are you sure you want to delete your portfolio? This action cannot be undone.")
                    confirm = input("Type 'yes' to confirm: ")
                    if confirm.lower() == 'yes':
                        database.delete_portfolio()
                        print("Portfolio deleted successfully!")
                        menu()
                    else:
                        menu()
                elif oove == 5:
                    print("Logging out... refresh the page to login again")
                    yea = False
                else:
                    print("Invalid choice. Please try again.")
                
        else:
            print("Invalid credentials. Please try again.")
    else:
        print("Wrong option try again")
        ch = int(input("Enter your choice: "))
  
        
        

    

    
   

main()