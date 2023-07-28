import time
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 50
        self.defense_power = 30
        self.inventory = []

    def take_damage(self, damage):
        self.health = max(0, self.health - damage)

    def attack(self, enemy):
        damage = random.randint(self.attack_power - 10, self.attack_power + 10)
        enemy.take_damage(damage)
        return damage

class Enemy:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def take_damage(self, damage):
        self.health = max(0, self.health - damage)

    def attack(self, player):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        player.take_damage(damage)
        return damage

class Tomb:
    def __init__(self, name):
        self.name = name
        self.enemies = []
        self.loot = []

def delay_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def show_status(player):
    print(f"\n{name}生命值：{player.health}  攻击力：{player.attack_power}  防御力：{player.defense_power}")

def explore_tomb(player, tomb):
    delay_print(f"\n{name}进入了{tomb.name}...")
    for enemy in tomb.enemies:
        if player.health <= 0:
            delay_print(f"{name}在{tomb.name}中遭遇了{enemy.name}，但由于生命值过低，无法继续探索。游戏结束。")
            exit()

        delay_print(f"{player.name}遭遇了{enemy.name}！")
        while player.health > 0 and enemy.health > 0:
            player_damage = player.attack(enemy)
            enemy_damage = enemy.attack(player)
            delay_print(f"{player.name}对{enemy.name}造成了{player_damage}点伤害，{enemy.name}还剩余{enemy.health}生命值。")
            delay_print(f"{enemy.name}对{player.name}造成了{enemy_damage}点伤害，{player.name}还剩余{player.health}生命值。")

        if player.health <= 0:
            delay_print(f"{player.name}在{tomb.name}中被{enemy.name}击败，游戏结束。")
            exit()

        delay_print(f"{player.name}击败了{enemy.name}！")

    if tomb.loot:
        player.inventory.extend(tomb.loot)
        delay_print(f"{player.name}找到了一些宝藏：")
        for item in tomb.loot:
            delay_print(f"- {item}")

def play_game():
    player_name = input("请输入你的名字：")
    player = Player(player_name)

    delay_print(f"欢迎来到盗墓笔记游戏，{player_name}！")
    delay_print("你将在这个游戏中探索古墓，战斗怪物，寻找宝藏。")

    tomb1 = Tomb("古墓1")
    tomb1.enemies = [Enemy("僵尸", 80, 40), Enemy("蜘蛛精", 60, 50)]
    tomb1.loot = ["古剑", "黄金"]

    tomb2 = Tomb("古墓2")
    tomb2.enemies = [Enemy("蝙蝠怪", 90, 35), Enemy("石像鬼", 70, 60)]
    tomb2.loot = ["紫瓷器", "银元宝"]

    tombs = [tomb1, tomb2]

    for tomb in tombs:
        show_status(player)
        action = input(f"{player_name}，你要继续前往{tomb.name}吗？(是/否)：").lower()
        if action == "是":
            explore_tomb(player, tomb)
        else:
            delay_print(f"{player_name}结束了游戏。")
            exit()

    delay_print(f"{player_name}探索完所有古墓，游戏结束。")

if __name__ == "__main__":
    play_game()
