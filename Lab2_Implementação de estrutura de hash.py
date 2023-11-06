class Noh:
    qtdNoh = 0
    def __init__(self, val):
        self.val = val
        self.proximo = None
    
class Linguagens:
    def __init__(self, nome):
        self.nome = nome

class TabelaDeHash:
    qtdNoh = 0
    armario1 = Noh("Armario 1")
    armario2 = Noh("Armario 2")
    armario3 = Noh("Armario 3")
    
    def funcaoDeHash(linguagem = Linguagens):
        vogais = ['A','E','I','O','U']
        if linguagem.nome[0].upper() in vogais:
            return TabelaDeHash.armario1
        elif linguagem.nome[0].upper() >= "B" and linguagem.nome[0].upper() <= "M" and linguagem.nome[0].upper() not in vogais:
            return TabelaDeHash.armario2
        else:
            return TabelaDeHash.armario3
    
    def inserir(linguagem):
        armario = TabelaDeHash.funcaoDeHash(linguagem)
        if armario.qtdNoh == 0:
            novo_noh = Noh(linguagem)
            armario.proximo = novo_noh
            armario.qtdNoh += 1
        else:
            novo_noh = Noh(linguagem)
            atual = armario.proximo
            for i in range(0, armario.qtdNoh):
                if atual.proximo == None: 
                    atual.proximo = novo_noh
                    armario.qtdNoh += 1
                    
                else:
                    atual = atual.proximo
    

    def busca(linguagemProcurada):
        cont = 1
        armario = TabelaDeHash.funcaoDeHash(Linguagens(linguagemProcurada))
        armarioNoh = armario.proximo
        print(armarioNoh.val.nome)
        for i in range(armario.qtdNoh):   
            if linguagemProcurada == armarioNoh.val.nome:
                print(armario.val + ", Posição "+str(cont)+" = "+ armarioNoh.val.nome)
                print("Posição = "+str(cont))
                return True
            else:
                armarioNoh = armarioNoh.proximo
                cont += 1
        else:
            print(linguagemProcurada+" não está na tabela de Hash")
            return False
        
        
    def excluir(linguagemProcurada):
        armario = TabelaDeHash.funcaoDeHash(Linguagens(linguagemProcurada))
        armarioNoh = armario
        for i in range(armario.qtdNoh):
            if armario.proximo.val.nome == linguagemProcurada:
                armario.proximo = armario.proximo.proximo
                return True
            elif linguagemProcurada == armarioNoh.proximo.val.nome:
                armarioNoh.proximo = armarioNoh.proximo.proximo
                return True
            else:
                armarioNoh = armarioNoh.proximo
        else:
            return False


#TESTES DE INSERÇÃO
l1 = Linguagens("Angular")
l2 = Linguagens("Elixir")
l3 = Linguagens("indio")
TabelaDeHash.inserir(l2)
TabelaDeHash.inserir(l1)
TabelaDeHash.inserir(l3)

l4 = Linguagens("Java")
l5 = Linguagens("C++")
l6 = Linguagens("C#")
TabelaDeHash.inserir(l5)
TabelaDeHash.inserir(l4)
TabelaDeHash.inserir(l6)

l7 = Linguagens("Python")
l8 = Linguagens("php")
l9 = Linguagens("rUBy")
TabelaDeHash.inserir(l7)
TabelaDeHash.inserir(l8)
TabelaDeHash.inserir(l9)

#TESTE DE EXLCUSÃO
print(TabelaDeHash.excluir("Python"))
print("**********************")
print("**********************")
print("**********************")
#TESTE DE BUSCA
print(TabelaDeHash.busca("rUBy"))
print("**********************")
print("**********************")
print("**********************")
#PERCORRENDO A LISTA LIGADA
tabela1 = TabelaDeHash.armario1
tabela2 = TabelaDeHash.armario2
tabela3 = TabelaDeHash.armario3
def imprimir(tabela):
    if type(tabela.val) == str:
        imprimir(tabela.proximo)   
    else:
        print(tabela.val.nome)
        if tabela.proximo != None:
            imprimir(tabela.proximo)
        else:
            return None

#print(imprimir(tabela1))
#print("**********************")
#print(imprimir(tabela2))
#print("**********************")
print(imprimir(tabela3))
print("**********************")
print(imprimir(tabela3))