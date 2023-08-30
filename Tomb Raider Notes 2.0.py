import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description

def delay_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def explore_tomb(player):
    delay_print(f"欢迎来到《盗墓笔记》游戏，{player.name}！")
    delay_print("你将在这个游戏中探索古墓，解开谜题，寻找宝藏。")

    locations = [
        Location("古墓入口", "一个阴森恐怖的古墓入口。"),
        Location("神秘通道", "昏暗的通道，四周有着奇怪的气氛。"),
        Location("古墓内堂", "古墓内部，充满了古老的气息。"),
    ]

    while player.health > 0:
        print("\n你可以前往以下地点：")
        for index, location in enumerate(locations):
            print(f"{index + 1}. {location.name}")

        choice = input("请选择要前往的地点（输入地点编号）：")
        if choice in ["1", "2", "3"]:
            location = locations[int(choice) - 1]
            delay_print(f"{player.name}前往了{location.name}。")
            delay_print(location.description)
        else:
            delay_print("无效的选择。")

        player.health -= 20
        continue_choice = input("是否继续探索？(是/否): ").strip().lower()
        if continue_choice != "是":
            delay_print(f"谢谢参与《盗墓笔记》游戏！再见。")
            exit()

def main():
    player_name = input("请输入你的名字：")
    player = Player(player_name)

    explore_tomb(player)

if __name__ == "__main__":
    main()
