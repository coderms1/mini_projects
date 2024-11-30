from bankaccount import BankAccount

def main():

  myAccount = BankAccount(1000) 

  print(myAccount)

  myAccount.deposit(500)  

  print(myAccount)  

  myAccount.withdraw(200) 

  print( myAccount.get_balance() )  

main()