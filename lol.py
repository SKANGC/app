import random
import time


def get_complex_seed():
    return (
        time.time(),  # 秒级时间戳
        time.time_ns(),  # 纳秒级时间戳
        time.perf_counter(),  # 性能计数器，提供更高的分辨率
        time.process_time(),  # 进程执行的时间
    )


def load_data_from_file(file_path):
    with open(file_path, 'r', encoding='GBK') as file:
        return [line.strip() for line in file.readlines()]


def generate_random_combination(heroes, runes, summoner_spells, zhuangbis, xies, num_of_players):
    combinations = []
    used_heroes = set()

    for _ in range(num_of_players):
        while True:
            hero = random.choice(heroes)
            if hero not in used_heroes:
                used_heroes.add(hero)
                break

        rune = random.choice(runes)
        summoner_spell_1 = random.choice(summoner_spells)
        summoner_spell_2 = random.choice(summoner_spells)
        while summoner_spell_1 == summoner_spell_2:
            summoner_spell_2 = random.choice(summoner_spells)

        # 随机选择装备，默认为1
        equipments = random.sample(zhuangbis, 1)
        hero_xie = random.choice(xies)
        equipments.append(hero_xie)

        combinations.append((hero, rune, summoner_spell_1, summoner_spell_2, equipments))

    return combinations


def main():
    seed = get_complex_seed()
    random.seed(seed)
    num_of_players = int(input("请输入玩家数量："))
    heroes = load_data_from_file('heroes.txt')
    runes = load_data_from_file('runes.txt')
    summoner_spells = load_data_from_file('summoner_spells.txt')
    zhuangbis = load_data_from_file('zhuangbei.txt')
    xie_data = load_data_from_file('xie.txt')

    random_combinations = generate_random_combination(heroes, runes, summoner_spells, zhuangbis, xie_data, num_of_players)

    for i, (hero, rune, summoner_spell_1, summoner_spell_2, equipments) in enumerate(random_combinations):
        print(f"玩家 {i+1}:")
        print(f"  - 英雄: {hero}")
        print(f"  - 符文: {rune}")
        print(f"  - 召唤师技能: {summoner_spell_1} 和 {summoner_spell_2}")
        print(f"  - 装备: {', '.join(equipments)}")
        print("-" * 40)


if __name__ == "__main__":
    main()