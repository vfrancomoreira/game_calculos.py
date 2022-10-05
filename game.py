from models.calcular import Calcular

def main() -> None:
    pontos: int = 0
    jogar(pontos)

def jogar(pontos: int) -> None:
    dificuldade: int = int(input('Informe o nível de dificuldade desejado [ 1 | 2 | 3 | 4 ]: '))

    calc: Calcular = Calcular(dificuldade)

    print('\nInforme o resultado para a seguinte operação: ')
    calc.mostra_operacao() # 5 + 4 =
    
    resultado: int = int(input())

    if calc.checar_resultado(resultado):
       pontos += 1
       print(f'Você tem {pontos} pontos(s).')
    
    continuar: int = int(input('\nDeseja continuar no jogo? [1 - SIM | 0 - NÃO] '))

    if continuar:
        jogar(pontos)
    else:
        print(f'Você finalizou com {pontos} ponto(s).')
        print('Até a próxima!')


if __name__ == '__main__':
    main()
