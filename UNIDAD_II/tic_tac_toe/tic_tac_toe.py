from jugador import jugador
from tablero import tablero

#MAIN
if __name__ == "__main__":
    print("*********BIENVENIDOS AL GATO*********")
    nombre = input("Ingrese el nombre del Usuario: ")
    humano = jugador(nombre, False)
    
    #nombre = input("Ingrese el nombre del Usuario: ")
    #humano2 = jugador(nombre, False)
    bot = jugador("BOT", True)
    vot = jugador("VOT", True)

    tictactoe = tablero(humano, bot)
    #tictactoe = tablero(bot,humano)
    #tictactoe = tablero(humano, humano2)
    #tictactoe = tablero(bot, vot)
    tictactoe.inicia_partida()