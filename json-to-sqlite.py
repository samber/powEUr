
import os
import json
from datetime import datetime, timedelta

import sqlite3

start = datetime(2020, 1, 1).replace(hour=0, minute=0, second=0, microsecond=0)
end = datetime(2024, 1, 1).replace(hour=0, minute=0, second=0, microsecond=0)

# countries = [x[1] for x in os.walk("./data/generation")][0]

countries = {
    'AT': 'austria',
    'BE': 'belgium',
    'BG': 'bulgaria',
    'CH': 'switzerland',
    'CY': 'cyprus',
    'CZ': 'czech_republic',
    'DE': 'germany',
    'DK': 'denmark',
    'EE': 'estonia',
    'ES': 'spain',
    'FI': 'finland',
    'FR': 'france',
    'GB': 'united_kingdom',
    'GR': 'greece',
    'HR': 'croatia',
    'HU': 'hungary',
    'IE': 'ireland',
    'IT': 'italy',
    'LT': 'lithuania',
    'LU': 'luxembourg',
    'LV': 'latvia',
    'NL': 'netherlands',
    'NO': 'norway',
    'PL': 'poland',
    'PT': 'portugal',
    'RO': 'romania',
    'RS': 'serbia',
    'SE': 'sweden',
    'SI': 'slovenia',
    'SK': 'slovakia',
}

print("COUNTRIES:", countries)
print()

# date = start
# energies = {}

# while date < end:
#     for country in countries:
#         filename = date.strftime("%Y-%m-%d") + '.json'
#         path = './data/generation/' + country + '/' + filename
#         try:
#             with open(path, 'r') as f:
#                 data = json.load(f)
#                 for timestamp in data:
#                     for energy in data[timestamp]:
#                         if energy[0] != '(':
#                             if energy not in energies:
#                                 energies[energy] = 1
#                             else:
#                                 energies[energy] += 1

#         except FileNotFoundError:
#             pass

#     date += timedelta(days=1)

# for energy in energies:
#     energies[energy] = energy.lower()\
#         .replace(' ', '_')\
#         .replace('/', '_')\
#         .replace('-', '_')

energies = {
    'Biomass': 'biomass_generation_mwh',
    'Fossil Brown coal/Lignite': 'fossil_brown_coal_lignite_generation_mwh',
    'Fossil Gas': 'fossil_gas_generation_mwh',
    'Fossil Hard coal': 'fossil_hard_coal_generation_mwh',
    'Fossil Oil': 'fossil_oil_generation_mwh',
    'Hydro Pumped Storage': 'hydro_pumped_storage_generation_mwh',
    'Hydro Run-of-river and poundage': 'hydro_run_of_river_and_poundage_generation_mwh',
    'Hydro Water Reservoir': 'hydro_water_reservoir_generation_mwh',
    'Nuclear': 'nuclear_generation_mwh',
    'Other': 'other_generation_mwh',
    'Other renewable': 'other_renewable_generation_mwh',
    'Solar': 'solar_generation_mwh',
    'Wind Onshore': 'wind_onshore_generation_mwh',
    'Fossil Coal-derived gas': 'fossil_coal_derived_gas_generation_mwh',
    'Waste': 'waste_generation_mwh',
    'Wind Offshore': 'wind_offshore_generation_mwh',
    'Fossil Oil shale': 'fossil_oil_shale_generation_mwh',
    'Fossil Peat': 'fossil_peat_generation_mwh',
    'Geothermal': 'geothermal_generation_mwh',
    'Marine': 'marine_generation_mwh',
}

print("ENERGIES:", energies)
print()

date = start
insertion = []

while date < end:
    for country in countries:
        filename = date.strftime("%Y-%m-%d") + '.json'
        path = './data/generation/' + country + '/' + filename
        try:
            with open(path, 'r') as f:
                data = json.load(f)
                for timestamp in data:
                    point = {
                        'timestamp': datetime.fromtimestamp(int(timestamp) / 1000),
                        'country': countries[country],
                    }

                    for energy in energies:
                        if energy in data[timestamp]:
                            point[energies[energy]] = data[timestamp][energy]
                        else:
                            point[energies[energy]] = 0

                    insertion.append(point)

        except FileNotFoundError:
            pass

    date += timedelta(days=1)

# print("INSERTION:", insertion[0])

with sqlite3.connect('./data/generation.db') as conn:
    query = """CREATE TABLE IF NOT EXISTS power_generation (
        id INTEGER PRIMARY KEY,
        timestamp INTEGER NOT NULL,
        country text NOT NULL,
        biomass_generation_mwh INTEGER DEFAULT 0,
        fossil_brown_coal_lignite_generation_mwh INTEGER DEFAULT 0,
        fossil_gas_generation_mwh INTEGER DEFAULT 0,
        fossil_hard_coal_generation_mwh INTEGER DEFAULT 0,
        fossil_oil_generation_mwh INTEGER DEFAULT 0,
        hydro_pumped_storage_generation_mwh INTEGER DEFAULT 0,
        hydro_run_of_river_and_poundage_generation_mwh INTEGER DEFAULT 0,
        hydro_water_reservoir_generation_mwh INTEGER DEFAULT 0,
        nuclear_generation_mwh INTEGER DEFAULT 0,
        other_generation_mwh INTEGER DEFAULT 0,
        other_renewable_generation_mwh INTEGER DEFAULT 0,
        solar_generation_mwh INTEGER DEFAULT 0,
        wind_onshore_generation INTEGER DEFAULT 0,
        fossil_coal_derived_gas_generation_mwh INTEGER DEFAULT 0,
        waste_generation_mwh INTEGER DEFAULT 0,
        wind_offshore_generation INTEGER DEFAULT 0,
        fossil_oil_shale_generation_mwh INTEGER DEFAULT 0,
        fossil_peat_generation_mwh INTEGER DEFAULT 0,
        geothermal_generation_mwh INTEGER DEFAULT 0,
        marine_generation_mwh INTEGER DEFAULT 0
    );"""
    cursor = conn.cursor()
    cursor.execute(query)

    for point in insertion:
        query = """INSERT INTO power_generation (
                timestamp,
                country,
                biomass_generation_mwh,
                fossil_brown_coal_lignite_generation_mwh,
                fossil_gas_generation_mwh, 
                fossil_hard_coal_generation_mwh,
                fossil_oil_generation_mwh,
                hydro_pumped_storage_generation_mwh,
                hydro_run_of_river_and_poundage_generation_mwh,
                hydro_water_reservoir_generation_mwh, 
                nuclear_generation_mwh,
                other_generation_mwh,
                other_renewable_generation_mwh,
                solar_generation_mwh,
                wind_onshore_generation
            ) VALUES (
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?
            );"""
        cursor.execute(query, (
            point['timestamp'].timestamp(),
            point['country'],
            point['biomass_generation_mwh'],
            point['fossil_brown_coal_lignite_generation_mwh'],
            point['fossil_gas_generation_mwh'],
            point['fossil_hard_coal_generation_mwh'],
            point['fossil_oil_generation_mwh'],
            point['hydro_pumped_storage_generation_mwh'],
            point['hydro_run_of_river_and_poundage_generation_mwh'],
            point['hydro_water_reservoir_generation_mwh'],
            point['nuclear_generation_mwh'],
            point['other_generation_mwh'],
            point['other_renewable_generation_mwh'],
            point['solar_generation_mwh'],
            point['wind_onshore_generation_mwh'],
        ))

    conn.commit()
