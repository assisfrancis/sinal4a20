import sys
import func

n1 = 100 
n2 =0
n3=5
n4= 1
n5 = 37
n6=0
n7=1

m1 =100 #int(input("Digite o limite superior:"))
m2 =20
m3=4
m4=4
m5=9


def mostraMenu():
    print("Menu")
    print("1 - Calcular o sinal 4 a 20 mA: ")
    print("2 - Calcular o percentual 4 a 20 mA: ")
    print("3 - Sair")

def calcularIntervalo():
 perc = func.calcularPercnetual(m1,m2,m3,m4,m5)
 print(f"{m5} mA é = ", perc," % no intevalo de 1 a 5:")

def calcularSinalQV():
  sinal = func.sinalQuatroV(n1,n2,n3,n4,n5,n6,n7)
  print(f"{n5}% equivale a :",sinal,"Volts no intevalo de 1 a 5 volts:")
  
def mainMenu():
     while True:
         mostraMenu()
         opcao =input("Escolha uma opção: ")        
         if opcao == "1":
             calcularSinalQV()             
         elif opcao == "2":
             calcularIntervalo()
         elif opcao == "3":
             sys.exit()         
         else:
             print("Opção inválida: ")
            