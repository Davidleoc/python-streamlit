from avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome_restaurante, categoria): # Construtor da classe. O self faz cada item ser único
        self._nome_restaurante = nome_restaurante.title() # O método title() coloca a primeira letra de cada palavra em maiúscula. o upper() deixa todas as letras maiúsculas e o lower() deixa todas as letras minúsculas
        self._categoria = categoria
        self._restaurante_ativo = False # Atributo protegido, não pode ser acessado fora da classe, só pode ser acessado por métodos da classe
        self._avaliacao = []
        Restaurante.restaurantes.append(self) # Adiciona o objeto criado à lista de restaurantes

    def __str__(self): # Método que mostra em string representando o objeto, para não mostrar o endereço de memória
        return f'{self._nome_restaurante} | {self._categoria} | {self._restaurante_ativo}'

    @classmethod # Indica que o método é de classe, não precisa de self, mas precisa do cls. O cls é uma referência à própria classe
    def listar_restaurantes(cls): 
        print(f"{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | Status")
        print(f"{''.ljust(25)} {'|'.ljust(27)} | {''.ljust(27)} |")
        for restalrante in cls.restaurantes:
            print(f'{restalrante._nome_restaurante.ljust(25)} | {restalrante._categoria.ljust(25)} | {str(restalrante.media_avaliacoes).ljust(25)} | {restalrante._restaurante_ativo}')
        
        @property # Modifica a forma como o atributo vai ser lido. Sobre o @: Um decorator modifica ou adiciona um comportamento a uma função ou método
        def ativo(self):
            return "Ativo" if self._restaurante_ativo else "Inativo" # sintaxe padrão: valor_se_verdadeiro if condição else valor_se_falso
    
    def alterar_estado(self): # É um metodo para os objetos da classe, não precisa do @classmethod, pois o self é uma referência ao objeto que chamou o método
        self._restaurante_ativo = not self._restaurante_ativo # Altera o estado do restaurante para o oposto do atual

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        soma_notas = sum(avaliacao.nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media_notas = round (soma_notas / quantidade_notas, 1) # o round e o ", 1" garantem que só vai ter uma casa decimal 
        return media_notas
    


# restaurante_praca = Restaurante('Praça', 'Gourmet')
# pizza_express = Restaurante('Pizza Express', 'Italiana')
# restaurante_praca.alterar_estado()
# Restaurante.listar_restaurantes()