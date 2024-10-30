import numpy as np

class State:
    def __init__(self, population: int, electoral_votes: int, popular_votes: NDArray[int]):
        self.population = population
        self.electoral_votes = electoral_votes
        self.popular_votes = popular_votes
