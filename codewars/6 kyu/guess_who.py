class GuessWho():
    def __init__(self, character):
        self.characteristic = {
            'Jean-Claude': {'Glasses', 'Bald', 'Small mouth', 'Small nose', 'Brown eyes', 'White hair', 'Male'}, 
            'Pierre': {'Small nose', 'Big mouth', 'Brown eyes', 'Brown hair', 'Male', 'Mustache'}, 
            'Jean': {'Big mouth', 'Big nose', 'White hair', 'Male', 'Blue eyes'}, 
            'Amelie': {'Small nose', 'Small mouth', 'Long hair', 'Brown eyes', 'Brown hair', 'Female', 'Hat'}, 
            'Mirabelle': {'Small mouth', 'Big nose', 'Brown eyes', 'Earrings', 'Female', 'Black hair'}, 
            'Isabelle': {'Glasses', 'Small mouth', 'Small nose', 'Brown eyes', 'Female', 'Blonde hair', 'Hat'}, 
            'Antonin': {'Small nose', 'Big mouth', 'Brown eyes', 'Male', 'Black hair'}, 
            'Bernard': {'Small nose', 'Brown eyes', 'Brown hair', 'Male', 'Hat'}, 
            'Owen': {'Small nose', 'Small mouth', 'Male', 'Blue eyes', 'Blonde hair'}, 
            'Dylan': {'Small nose', 'Small mouth', 'Bald', 'Brown eyes', 'Beard', 'Male', 'Blonde hair'}, 
            'Herbert': {'Small mouth', 'Bald', 'Big nose', 'Brown eyes', 'Male', 'Blonde hair'}, 
            'Christine': {'Small nose', 'Small mouth', 'Long hair', 'Female', 'Blue eyes', 'Blonde hair'}, 
            'Luc': {'Small nose', 'Small mouth', 'Glasses', 'Brown eyes', 'White hair', 'Male'}, 
            'Cecilian': {'Small nose', 'Small mouth', 'Brown eyes', 'Ginger hair', 'Male'}, 
            'Lionel': {'Big mouth', 'Big nose', 'Brown eyes', 'Brown hair', 'Male', 'Mustache'}, 
            'Benoit': {'Small nose', 'Small mouth', 'Brown eyes', 'Brown hair', 'Beard', 'Male', 'Mustache'}, 
            'Robert': {'Big mouth', 'Big nose', 'Brown hair', 'Male', 'Blue eyes'}, 
            'Charline': {'Small nose', 'Big mouth', 'Brown hair', 'White hair', 'Female'}, 
            'Renaud': {'Small nose', 'Big mouth', 'Brown eyes', 'Male', 'Blonde hair', 'Mustache'}, 
            'Michel': {'Small nose', 'Big mouth', 'Brown eyes', 'Beard', 'Male', 'Blonde hair'}, 
            'Pierre-Louis': {'Small nose', 'Small mouth', 'Bald', 'Glasses', 'Brown hair', 'Male', 'Blue eyes'}, 
            'Etienne': {'Small nose', 'Small mouth', 'Glasses', 'Brown eyes', 'Male', 'Blonde hair'}, 
            'Henri': {'Small nose', 'Big mouth', 'Brown eyes', 'White hair', 'Male', 'Hat'}, 
            'Damien': {'Small nose', 'Big mouth', 'Brown eyes', 'Male', 'Blonde hair', 'Hat'}
        }
        self.characters = self.characteristic.keys()
        self.character = character
        self.turns = 0

    def guess(self, guess):
        self.turns += 1
        
        if guess == self.character:
                return [f'Correct! in {self.turns} turns']

        if guess in self.characters:
            return {self.character}
        
        if guess in self.characteristic[self.character]:
            self.characters = {character for character in self.characters if guess in self.characteristic[character]}
        else:
            self.characters = {character for character in self.characters if guess not in self.characteristic[character]}
        
        return self.characters
        