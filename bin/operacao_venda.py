import os
import json
from pathlib import Path
from datetime import date


ARQUIVO_ESTOQUE = Path("../data/cadastro_estoque.json")
ARQUIVO_VENDAS = Path("../data/cadastro_vendas.json")

class FazerVenda():
    """Tentando fazer operção venda"""

    def __init__(self):
        self.ARQUIVO_ESTOQUE = ARQUIVO_ESTOQUE
        self.ARQUIVO_VENDAS = ARQUIVO_VENDAS
        self.lista_de_compras = []
        self.total = 0
        

    def abrir_arquivo_estoque(self):

        with self.ARQUIVO_ESTOQUE.open("r", encoding="utf8") as f:
            self.estoque = json.load(f)

    def abrir_arquivo_vendas(self):

        with self.ARQUIVO_VENDAS.open("r", encoding="utf8") as file:
            self.vendas = json.load(file)

    def escreve_arquivo_estoque(self):

        with self.ARQUIVO_ESTOQUE.open("w", encoding="utf8") as f:
            json.dump(self.estoque, f, indent=4, ensure_ascii=False)

    def escreve_arquivo_vendas(self):

        with self.ARQUIVO_VENDAS.open("w", encoding="utf8") as file:
            json.dump(self.vendas, file, indent=4, ensure_ascii=False)


    def listar_produtos(self):

        for self.index, self.produto in enumerate(self.estoque):
            print(f'{self.produto["Descrição"]} - {self.produto["Valor_unidade"]}')
            print(f'[{self.index}]\n')
            

    
    def soma_valores_dos_produtos_no_carrinho(self):


        for self.produto in self.lista_de_compras:
            self.total += self.produto["Total"]


    def faz_carrinho_de_compra(self):
        
        self.escolhe_produto = int(input("Escolha o produto para colocar no carrinho pelo index: "))

        self.lista_de_compras.append(self.estoque[self.escolhe_produto])
        os.system("clear")

        self.quantidade_levada = int(input("Quantas unidades deseja levar? "))

        self.total += (self.estoque[self.escolhe_produto]["Valor_unidade"] * \
                                    self.quantidade_levada)
            
    def mostra_carrinho_de_compras(self):

        for self.produto in self.lista_de_compras:
            print(self.produto["Descrição"])
            print(f'Valor un: {self.produto["Valor_unidade"]}')
                
        print(f'\nTotal: {self.total:.2f}')
            
    
    def modifica_lista_estoque_json(self):
        
        self.estoque[self.escolhe_produto]["Quantidade"] -= self.quantidade_levada

    
    def modifica_lista_vendas_json(self):

        self.vendas.append(self.lista_de_compras)



