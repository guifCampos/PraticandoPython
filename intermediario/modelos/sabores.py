#nome do sabor -> string
#categoria do sabor (salgado ou doce) -> string
#disponibilidade do sabor (disponivel ou indisponivel) -> boolean (False - por default)

#classe
class Sabores_Pizza:
    sabores = []
    
    #self seria o equivalente ao this usado em java
    #tais palavras apontam para a instancia atual do objeto q esta trabalhando
    #usado para diferenciacao de atributos da instancia de variaveis locais ou parametros da classe
    #com nomes iguais e chamar um construtuor a partir de outro
    #nao eh obrigatorio o uso do self ou this em python, mas por convencao se eh usado, mas poderia ser algo como ex: self.nome_sabor
    def __init__(self, nome_sabor, categoria_sabor, preco_sabor, ingredientes_sabor, disponibilidade_sabor=False):
        #o "_" adicionado entre o "self." e a variavel significa q aquele atributo faz parte da implementacao interna da classe, como um aviso p q seja evitado o acesso direto a ele
        self._nome_sabor = nome_sabor.title() #todos os sabores de pizza qnd forem listados aprarecerao com os estilo de titulo ("Titulo") por conta da funcao "title()" do python
        self.categoria_sabor = categoria_sabor.upper() #todos as categorias exibidas das pizzas serao apresentadas com todas as letras maiusculas
        self.preco_sabor = preco_sabor
        self.ingredientes_sabor = ingredientes_sabor
        self._disponibilidade_sabor = False
        
        Sabores_Pizza.sabores.append(self)
                 
    def __str__(self):                              
        return f'''{self.nome_sabor} | {self.categoria_sabor} | {self.preco_sabor} | {self.disponibilidade_sabor}
                  {self.ingredientes_sabor}'''
    
    def cardapio_sabores():
        print(f"{'SABOR'.ljust(21)} || {'CATEGORIA'.ljust(21)} || PRECO || DISPONIBILIDADE")
        for sabor in Sabores_Pizza.sabores:
            print(f'''>>{sabor._nome_sabor.ljust(19)} || {sabor.categoria_sabor.ljust(21)} || {sabor.preco_sabor} || {sabor.disponibilidade_sabor}
  {sabor.ingredientes_sabor}
==========================================================================''')

    #@property eh um decorator q transforma um metodo em um atributo
    #possibilita o controle de acesso, validacao de dados e faz calculos
    #sem mudar a forma como o restante do codigo usa o objeto --> acessa o valor como se fosse uma variavel
    #no caso aqui estou buscando alterar a disponibilidade
    #na linha 19 "self.disponibilidade_sabor = disponibilidade_sabor", aqui uso a funcao nomeada como "disponibilidade" e volto a chamar o "disponibilidade_sabor"
    @property
    def disponibilidade_sabor(self):
        return '|✓|' if self._disponibilidade_sabor else '|X|'


sabor_calabria = Sabores_Pizza(
    'calabria', 
    'salgada',
    34.00,
    '|queijo de bufala, molho de tomate da casa e calabresa',
    )
sabor_ninho = Sabores_Pizza(
    'ninho', 
    'doce',
    25.00,
    '|brigadeiro branco, leite ninho em pó',
    )

Sabores_Pizza.cardapio_sabores()