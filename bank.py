class Banco:
    
    #creates 2 dictionaries: Client personal Info & Client Bank Balance
    def __init__(self):
        self.clients = {}
        self.clients_balance = {}  #change Dict name to clients_account_data
        
    
    #insert Client in the personal info Dict and return the Client for further usage
    def addClient(self, nome, NIF):
        

        #need to verify the NIF if it already exists..... 
        
        new_client = Cliente(nome, NIF)
        self.clients[new_client.id] = new_client
        return new_client

    
    #remove the Client assingned from personal info and Balance
    def removeClient(self, client):
        #remove Client's account
        if client.id in self.clients_balance:
            client.hasAccount = False
            del self.clients_balance[client.id]
        if client.id in self.clients:
            del self.clients[client.id]
        
            
    
    #insert Client's account in DB and return it
    def createAccount(self, client, saldo=0):
        client_account = Conta(saldo)
        client.hasAccount = True
        if client.id not in self.clients_balance.keys() :
            self.clients_balance[client.id] = [client_account]
        else: 
            self.clients_balance[client.id] += [client_account]
        return client_account
    
    
    #print the Dict Clients Info + Bank Balance: if it exists
    def showClient(self, client):   #posso facilitar e adicionar Account como argumento
        if client.id in self.clients:
            
            account_balance = "".join("conta " + str(n.account_number) + "= " + str(n.saldo) + "€, " for n in self.clients_balance[client.id] if client.hasAccount == True)
            return f"ID: {client.id}, Nome: {client.name}, NIF: {client.nif}, Saldo: {account_balance} "
            
            
    def showClient_nif(self, nif):
        for key_id in self.clients:
            if self.clients[key_id].nif == nif:
                client_object = self.clients.get(key_id)
                return self.showClient(client_object)
            
            
    def showClient_id(self, client_id):
        client_object = self.clients.get(client_id)
        return self.showClient(client_object)
                
            

    #check self.isBlocked before operations
    
        
        
    #transfer positive amount from self to other account
    def transfer(self, client_1, client_2, amount, accountc1=0, accountc2=0):
        amount = abs(amount)
        
        #check if self bank balance
        if amount <= self.clients_balance[client_1.id][accountc1].saldo:
            self.clients_balance[client_1.id][accountc1].saldo -= amount
            self.clients_balance[client_2.id][accountc2].saldo += amount

        else:
            print("Impossivel transferir:",amount,"€"," saldo:",self.clients_balance[client_1.id][accountc1].saldo,"€")
    
   # def showAccount(self, client):  #                                                  --->  move this method to Conta class
     #   print("your account number is:", self.clients_balance[client.id].account_number, "and you balance is", self.clients_balance[client.id].saldo)


    
class Cliente:
    num_clients = 0
    
    
    def __init__(self, nome, nif):
        self.id = Cliente.num_clients 
        self.name = nome
        self.nif = nif
        self.hasAccount = False
        Cliente.num_clients += 1

        
     #create setters e getters
        
    
class Conta:
    id_conta = 0
    
    #adicionar tipo de conta: debit, credit, poupança, ordenado...
    def __init__(self, saldo):
        self.id = Conta.id_conta
        self.saldo = saldo
        self.isBlocked = False
        self.account_number =  (5 - len(str(self.id)))*'0' + str(self.id)
        Conta.id_conta += 1
        
     
    #add a positive amount on Client's account balance                                --->  later to choose account 
    def addMoney(self, amount):
        self.saldo += abs(amount)
        
    def withdraw(self, amount):
        if abs(amount) <= self.saldo:
            self.saldo -= abs(amount) 
        else: 
            print("insuficient funds!")
    #creat withdraw method
    
    #check self.isBlocked before operations
        
    #create card options
    
    #create loan simulator
    

if __name__ == "__main__":

        
    #ideia para gerar N clientes com saldos de conta aleatórios para test
    
    
    WSB = Banco()
    Peter = WSB.addClient("Peter","321839790")
    c1 = WSB.addClient("Parker","123456789")
    
    #Peterson = WSB.addClient("Peterson", "18047411756")
    
    petercontadebito = WSB.createAccount(Peter)
    petercontacredito = WSB.createAccount(Peter)
    c1contadebito = WSB.createAccount(c1)
    print("iddebt",petercontadebito.id)
    print("idcredit",petercontacredito.id)
    print("idc2deb",c1contadebito.id)
    
    c1contadebito.addMoney(-100)
    c1contadebito.withdraw(4.10)
    print(Peter.id, c1.id)
    print(WSB.showClient(Peter))
    print(WSB.showClient(c1))
    
    #print(WSB.clients, WSB.clients_balance)
    WSB.showClient_nif("321839790")
    
    
    
    
    
    WSB.transfer(c1, Peter, 55.90, 0, 1)
    WSB.showClient(Peter)
    
    WSB.showClient(c1)
    #WSB.showAccount(c1)
    print(WSB.showClient(Peter))
    print(WSB.showClient(c1))
    
    c2 = WSB.addClient("Lean","123456000")
    contadebitlean = WSB.createAccount(c2)
    contadebitlean1 = WSB.createAccount(c2)
    contadebitlean2 = WSB.createAccount(c2)
    print(WSB.showClient(c2))
    WSB.removeClient(c1)
    print(WSB.clients)
    #print(WSB.showClient(c2))
    
