import GUIdrawer as graphics
import logicTexas as log

# TODO: Fixa Gameview(GameState()) och
# TODO: self.game_state vidare i GameView
if __name__ == "__main__":
    game_state = log.execute()
    graphics.execute(game_state)

# GUIdrawer - Programmet som ritar upp fönstret (basicGUIdrawer har ingen input från
# någon annan fil AKA simple as it gets)

# logicTexas - Min spellogik

# cardlib - kort biblioteket

# pokergame - Min "exe" fil typ

# Vart jag är just nu: Koppla logiken med GUIn ytterligare samt skriva "Hur man vinner"
