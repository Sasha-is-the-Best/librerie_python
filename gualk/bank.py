import configparser
import os

class Bank:
    def __init__(self, file_name="bank_config.ini"):
        self.file_name = file_name
        self.config = configparser.ConfigParser()
        if not os.path.exists(file_name):  # Controlla se il file .ini esiste
            with open(file_name, 'w') as f:  # Crea il file se non esiste
                f.write("")
        self.config.read(file_name)
        if 'Accounts' not in self.config:
            self.config['Accounts'] = {}
            self.save()

    def create_account(self, account_name, initial_balance=0):
        if account_name in self.config['Accounts']:
            print("L'account esiste già!")
        else:
            self.config['Accounts'][account_name] = str(initial_balance)
            self.save()
            print(f"Account '{account_name}' creato con successo!")

    def get_balance(self, account_name):
        if account_name in self.config['Accounts']:
            return float(self.config['Accounts'][account_name])
        else:
            print("Account non trovato!")
            return None

    def deposit(self, account_name, amount):
        if account_name in self.config['Accounts']:
            balance = float(self.config['Accounts'][account_name])
            balance += amount
            self.config['Accounts'][account_name] = str(balance)
            self.save()
            print(f"Deposito di {amount} completato! Saldo attuale: {balance}")
        else:
            print("Account non trovato!")

    def withdraw(self, account_name, amount):
        if account_name in self.config['Accounts']:
            balance = float(self.config['Accounts'][account_name])
            if amount <= balance:
                balance -= amount
                self.config['Accounts'][account_name] = str(balance)
                self.save()
                print(f"Prelievo di {amount} completato! Saldo attuale: {balance}")
            else:
                print("Saldo insufficiente!")
        else:
            print("Account non trovato!")

    def save(self):
        with open(self.file_name, 'w') as configfile:
            self.config.write(configfile)

def main_menu():
    bank = Bank()
    while True:
        print("\n--- Menu ---")
        print("1. Crea un nuovo account")
        print("2. Deposita denaro")
        print("3. Preleva denaro")
        print("4. Controlla saldo")
        print("5. Esci\n")
        scelta = input("Scegli un'opzione: ")
        
        if scelta == "1":
            account_name = input("\nInserisci il nome dell'account: ")
            bank.create_account(account_name, 0)
        elif scelta == "2":
            account_name = input("\nInserisci il nome dell'account: ")
            amount = float(input("Inserisci l'importo da depositare: "))
            bank.deposit(account_name, amount)
        elif scelta == "3":
            account_name = input("\nInserisci il nome dell'account: ")
            amount = float(input("Inserisci l'importo da prelevare: "))
            bank.withdraw(account_name, amount)
        elif scelta == "4":
            account_name = input("\nInserisci il nome dell'account: ")
            balance = bank.get_balance(account_name)
            if balance is not None:
                print(f"Saldo attuale: {balance}")
        elif scelta == "5":
            print("\nGrazie per aver utilizzato la banca!")
            input()
            break
        else:
            print("\nOpzione non valida, riprova!")