import json 
from pathlib import Path
from random import randint

ARQUIVO = Path("../data/cadastro_estoque.json")

produto0 = {"Id_cadastro" : "",
            "Cod_barra" : "",
            "Descrição" : "",
            "Quantidade" : "",
            "Valor_unidade" : "",
        }

lista_produtos = [produto0]


class CadastroProduto:
    """Operação que cadatra produto e salva em arquivo"""
    
    def __init__(self):
        """Inicializa os valores essenciais para o cadastro do produto"""
        #self.Id_cadastro = Id_cadastro
        #self.Cod_barra = Cod_barra
        #self.Descrição = Descrição
        #self.Quantidade = Quantidade
        #self.Valor_unidade = Valor_unidade

    def prompt_campo_cadastro(self):
        """Obtem do usuário as informações do produto as salva no dicionário"""
        self.var_id =int(input("Digite o id para mostrar o produto ou 0 para cadastrar um produto: "))

        self.var_cod_barra = int(input("Preencha o código de barras: "))

        self.var_Descricao = input("Coloque uma descrição: ")
    
        self.var_Quantidade = int(input("Qtd no estoque: "))

        self.var_Valor_unidade = float(input("Valor unidade: "))

        return {
            "Id cadastro" : self.var_id,
            "Codigo_barra" : self.var_cod_barra,
            "Descrição" : self.var_Descricao,
            "Quantidade" : self.var_Quantidade,
            "Valor Unidade" : self.var_Valor_unidade
        }


    def salvar_informacoes(self):
        """Salva informações em dicionário e depois em arquivo"""
        self.id_gerado = self.cria_um_id_para_produto()
        self.input_prompts = self.prompt_campo_cadastro


        produto0["Id_cadastro"] = self.id_gerado
        produto0["Cod_barra"] = self.var_cod_barra
        produto0["Descrição"] = self.var_Descricao
        produto0["Quantidade"] = self.var_Quantidade
        produto0["Valor_unidade"] = self.var_Valor_unidade

        if ARQUIVO.exists():
            with ARQUIVO.open("r", encoding="utf-8") as f:
                lista_produtos = json.load(f)
        else:
            lista_produtos = []

        lista_produtos.append(produto0)

        with ARQUIVO.open("w", encoding="utf-8") as f:
            json.dump(lista_produtos, f, indent=4, ensure_ascii=False)


    def verifica_se_busca_ou_cadastro(self):
        """Verifica se o usuário está fazendo uma busca ou está cadastrando um produto"""
        self.verificar_operacao = self.prompt_campo_cadastro()
       
        if self.verificar_operacao.var_id == 0:
            flag = True
        else:
            flag = False


    def cria_um_id_para_produto(self):
        """Gera um id aleatório, salva e define como id do produto"""
        self.var_rand_id = randint(10000, 99999)
        return self.var_rand_id
    
        









