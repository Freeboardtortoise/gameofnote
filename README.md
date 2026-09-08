# Pack of Worlds
A retor sandbox survival game where your both inventory and chests are physical spaces you can enter... All built in tic80

## 🎮 About
### what is the game
the game is a sanbox survival game
### The gameplay loop
Wonder around and collect recources, mine, get jump scared by a mob, kill it, and then enter your backpack to place the things you got into your inventroy one by one and orgonise it.
### What makes it intresting?
you can enter your backpack

## ✨ Features

- procedural generation
- ores
- weapons
- vision system to make sure you cant see things you arenst supposed to be able too see

## 🚀 Getting Started

### Requirements

- tic80
- tic80
- None

### Installation
```bash
git clone https://github.com/freeboardtortoise/gameofnote.git
cd gameofnote
```
##### windows
```
 SDL_AUDIODRIVER=dummy xvfb-run --auto-servernum tic80 --cli --soft --fs=. --cmd "load sandbox_game.tic & import code code.py & export win game.exe & exit" < /dev/null
```
##### Mac
```
SDL_AUDIODRIVER=dummy xvfb-run --auto-servernum tic80 --cli --soft --fs=. --cmd "load sandbox_game.tic & import code code.py & export mac game-mac & exit" < /dev/null
```
##### Linux
```
 SDL_AUDIODRIVER=dummy xvfb-run --auto-servernum tic80 --cli --soft --fs=. --cmd "load sandbox_game.py & import code code.py & export linux game-linux & exit" < /dev/null || \
```
