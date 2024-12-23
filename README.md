# ECE-1000-Simon-Says-Game
This is a project for ECE 1000 class. Making a Simon Says Game using a Raspberry Pi Pico, Cathode LEDS, and LCD screen.

## Executive Summary
Simon Says is a classic memory game that challenges players to recall and repeat sequences of colors and sounds. This ECE-1000 project focuses on the design and assembly of an interactive Simon Says game prototype powered by a Raspberry Pi Pico microcontroller. The final product will be a functional and engaging device that allows players to test their memory skills through increasingly complex patterns of lights while trying to beat their highest score. Sounds emit from the Raspberry pi letting you know if you are right or wrong while and LCD screen keeps your score.

## Current Game Capabilites
At this moment the Simon Says game shows a sequence and then allows the user to input the same sequence back. If the user is correct the sequence gets longer. This continues until the user is incorrect. The game uses cathode RGB LEDS to represent the sequence. Based on the users input if they are correct a buzzer sounds letting them know if they are wrong a buzzer in a different cadence lets them know. The LCD screen increments when the user gets the sequence right and resets to 0 when they get one wrong displaying the users current place in the game.

* Four RGB LEDs that are coded to append a sequence until the user is wrong
* Each RGB LED is a different color
* LED COLORS(red, green, blue, and purple) Purple shows the best difference
* Buzzer is coded to play a tune based on if the user is wrong or right
* LCD screen coded to keep score of the user
* LCD coded to say game over or start game

## Photos

### System Photo
https://github.com/ACOwens43/ECE-1000-Simon-Says-Game/blob/main/Photos/IMG_4921.JPG

## Who are we

* Asher Owens - Electrical Engineering Major - Coder and RGB LED and Button Circuit builder
* Hayden Hobgood -Computer Engineering Major - Coder and LCD Screen and Buzzer builder

## Repo Guide
* Design Files - Code for whole System
* Documentation - Project Reports
* Photos and Videos
* Simulated Files - All the simulations used to create the game
