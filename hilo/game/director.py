from game.card import Card


class Director:
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        card (Card): A single Card instance.
        is_playing (boolean): Whether or not the game is being played.
        guess (boolean): Whether they guessed high or not.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """
        self.card = Card()
        self.is_playing = True
        self.guess = True
        self.score = 0
        self.total_score = 100

        self.card.draw_card()

    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they guess higher or lower.

        Args:
            self (Director): An instance of Director.
        """
        userChoice = input("Higher or Lower? [h/l] ")
        self.guess = (userChoice == "h")

    def prompt_play(self):
        """Ask the user if they want to keep playing.

        Args:
            self (Director): An instance of Director.
        """
        userChoice = input("Play again? [y/n] ")
        self.is_playing = (userChoice == "y")

    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        print("\nThe card is:",str(self.card.get_value()))
        self.get_inputs()
        self.card.draw_card()
        print("Next card was:",str(self.card.get_value()))

    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        if self.guess and self.card.is_greater:
            self.score = 100
        elif (not self.guess) and (not self.card.is_greater):
            self.score = 100
        else:
            self.score = -75
        
        self.total_score += self.score
        print(f"Your score is: {self.total_score}")
        if not self.total_score > 0:
            self.is_playing = False
        else:
            self.prompt_play()
            if self.is_playing:
                self.score = 0
