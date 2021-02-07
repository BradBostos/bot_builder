import random
import time

class delay:
    def __init__(self):
	    print("Hello peasants")

    def fixed(self, fixed_duration): # Waits for a fixed amount of time
        time.sleep(fixed_duration)

    def random(self,random_duration): # Waits for a
        time.sleep(random.uniform(0, random_duration))

    def fixed_random(self, fixed_duration, random_duration):
        time.sleep(fixed_duration)
        time.sleep(random.uniform(0, random_duration))

    def fixed_chance(self, fixed_duration, chance):
        my_rand = random.randint(1,chance)
        if my_rand == 1:
            print("Hit chance")
            time.sleep(fixed_duration)

    def random_chance(self, random_duration, chance):
        my_rand = random.randint(1,chance)
        if my_rand == 1:
            print("Hit chance")
            time.sleep(random.uniform(0, random_duration))

    def fixed_random_chance(self, fixed_duration, random_duration, chance):
        time.sleep(fixed_duration)
        my_rand = random.randint(1,chance)
        if my_rand == 1:
            print("Hit chance")
            time.sleep(random.uniform(0, random_duration))

    def fixed_chance_random_chance(self, fixed_duration, random_duration, chance):
        my_rand = random.randint(1,chance)
        if my_rand == 1:
            print("Hit chance")
            time.sleep(fixed_duration)
            time.sleep(random.uniform(0, random_duration))

    def fcrc(self, fixed_duration, random_duration, chance): # Easier Name
        self.fixed_chance_random_chance(fixed_duration, random_duration, chance)

    def frc(self, fixed_duration, random_duration, chance): # Easier Name
        self.fixed_random_chance(fixed_duration, random_duration, chance)
