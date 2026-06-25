#nome do sabor -> string
#categoria do sabor (salgado ou doce) -> string
#disponibilidade do sabor (disponivel ou indisponivel) -> boolean (False - por default)

#classe
class Sabores_Pizza:
    sabores = []
    
    #self seria o equivalente ao this usado em java
    #tais palavras apontam para a instancia atual do objeto q esta trabalhando
    #usado para diferenciaciao de atributos locais de classe com nomes iguais e chamar
    #um contrutuor a partir de outro
    #nao eh obrigatorio o uso do self ou this em python, mas por convencao se eh usado, mas poderia ser algo como ex: self.nome_sabor
    def __init__(self, nome_sabor, categoria_sabor, preco_sabor, ingredientes_sabor, disponibilidade_sabor=False):
        self.nome_sabor = nome_sabor
        self.categoria_sabor = categoria_sabor
        self.preco_sabor = preco_sabor
        self.ingredientes_sabor = ingredientes_sabor
        self.disponibilidade_sabor = disponibilidade_sabor
        
        Sabores_Pizza.sabores.append(self)
                 
    def __str__(self):                              
        return f'''{self.nome_sabor} | {self.categoria_sabor} | {self.preco_sabor} | {self.disponibilidade_sabor}
                  {self.ingredientes_sabor}'''
    
    def cardapio_sabores():
        for sabor in Sabores_Pizza.sabores:
            print(f'''>>{sabor.nome_sabor.ljust(5)} | {sabor.categoria_sabor.ljust(5)} | {sabor.preco_sabor} | {sabor.disponibilidade_sabor}
  {sabor.ingredientes_sabor}\n''')


sabor_calabria = Sabores_Pizza(
    'calabria', 
    'salgada',
    34.00,
    'queijo de bufala, molho de tomate da casa e calabresa',
    True
    )
sabor_ninho = Sabores_Pizza(
    'ninho', 
    'doce',
    25.00,
    'brigadeiro branco, leite ninho em pó',
    )

Sabores_Pizza.cardapio_sabores()