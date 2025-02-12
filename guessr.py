import random

# List of words to choose from
words = ['python', 'programming', 'developer', 'algorithm', 'machine', 'artificial', 'intelligence', 'data', 'jeep', 'dodge', 'chrysler', 'ram', 'ford', 'lincoln', 'mazda', 'blanket', 'orchid', 'lantern', 'pizza', 'moonlight', 'compass', 'gravity', 'whisper', 'raindrop', 'galaxy', 'jellyfish', 'cinnamon', 'breeze', 'blueprint', 'trampoline', 'waffle', 'horizon', 'puppet', 'guitar', 'monarch', 'umbrella', 'pineapple', 'velvet', 'shadow', 'puddle', 'tumble', 'stardust', 'volcano', 'tortoise', 'meadow', 'ribbon', 'sculptor', 'rocket', 'puzzle', 'acorn', 'lighthouse', 'glacier', 'firefly', 'squirrel', 'ladder', 'notebook', 'tapestry', 'mirage', 'tidal', 'carousel', 'fountain', 'nectar', 'zipper', 'blizzard', 'bicycle', 'horizon', 'crocus', 'whisper', 'labyrinth', 'sparkle', 'marshmallow', 'carousel', 'sunset', 'jellybean', 'echo', 'stream', 'clownfish', 'magnolia', 'quicksand', 'hammock', 'potion', 'raccoon', 'velvet', 'cactus', 'picnic', 'lantern', 'treble', 'mistletoe', 'obsidian', 'pomegranate', 'glacier', 'nomad', 'wisteria', 'dreamscape', 'parrot', 'volcano', 'sapphire', 'spiral', 'lullaby', 'bumblebee']
# Pick a random word from the list
secret_word = random.choice(words)

# Scramble the letters of the word
scrambled_word = ''.join(random.sample(secret_word, len(secret_word)))

print("Welcome to the Scrambled Word Game!")
print(f"Here's the scrambled word: {scrambled_word}")

# Allow the player to guess
attempts = 0
while True:
    guess = input("Guess the word: ").lower()
    attempts += 1
    
    if guess == secret_word:
        print(f"Congratulations! You've guessed the word '{secret_word}' in {attempts} attempts.")
        
        break
    else:
        print("Oops! Try again.")