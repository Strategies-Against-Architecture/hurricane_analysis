# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville',
        'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah',
        'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch',
        'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew',
        'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September',
        'September', 'September', 'September', 'September', 'September', 'October',
        'September', 'August', 'September', 'September', 'August', 'August',
        'September', 'September', 'August', 'October', 'September', 'September',
        'July', 'August', 'September', 'October', 'August', 'September', 'October',
        'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967,
        1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005,
        2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160,
                    160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160,
                    175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'],
                ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'],
                ['The Bahamas', 'Northeastern United States'],
                ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'],
                ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'],
                ['Jamaica', 'Yucatn Peninsula'],
                ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'],
                ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'],
                ['Bermuda', 'New England', 'Atlantic Canada'],
                ['Lesser Antilles', 'Central America'],
                ['Texas', 'Louisiana', 'Midwestern United States'],
                ['Central America'],
                ['The Caribbean', 'Mexico', 'Texas'],
                ['Cuba', 'United States Gulf Coast'],
                ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'],
                ['Mexico'],
                ['The Caribbean', 'United States East coast'],
                ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'],
                ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'],
                ['The Caribbean', 'United States East Coast'],
                ['The Bahamas', 'Florida', 'United States Gulf Coast'],
                ['Central America', 'Yucatn Peninsula', 'South Florida'],
                ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'],
                ['The Caribbean', 'Venezuela', 'United States Gulf Coast'],
                ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'],
                ['Bahamas', 'United States Gulf Coast'],
                ['Cuba', 'United States Gulf Coast'],
                ['Greater Antilles', 'Central America', 'Florida'],
                ['The Caribbean', 'Central America'],
                ['Nicaragua', 'Honduras'],
                ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'],
                ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'],
                ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'],
                ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M',
        'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B',
        '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B',
        '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B',
        '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,
        107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
updated_damages = []
def update_damages(dmg_list):
    conversion = {"M": 1000000,
                  "B": 1000000000}

    for item in dmg_list:
        if item == 'Damages not recorded':
            updated_damages.append(item)
        else:
            updated_item = float(item[:-1]) * conversion[item[-1]]
            updated_damages.append(updated_item)

    return updated_damages

update_damages(damages)
#print(updated_damages)

# write your construct hurricane dictionary function here:
hurricanes = {}
def hurricane_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    for i in range(len(names)-1):
        hurricane = {
            'Name': names[i],
            'Month': months[i],
            'Year': years[i],
            'Max Sustained Wind': max_sustained_winds[i],
            'Areas Affected': areas_affected[i],
            'Damage': damages[i],
            'Death': deaths[i]
            }
        hurricanes[names[i]] = hurricane

    return hurricanes

hurricane_dict(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
print(hurricanes)

# write your construct hurricane by year dictionary function here:
hurricanes_by_year = {}
def hurricanes_by_year_constructor(hurricanes):
    for key in hurricanes.keys():
        current_year = hurricanes[key]['Year']
        current_hurricane = hurricanes[key]

        if current_year not in hurricanes_by_year.keys():
            hurricanes_by_year[current_year] = [current_hurricane]
        else:
            hurricanes_by_year[current_year].append(current_hurricane)

hurricanes_by_year_constructor(hurricanes)
#print(hurricanes_by_year)

# write your count affected areas function here:
affected_areas_count = {}
def count_affected_areas(list):
    areas_list = []
    count = 0
    for areas in areas_affected:
        for area in areas:
            if area not in areas_list:
                areas_list.append(area)

    for area in areas_list:
        for hurricane in hurricanes.keys():
            if area in hurricanes[hurricane]['Areas Affected']:
                count += 1
        affected_areas_count[area] = count
        count = 0
    return affected_areas_count

print(count_affected_areas(hurricanes))


# write your find most affected area function here:

def most_affected_area_calculator(list):
    areas_list = []
    count = 0
    max_area = ''
    max_area_count = 0
    for areas in areas_affected:
        for area in areas:
            if area not in areas_list:
                areas_list.append(area)
    for area in areas_list:
        for hurricane in hurricanes.keys():
            if area in hurricanes[hurricane]['Areas Affected']:
                count += 1
        if count > max_area_count:
            max_area = area
            max_area_count = count
        count = 0

    return (max_area, max_area_count)

print(most_affected_area_calculator(hurricanes))


# write your greatest number of deaths function here:
def great_number_of_deaths_calculator(list):
    max_hurricane = ''
    max_deaths_count = 0
    for hurricane in hurricanes.keys():
        if hurricanes[hurricane]['Death'] > max_deaths_count:
            max_hurricane = hurricane
            max_deaths_count = hurricanes[hurricane]['Death']

    return(max_hurricane, max_deaths_count)

print(great_number_of_deaths_calculator(hurricanes))

# write your catgeorize by mortality function here:
hurricanes_by_mortality = {}
def categorize_by_mortality(list):
    mortality_scale = {0: 0,
                       1: 100,
                       2: 500,
                       3: 1000,
                       4: 10000}

    for rate in mortality_scale:
        hurricanes_by_mortality.update({rate: []})

    for hurricane in hurricanes.keys():
        if hurricanes[hurricane]['Death'] >= 0 and hurricanes[hurricane]['Death'] < 100:
            hurricanes_by_mortality[0].append(hurricane)
        elif hurricanes[hurricane]['Death'] >= 100 and hurricanes[hurricane]['Death'] < 500:
            hurricanes_by_mortality[1].append(hurricane)
        elif hurricanes[hurricane]['Death'] >= 500 and hurricanes[hurricane]['Death'] < 1000:
            hurricanes_by_mortality[2].append(hurricane)
        elif hurricanes[hurricane]['Death'] >= 1000 and hurricanes[hurricane]['Death'] < 10000:
            hurricanes_by_mortality[3].append(hurricane)
        else:
            hurricanes_by_mortality[4].append(hurricane)

    return hurricanes_by_mortality

categorize_by_mortality(hurricanes)
print(hurricanes_by_mortality)


# write your greatest damage function here:
def greatest_damage_calculator(list):
    max_damage_name = ''
    max_damage = 0

    for hurricane in hurricanes.keys():
        try:
            if int(hurricanes[hurricane]['Damage']) > max_damage:
                max_damage_name = hurricane
                max_damage = hurricanes[hurricane]['Damage']
        except ValueError:
            continue
    return(max_damage_name, max_damage)

print(greatest_damage_calculator(hurricanes))


# write your catgeorize by damage function here:
hurricanes_by_dmg = {}
def categorize_by_damage(list):
    damage_scale = {0: 0,
                    1: 100000000,
                    2: 1000000000,
                    3: 10000000000,
                    4: 50000000000}

    hurricanes_by_dmg.update(dict((k, []) for k in damage_scale.keys()))

    for hurricane in hurricanes.keys():
        if hurricanes[hurricane]['Damage'] == 'Damages not recorded':
            hurricanes_by_dmg[0].append(hurricane)
        elif hurricanes[hurricane]['Damage'] >= 0 and hurricanes[hurricane]['Death'] < 100000000:
            hurricanes_by_dmg[0].append(hurricane)
        elif hurricanes[hurricane]['Damage'] >= 100000000 and hurricanes[hurricane]['Death'] < 1000000000:
            hurricanes_by_dmg[1].append(hurricane)
        elif hurricanes[hurricane]['Damage'] >= 1000000000 and hurricanes[hurricane]['Death'] < 10000000000:
            hurricanes_by_dmg[2].append(hurricane)
        elif hurricanes[hurricane]['Death'] >= 10000000000 and hurricanes[hurricane]['Death'] < 50000000000:
            hurricanes_by_dmg[3].append(hurricane)
        else:
            hurricanes_by_dmg[4].append(hurricane)

    return hurricanes_by_dmg

categorize_by_damage(hurricanes)
print(hurricanes_by_dmg)