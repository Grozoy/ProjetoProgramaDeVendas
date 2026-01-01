from os import system
from cadastro_de_produtos import CadastroProduto
from cadastro_de_clientes import CadastroCliente
from operacao_cadastro_fiado import MarcarFiado
from operacao_fechar_conta import FecharConta
from operacao_venda import FazerVenda


class Programa_de_vendas:
    """Inicializa o programa, suas dependências e configurações"""

    def __init__(self):
        self.operacao_cadastrar_produto = CadastroProduto()
        self.operacao_cadastrar_cliente = CadastroCliente()
        self.operacao_marcar_na_conta = MarcarFiado()
        self.operacao_fechar_venda_fiado = FecharConta()
        self.operação_venda = FazerVenda()

    
    def rodar_programa(self):
        """Executa o programa e seus métodos"""
        while True:
            system("clear")
            print("Cadastro de Produto[1]")
            print("Cadastro de cliente[2]")
            print("Compra fiado[3]")
            print("Fechar Venda Fiado[4]")
            print("Fazer Venda Comum[5]")
            print("Digite [0] para sair\n")

            escolha = int(input("Escolha o número da operação: "))

            if escolha == 1:
                self.operacao_cadastrar_produto.prompt_campo_cadastro()
                sair_ou_ficar = input("As informações estão corretas? s/n ")
                if sair_ou_ficar == "n":
                    continue
                self.operacao_cadastrar_produto.salvar_informacoes()
                encerrar_programa = input("Sair agora? s/n ")
                if encerrar_programa == "s":
                    break
                else:
                    continue
            
            elif escolha == 2:
                self.operacao_cadastrar_cliente.prompt_campo_cadastro()
                sair_ou_ficar = input("As informações estão corretas? s/n ")
                if sair_ou_ficar == "n":
                    continue
                self.operacao_cadastrar_cliente.salvar_informacoes()
                encerrar_programa = input("Sair agora? s/n ")
                if encerrar_programa == "s":
                    break

                else:
                    continue
                
            elif escolha == 3:
                while True:
                    self.operacao_marcar_na_conta.abre_o_arquivo_estoque()
                    self.operacao_marcar_na_conta.abre_o_arquivo_clientes()
                    self.operacao_marcar_na_conta.mostra_lista_de_clientes()
                    self.operacao_marcar_na_conta.mostra_lista_de_compra()
                    self.operacao_marcar_na_conta.cria_dicionário_produto_fiado()
                    self.operacao_marcar_na_conta.preenche_dicionário()
                    self.operacao_marcar_na_conta.concatena_produto_na_lista()
                    self.operacao_marcar_na_conta.salvar_carrinho()
                    continuar_ou_sair = input("informações corretas? s/n ")
                    if continuar_ou_sair == "n":
                        continue
                    else:
                        break
            
            elif escolha == 4:
                self.operacao_fechar_venda_fiado.abre_o_arquivo_clientes()
                self.operacao_fechar_venda_fiado.lista_e_escolhe_clientes()
                self.operacao_fechar_venda_fiado.lista_produtos_na_conta()
                self.operacao_fechar_venda_fiado.escreve_flag_pago_para_true()
                self.operacao_fechar_venda_fiado.escreve_mudanças_no_arquivo_clientes()
                

            elif escolha == 5:
                self.operação_venda.abrir_arquivo_estoque()
                self.operação_venda.abrir_arquivo_vendas()
                while True:
                    self.operação_venda.listar_produtos()
                    self.operação_venda.faz_carrinho_de_compra()
                    self.operação_venda.mostra_carrinho_de_compras()
                    self.escolha = input("Deseja colocar mais alguma coisa no carrinho? s/n ").lower()
                    if self.escolha == "s":
                        continue
                    else:
                        self.fluxo = input("Confirmar venda? s/n ").lower()
                        if self.fluxo == "s":
                            break
                        else:
                            continue
                    
                self.operação_venda.modifica_lista_estoque_json()
                self.operação_venda.modifica_lista_vendas_json()
                self.operação_venda.escreve_arquivo_estoque()
                self.operação_venda.escreve_arquivo_vendas()
                


            elif escolha == 0:
                break


if __name__ == "__main__":
    # Cria uma instancia do programa e executa
    ai = Programa_de_vendas()
    ai.rodar_programa()