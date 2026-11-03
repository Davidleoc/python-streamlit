from restaurante import Restaurante  # Importa a classe Restaurante do arquivo restaurante.py localizado na pasta modelos_restaurantes

restaurante_praca = Restaurante('Praça', 'Gourmet')
pizza_express = Restaurante('Pizza Express', 'Italiana')
restaurante_japones = Restaurante ('Japa-jantas', 'Japones' )

restaurante_japones.alterar_estado()
# restaurante_praca.alterar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()