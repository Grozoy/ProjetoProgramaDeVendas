from operacao_cadastro_fiado import MarcarFiado
import json
from pathlib import Path



class FecharConta(MarcarFiado):
    """Modifica dicionário cadastro de clientes, flag pago, para True"""

    def __init__(self):
        super().__init__()
        self.ARQUIVO_ESTOQUE = Path("../data/cadastro_estoque.json")
        self.ARQUIVO_CLIENTES = Path("../data/cadastro_clientes.json")
        
        
    def abre_o_arquivo_clientes(self):
        
        with self.ARQUIVO_CLIENTES.open("r", encoding="utf8") as f:
            self.clientes = json.load(f)

    def escreve_mudanças_no_arquivo_clientes(self):

        with self.ARQUIVO_CLIENTES.open("w", encoding="utf8") as file:
            json.dump(self.clientes, file, indent=4, ensure_ascii=False)

    def lista_e_escolhe_clientes(self):
        """Lista todos os clientes e seus indexes"""

        print("clear")
        print("escolha o cliente que deseja marcar: \n")
        
        for self.index ,self.cliente in enumerate(self.clientes):
            print(self.cliente["Nome"])
            print(f'[{self.index}]\n')    
    
        self.escolhe_cliente1 = int(input("Digite o index do cliente que deseja consultar a conta: "))
        return self.escolhe_cliente1
    
    def lista_produtos_na_conta(self):
        """Lista e escolhe os produtos na conta do cliente escolhido"""
        self.tamanho_conta = [self.x for self.x in range(len(self.clientes[self.escolhe_cliente1]["Conta"]))]

        for self.index, self.produto in enumerate(self.clientes):
            print(f'{self.index}')
            print(f'{self.produto["Conta"]}{self.tamanho_conta}')

        self.escolhe_produto = int(input("Escolha o produto pelo index: "))
        return self.escolhe_produto
    

    
    def soma_divida_total(self):
        """Pega o dicionário conta e soma todos produtos marcados na conta"""
        
        for self.valor in self.clientes[self.escolhe_cliente1]["Conta"]["Total"]:
            self.valor += self.valor



    def escreve_flag_pago_para_true(self):
        """Procura dicionario e cliente para mudar pago para true"""
        self.escolha = input("Deseja marcar como Pago a conta? s/n ")

        if self.escolha == "s":
            self.clientes[self.escolhe_cliente1]["Conta"][self.escolhe_produto]["Pago"] = True

