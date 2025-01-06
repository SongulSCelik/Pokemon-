# POKEMON-BATTLE-GAME

A Python-based Pokémon battle simulator! This project demonstrates object-oriented programming principles and game logic, where two teams of Pokémon battle until one team emerges victorious.

---

## 📝 Features

- **Team-Based Battles:** Players control teams of Pokémon, each with unique stats and moves.
- **Type Advantage System:** Moves have type advantages/disadvantages (e.g., Water is strong against Fire).
- **Item Usage:** Players can use Potions to heal and Pokéballs to catch opponent Pokémon.
- **Dynamic Switching:** Automatically switches to the next Pokémon when one faints.
- **Interactive Gameplay:** Players choose moves and actions for their Pokémon during battles.

---

## 📚 How to Play

1. **Start the Game:**
   - The program initializes with two predefined teams of Pokémon.

2. **Choose Actions:**
   - Players alternate turns, choosing actions for their Pokémon:
     - **(1) Attack:** Select a move to damage the opponent.
     - **(2) Use Potion:** Heal your active Pokémon.
     - **(3) Throw Pokéball:** Attempt to catch the opponent's Pokémon.

3. **Battle Logic:**
   - Pokémon faint when their HP drops to 0.
   - The game automatically switches to the next Pokémon when one faints.

4. **Win Condition:**
   - The game ends when all Pokémon on one team faint, and the opposing team wins.

---

### 🎲 Example Gameplay
Charmander added to the team. Pikachu added to the team. Squirtle added to the team. Bulbasaur added to the team. Battle Start! Team 1's turn: Choose action: (1) Attack (2) Use Potion (3) Throw Pokeball: 1 Available moves: 0: Flame Thrower (Type: Fire, Power: 50) 1: Water Gun (Type: Water, Power: 40) Choose move (0-1): 1 Charmander uses Water Gun on Squirtle! Squirtle takes 44 damage. Remaining HP: 56 Team 2's turn: Choose action: (1) Attack (2) Use Potion (3) Throw Pokeball: 1 Available moves: 0: Water Gun (Type: Water, Power: 40) 1: Vine Whip (Type: Grass, Power: 35) Choose move (0-1): 1 Squirtle uses Vine Whip on Charmander! Charmander takes 19 damage. Remaining HP: 81 ... Bulbasaur has fainted! Team 2 has no more Pokémon. Team 1 wins!


---

## 🛠️ Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/SongulSCelik/Pokemon.git
   cd Pokemon
 2.Run the code: python main.py
 3.Requirements:
  Python 3.7 or higher (no external libraries required).




🌟 Features to Add in the Future

AI Opponent: Add AI logic for the opponent’s actions.
Custom Teams: Allow players to select or create their own teams.
Advanced Type Chart: Expand type effectiveness for more Pokémon types.
Battle History: Log battle events for replayability or debugging.


🛠️ Project Structure

*battle.py:
Contains the Battle class for managing team battles.
*items.py: 
Contains the Item, Potion, and Pokeball classes for in-game items.
*move.py: 
Contains the Move class for defining Pokémon moves.
*pokemon.py: 
Contains the Pokemon class for Pokémon logic.
*team.py:
Contains the Team class for managing Pokémon teams.
*main.py: 
Entry point for the game.



Enjoy the game and unleash your inner Pokémon trainer! 🎮✨
