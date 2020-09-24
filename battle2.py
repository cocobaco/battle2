# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 07:40:19 2018

@author: roppon
"""

import sys
#import os
import random
import time

import params

MAX_HEALTH = params.MAX_HEALTH
DMG_RANGES = params.DMG_RANGES


class Character:
    def __init__(self, name, starting_health):
        self.name = name
        self.health = starting_health

    def __str__(self):
        if self.health > 0:
            return "%s (%i health)" % (self.name, self.health)
        else:
            return "%s (DEAD)" % self.name

    def take_damage(self, dmg):
        self.health = max(0, self.health - dmg)

    def get_boost(self, boost):
        self.health = min(MAX_HEALTH, self.health + boost)

    def move(self, other, ai=False):
        attack_stmt = 'Choose move: ([h]eal, [t]ackle, [p]unch, [k]ick, [q] quit'
        if not ai:
            move = str.lower(input(attack_stmt + '> '))
        else:
            move = random.choice(['h', 't', 'p', 'k'])

        if move in ['heal', 'h']:
            print(self.name + ' heals...')
            time.sleep(1)
#            self.health = min(100, self.health + random.randint(1, 15))
            amount = random.randint(DMG_RANGES['heal'][0], DMG_RANGES['heal'][1])
            print('health boost:', amount)
            self.get_boost(amount)
            print(str(self))
            print(str(other))
        elif move in ['tackle', 't']:
            print(self.name + ' tackles...')
            time.sleep(1)
            amount = random.choice(DMG_RANGES['tackle'])
            print('damage:', amount)
#            other.health = max(0, other.health - random.choice([0, 5, 30]))
            other.take_damage(amount)
            print(str(self))
            print(str(other))
        elif move in ['punch', 'p']:
            print(self.name + ' punches...')
            time.sleep(1)
            amount = random.randint(DMG_RANGES['punch'][0], DMG_RANGES['punch'][1])
            print('damage:', amount)
#            other.health = max(0, other.health - random.randint(6, 17))
            other.take_damage(amount)
            print(str(self))
            print(str(other))
        elif move in ['kick', 'k']:
            print(self.name + ' kicks...')
            time.sleep(1)
            amount = random.randint(DMG_RANGES['kick'][0], DMG_RANGES['kick'][1])
            print('damage:', amount)
#            other.health = max(0, other.health - random.randint(3, 19))
            other.take_damage(amount)
            print(str(self))
            print(str(other))
        elif move == 'q':
            sys.exit()
#            os._exit(0)
#            quit()
        else:
            print('invalid move. try aagin.')
            self.move(other, ai)


def battle(player, enemy):
    print('{} [{}] vs {} [{}]'.format(player.name, player.health,
          enemy.name, enemy.health))

    turn = random.randint(1, 2)
    if turn == 1:
        player_turn, enemy_turn = True, False
        print('{} will go first'.format(player.name))
    else:
        player_turn, enemy_turn = False, True
        print('{} will go first'.format(enemy.name))

    while (player.health > 0 and enemy.health > 0):
        if player_turn:
            print('*' * 50)
            print('{}\'s turn'.format(player.name))
            player.move(enemy, ai=False)
            if enemy.health <= 0:
                break
        else:
            print('*' * 50)
            print('{}\'s turn'.format(enemy.name))
            enemy.move(player, ai=True)
            if player.health <= 0:
                break
        player_turn, enemy_turn = enemy_turn, player_turn

    if player.health > 0:
        print('{} wins'.format(player.name))
    if enemy.health > 0:
        print('{} wins'.format(enemy.name))


def main():
    print('Welcome to Battle 2!')

    while True:
        player_health = MAX_HEALTH
        enemy_health = MAX_HEALTH
        zaber = Character('Zaber', player_health)
        golem = Character('Golem', enemy_health)
        battle(zaber, golem)

        play_again = input("again? [y or n]: ")
        if play_again.lower() == 'y':
            #pass
            continue
        else:
            break


if __name__ == '__main__':
    main()
