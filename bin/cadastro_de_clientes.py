import json 
from pathlib import Path
from random import randint

ARQUIVO = Path("../data/cadastro_clientes.json")

cliente0 = {"Id_cadastro" : "",
            "Nome" : "",
            "CPF" : "",
            "Telefone" : "",
            "E-mail" : "",
            "Endereço" : "",
        }

lista_clientes = [cliente0]


class CadastroCliente:
    """Operação que cadatra o cliente e salva em arquivo"""
    
    def __init__(self):
        """Inicializa os valores essenciais para o cadastro do cliente"""
        #self.Id_cadastro = Id_cadastro
        #self.Cod_barra = Cod_barra
        #self.Descrição = Descrição
        #self.Quantidade = Quantidade
        #self.Valor_unidade = Valor_unidade

    def prompt_campo_cadastro(self):
        """Obtem do usuário as informações do produto as salva no dicionário"""
        self.var_id =int(input("Digite o id para mostrar o produto ou 0 para cadastrar um cliente: "))

        self.var_nome = input("Digite o nome: ")

        self.var_Telefone = int(input("Digite o telefone: "))
    
        self.var_E_mail = input("Digite o E-mail: ")

        self.var_endereco = input("Digite o endereço: ")

        self.var_cpf = int(input("Digite o CPF: "))

        self.conta = []
        self.var_fiado = []

        return {
            "Id cadastro" : self.var_id,
            "Nome" : self.var_nome,
            "Telefone" : self.var_Telefone,
            "E-mail" : self.var_E_mail,
            "Endereço" : self.var_endereco,
            "CPF" : self.var_cpf,
            "Conta" : self.var_fiado
        }


    def salvar_informacoes(self):
        """Salva informações em dicionário e depois em arquivo"""
        self.id_gerado = self.cria_um_id_para_produto()
        self.input_prompts = self.prompt_campo_cadastro


        cliente0["Id_cadastro"] = self.id_gerado
        cliente0["Nome"] = self.var_nome
        cliente0["Telefone"] = self.var_Telefone
        cliente0["E-mail"] = self.var_E_mail
        cliente0["Endereço"] = self.var_endereco
        cliente0["CPF"] = self.var_cpf
        cliente0["Conta"] = self.var_fiado

        if ARQUIVO.exists():
            with ARQUIVO.open("r", encoding="utf-8") as f:
                lista_clientes = json.load(f)
        else:
            lista_clientes = []

        lista_clientes.append(cliente0)

        with ARQUIVO.open("w", encoding="utf-8") as f:
            json.dump(lista_clientes, f, indent=4, ensure_ascii=False)


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
    
        









