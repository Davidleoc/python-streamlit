class Avaliacao:
    def __init__(self, cliente, nota):
        self._cliente = cliente
        self._nota = self._validar_nota(nota)

    @classmethod
    def _validar_nota (nota):
        try:
            nota = int(nota)
        except(ValueError, TypeError): # capitura os tipos de erro que podem ocorrer na conversão para inteiro
            raise ValueError(f"Nota inválida: {nota!r}. Informe um número inteiro.") # o raise substitui o erro original por uma mensagem personalizada. O !r mostra a representação da variável, incluindo aspas se for string
        if not 0 <= nota <= 10:  # ajuste o intervalo à sua regra
            raise ValueError("A nota deve estar entre 0 e 10.")
        return nota

