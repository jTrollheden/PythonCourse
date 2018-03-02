import GUIdrawer as graphics
import logicTexas as log

# TODO: Fixa Gameview(GameState()) och
# TODO: self.game_state vidare i GameView
if __name__ == "__main__":
    [game_state, centercards, player1, player2] = log.execute()
    graphics.execute(game_state, centercards, player1, player2)