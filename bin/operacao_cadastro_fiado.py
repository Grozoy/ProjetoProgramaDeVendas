import os

import json

from pathlib import Path
from datetime import date


class MarcarFiado:
    """Representa a operação de marcar produtos fiados"""

    def __init__(self):
        self.ARQUIVO_ESTOQUE = Path("../data/cadastro_estoque.json")
        self.ARQUIVO_CLIENTES = Path("../data/cadastro_clientes.json")


    def cria_dicionário_produto_fiado(self):
        
        # Pega a data de hoje
        self.d = date.today()
        self.data_formatada = f'{self.d.day}-{self.d.month}-{self.d.year}'

        self.pego_fiado = {
        "Id_cadastro": "",
        "Cod_barra": "",
        "Descrição": "",
        "Valor_unidade": 0,
        "Qtd_comprado" : 1,
        "Pago" : False,
        "Data" : self.data_formatada       
}  
        
        #Estas linhas pegam o pegam quantas unidades vão ser pegas, no módulo "mostra_lista_de_compra"
        # e coloca a chave "Total" no dicionário.

        self.pego_fiado["Valor_unidade"] = self.estoque[self.O_que_deseja_comprar]["Valor_unidade"]
        self.total =  self.pego_fiado["Valor_unidade"] * self.quantidade_levado
        self.pego_fiado["Total"] = self.total
        return self.pego_fiado
    


    def preenche_dicionário(self):
        """Usa o indice escolhido na lista de compra para selecionar o produto, e, pega informaçoes do
        estoque e joga na conta do cliente"""
        
        self.pego_fiado["Id_cadastro"] = self.estoque[self.O_que_deseja_comprar]["Id_cadastro"]
        self.pego_fiado["Cod_barra"] = self.estoque[self.O_que_deseja_comprar]["Cod_barra"]
        self.pego_fiado["Descrição"] = self.estoque[self.O_que_deseja_comprar]["Descrição"]
        self.pego_fiado["Qtd_comprado"] = self.quantidade_levado
        self.pego_fiado["Valor_unidade"] = self.estoque[self.O_que_deseja_comprar]["Valor_unidade"]

    def mostra_lista_de_clientes(self):
        """Cria interface que lista todos os clientes, pede o index do cliente escolhido e o retorna"""

        os.system("clear")
        print("escolha o cliente que deseja marcar: \n")
        
        for self.index ,self.cliente in enumerate(self.clientes):
            print(self.cliente["Nome"])
            print(f'[{self.index}]\n')    
    
        self.escolhe_cliente = int(input("Digite o index do cliente que deseja consultar a conta: "))
        return self.escolhe_cliente
    
    def abre_o_arquivo_estoque(self):
        """Abre arquivo estoque e salva json em variável"""

        with self.ARQUIVO_ESTOQUE.open("r", encoding="utf8") as f:
            self.estoque = json.load(f)

    def abre_o_arquivo_clientes(self):
        """Abre o arquivo clientes e salva json em variável"""

        with self.ARQUIVO_CLIENTES.open("r", encoding="utf8") as file:
            self.clientes = json.load(file)

    

    def mostra_lista_de_compra(self, quantidade_levado=1):
        """Coloca itens no carrinho"""
        self.lista_compra = []
        self.quantidade_levado = quantidade_levado

        for self.i, self.opcao in enumerate(self.estoque):
            print(f'[{self.i}] - {self.opcao["Descrição"]}')
            print(f'R${self.opcao["Valor_unidade"]}')

        self.O_que_deseja_comprar = int(input("Selecione o index do que deseja marcar: "))
        self.quantidade_levado = int(input("Quantas unidades para marcar? " ))
        
        return self.O_que_deseja_comprar

    def concatena_produto_na_lista(self):
        """Usa umm append para marcar os produtos selecionados na conta"""
        #self.lista_compra = [self.pego_fiado]
        self.clientes[self.escolhe_cliente]["Conta"].append(self.pego_fiado)

    
    def salvar_carrinho(self):
        """Salva a lista de compra na conta do cliente"""

        with self.ARQUIVO_CLIENTES.open("w", encoding="utf8") as f:
            json.dump(self.clientes, f, indent=4, ensure_ascii=False)
