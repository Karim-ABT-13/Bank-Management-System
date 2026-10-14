from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt, IntPrompt, Confirm
from rich.progress import Progress
import time

console = Console()

def creat_account():
    console.print(
        Panel("                                                     CREAT ACCOUNT")
    )

    print()

    with open("creat_account.txt", "w") as file:
        print()

        try:
	        name = input("-Enter your Name: ")
	        password = input("-Creat a Password: ")

        except TypeError:
            print("Enter input correctly!")
            exit()


# I will just make here a progresse bar, its not a logical thing, its just for pristige;;

        with Progress() as progress:
            task = progress.add_task("Loading...", total=100)

            while not progress.finished:
                progress.update(task, advance=1)
                time.sleep(0.03)

## I just finished making the progress bar, don't worry if you can't do like this, just ask chat gpt for that because-
#its not a logic thing or somthing important, its just for make it look beatifule;;

                id = 1001
                balance = 0

                file.write(f"{name} | {id} | {balance} | {password}\n")


    print()
    table = Table(title="USER INFORMATIONS")

    table.add_column("                    ACCOUNT ID            ")
    table.add_column("                    NAME               ")
    table.add_column("                    BALANCE            ")

    table.add_row( str(id), name, str(balance) + "$" )
    console.print(table)

    print()
    print("Account Created Successfuly!")
    print()
 
creat_account()   


def LogIn():
	console.print(
		Panel("                                                           LOGIN")
		)

	# I will open the file because of the name and password:;

	with open("creat_account.txt", "r") as file:
		for line in file:
			data = line.strip().split(" | ") 

			name = data[0]
			password = data[3]

		file.readlines()


	try:
		Enter_username = input("Enter the account username: ")
		Enter_password = input("Enter password: ")

	except TypeError:
		print("Somthing went wrong!")


	if Enter_password == password and Enter_username == name:
		print()
		print(f"Log-In to your account successfuly!\nWelcome, {name}.")

	elif password != Enter_password or name != Enter_username :
		print("Incorrect Password or username!")
		exit()

LogIn()

def main_menu_options():
	print()
	print("=" * 49)
	print("                Main Menu Choices\n")

	choices = ["1. Show Balance", "2. Deposit", "3. Withdraw", "4. Transfer Money", "5. Transaction History", "6. Account Information", "7. Logout"]
	for i in choices:
		print(i)

main_menu_options()

choose_an_option = int(input("Choose: "))

class Account:
	def __init__(self, balance, amount, amount_transfered, amount_withdraw):
		self.balance = balance
		self.amount = amount
		self.amount_transfered = amount_transfered
		self.amount_withdraw = amount_withdraw

account1 = Account(0, 0, 0, 0)
amount = Account(0, 0, 0, 0)
amount_transfered = Account(0, 0, 0, 0)
amount_withdraw = Account(0, 0, 0, 0)


if choose_an_option == 1:


	class ShowBalance:
		def __init__(self, account):
			self.account = account

		def Balance(self):
			print("=" * 20 + " BALANCE " + "=" * 20)
			print()

			print(f"Current Balance: {self.account.balance}$ ")
			print("=" * 49) 

	user_balance = ShowBalance(account1)
	user_balance.Balance()

	choose_an_option = int(input("Choose: "))


if choose_an_option == 2:


	class DepositMoney:
		def __init__(self, amount):
			self.amount = amount

		def Deposit(self):
			print()
			print("=" * 20 + " DEPOSIT " + "=" * 20)
			print()

			try:
				self.enter_amount = int(input("Enter Amount: "))
				print()

			except ValueError:
				print("Enter Numbers Only!!")

			self.amount.balance += self.enter_amount

			print(f"New Balance: {self.amount.balance}$")
			print("=" * 49)

	user3 = DepositMoney(account1)
	user3.Deposit()

	choose_an_option = int(input("Choose: "))


if choose_an_option == 3:

	class WithdrawMoney:
		def __init__(self, amount_withdraw):
			self.amount_withdraw = amount_withdraw

		def Withdraw(self):
			print("=" * 20 + " WITHDRAW " + "=" * 19)
			print()

			try:
				self.enter_amount_withdraw = int(input("Enter Amount: "))

			except ValueError:
				print("Enter Numbers Only!!")

			if self.enter_amount_withdraw > self.amount_withdraw.balance :
				print("Insufficient Balance!")
				exit()

			elif self.enter_amount_withdraw <= self.amount_withdraw.balance:

				self.amount_withdraw.balance -= self.enter_amount_withdraw
				print()

				print(f"New Balance: {self.amount_withdraw.balance}$")
				print("=" * 49) 


	user2 = WithdrawMoney(account1)
	user2.Withdraw()

	choose_an_option = int(input("Choose: "))

if choose_an_option == 4:
	class TransferMoney:
		def __init__(self, amount_transfered):
			self.amount_transfered = amount_transfered

		def Transfer(self):
			print("=" * 17 + " TRANSFER MONEY " + "=" * 17)
			print()

			try:
				self.transfer_amount = int(input("Enter The Amount: "))
				self.account_number = int(input("Enter the account Number you want tranfer money to: "))

			except ValueError:
				print("Enter Numbers Only!!")

			if self.transfer_amount > self.amount_transfered.balance:
				print("Insufficient Balance!")
				exit()

			elif self.transfer_amount <= self.amount_transfered.balance:
				self.amount_transfered.balance -= self.transfer_amount
				self.account_number += self.transfer_amount

			print(f"New Balance: {self.amount_transfered.balance}$")
			print(f"Account Number-Amount transfered: {self.account_number}")

			print("=" * 49)

	user1 = TransferMoney(account1)
	user1.Transfer()

	choose_an_option = int(input("Choose: "))

if choose_an_option == 5:
	class AccountTransactionHistory:
		def __init__(self, transaction_history, amount_transfered, amount_withdraw, amount):
			self.transaction_history = transaction_history
			self.amount_transfered = amount_transfered
			self.amount_withdraw = amount_withdraw
			self.amount =  amount

		def Transaction(self):
			print("=" * 14 + " TRANSACTION HISTORY " + "=" * 14)
			print()

			print(f"Deposit : {self.amount.enter_amount}$\nWithdraw : {self.amount_withdraw.enter_amount_withdraw}$\nTransfered-Money : {self.amount_transfered.transfer_amount}$")

			print("=" * 49)

	user = AccountTransactionHistory(account1, user1, user2, user3)
	user.Transaction()


choose_an_option = int(input("Choose: "))

if choose_an_option == 6:


	class AccountInformation:
		def __init__(self, account_informations):
			self.account_informations = account_informations

		def Informations(self):

			with open("creat_account.txt", "r") as file:
				for line in file:
					data = line.strip().split(" | ")

					name = data[0]
					id = data[1]
					balance = data[2]

				file.readlines()


			print("=" * 15 + " ACCOUNT INFORMATIONS " + "=" * 15)
			print()

			table = Table(title="USER INFORMATIONS")

			table.add_column("                    ACCOUNT ID            ")
			table.add_column("                    NAME               ")

			table.add_row( id, name)
			console.print(table)

	user = AccountInformation(account1)
	user.Informations()
