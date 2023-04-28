#Código que gera arquivo CSV das suas partidas de Dota 2

import requests
import csv

# Para analisar seus dados coloque seu acount_id do dota2
account_id = 98459081

# Pega os dados pelo api do opendota
url = f'https://api.opendota.com/api/players/{account_id}/matches'
response = requests.get(url)
data = response.json()
list_heroes = [None, 'Anti-Mage', 'Axe', 'Bane', 'Bloodseeker', 'Crystal Maiden', 'Drow Ranger', 'Earthshaker', 'Juggernaut', 'Mirana', 'Morphling', 'Shadow Fiend', 'Phantom Lancer', 'Puck', 'Pudge', 'Razor', 'Sand King', 'Storm Spirit', 'Sven', 'Tiny', 'Vengeful Spirit', 'Windranger', 'Zeus', 'Kunkka','Unkwon', 'Lina', 'Lion', 'Shadow Shaman', 'Slardar', 'Tidehunter', 'Witch Doctor', 'Lich', 'Riki', 'Enigma', 'Tinker', 'Sniper', 'Necrophos', 'Warlock', 'Beastmaster', 'Queen of Pain', 'Venomancer', 'Faceless Void', 'Wraith King', 'Death Prophet', 'Phantom Assassin', 'Pugna', 'Templar Assassin', 'Viper', 'Luna', 'Dragon Knight', 'Dazzle', 'Clockwerk', 'Leshrac', "Nature's Prophet", 'Lifestealer', 'Dark Seer', 'Clinkz', 'Omniknight', 'Enchantress', 'Huskar', 'Night Stalker', 'Broodmother', 'Bounty Hunter', 'Weaver', 'Jakiro', 'Batrider', 'Chen', 'Spectre', 'Ancient Apparition', 'Doom', 'Ursa', 'Spirit Breaker', 'Gyrocopter', 'Alchemist', 'Invoker', 'Silencer', 'Outworld Destroyer', 'Lycan', 'Brewmaster', 'Shadow Demon', 'Lone Druid', 'Chaos Knight', 'Meepo', 'Treant Protector', 'Ogre Magi', 'Undying', 'Rubick', 'Disruptor', 'Nyx Assassin', 'Naga Siren', 'Keeper of the Light', 'Io', 'Visage', 'Slark', 'Medusa', 'Troll Warlord', 'Centaur Warrunner', 'Magnus', 'Timbersaw', 'Bristleback', 'Tusk', 'Skywrath Mage', 'Abaddon', 'Elder Titan', 'Legion Commander', 'Techies', 'Ember Spirit', 'Earth Spirit', 'Underlord', 'Terrorblade', 'Phoenix', 'Oracle', 'Winter Wyvern', 'Arc Warden', 'Monkey King', 'Dark Willow', 'Pangolier', 'Grimstroke', 'Hoodwink', 'Void Spirit', 'Snapfire', 'Mars', 'Dawnbreaker', 'Marci', 'Primal Beast', 'Muerta']

# atributos da 'tabela' que vai ser gerada no df do pandas
header = ['Match ID', 'Hero', 'Kills', 'Deaths', 'Assists','KDA', 'Duration', 'Result']

# Escreve um arquivo csv com uma linha para cada partida com os respectivos atributos e valores
try:
    with open('matches2.csv','w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)

        for match in data:
            if match['hero_id'] <= 125:
                match_id = match['match_id']
                hero = match['hero_id']
                hero_name = list_heroes[hero]
                kills = match['kills']
                deaths = match['deaths']
                assists = match['assists']
                kda = (kills + assists) / max(1, deaths)
                duration = match['duration']/60
                result = "Win" if match['radiant_win'] == (match['player_slot'] < 128) else "Loss"

                row = [match_id, hero_name, kills, deaths, assists, kda, duration, result]
                writer.writerow(row)

    print('Arquivo gerado com sucesso')
except:
    print('Erro ao gerar arquivo')