from matplotlib import pyplot as plt
import csv

indie_games = 'indie-games-developers.csv'
game_developers = 'video-games-developers.csv'

# Count games per country
country_count = {}

with open(indie_games, 'r') as f:
    datareader = csv.reader(f)
    next(datareader, None)
    for row in datareader:
        if row[3] not in country_count:
            country_count[row[3]] = 1
            continue
        country_count[row[3]] += 1

sorted_country_count = {}
sorted_keys = reversed(sorted(country_count, key=country_count.get))  # [1, 3, 2]

for w in sorted_keys:
    sorted_country_count[w] = country_count[w]

plt.barh(list(sorted_country_count.keys()), sorted_country_count.values())
plt.title('Developers per country')
plt.xlabel('Number of developers')
plt.ylabel('Countries')

plt.grid(b = True, color ='grey', linestyle ='-.', linewidth = 0.5, alpha = 0.2)

plt.show()

print(sorted_country_count.keys())