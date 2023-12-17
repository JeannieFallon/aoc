import sys
import fileinput

from dataclasses import dataclass, field

'''
python 05_2.py input_05.txt
'''

@dataclass
class MapVals:
    dest: int
    src: int
    length: int

@dataclass
class BaseMapping:
    maps: list[MapVals] = field(default_factory=list)

@dataclass
class SeedSoil(BaseMapping):
    category: str = "seed-to-soil"

@dataclass
class SoilFert(BaseMapping):
    category: str = "soil-to-fertilizer"

@dataclass
class FertWater(BaseMapping):
    category: str = "fertilizer-to-water"

@dataclass
class WaterLight(BaseMapping):
    category: str = "water-to-light"

@dataclass
class LightTemp(BaseMapping):
    category: str = "light-to-temperature"

@dataclass
class TempHumid(BaseMapping):
    category: str = "temperature-to-humidity"

@dataclass
class HumidLoc(BaseMapping):
    category: str = "humidity-to-location"

@dataclass
class Almanac:
    seeds: list[int] = field(default_factory=list)
    mappings: list[BaseMapping] = field(default_factory=list)
    categories: list[str] = field(default_factory=list)


def get_mapping(val: int, mapping: list) -> int:
    is_mapped = False
    for _map in mapping.maps:
        #print(f'val: {val}, _map: {_map}')
        if val >= _map.src and val <= _map.src + _map.length:
            val = _map.dest + abs(_map.src - val)
            #print(f'new val: {val}')
            return val

    return val


def get_lowest_location(alm: Almanac) -> int:
    locations = []

    for seed in alm.seeds:
        val = seed
        for mapping in alm.mappings:
            #print(mapping)
            val = get_mapping(val, mapping)
            print(val)
            #locations.append(get_mapping(val, mapping))
            locations.append(val)

    print(locations)
    locations.sort()
    return locations[0]


# FIXME: there's almost certainly a way to do this within the dataclass
def load_almanac() -> Almanac:
    alm = Almanac()

    alm.mappings.append(SeedSoil())
    alm.mappings.append(SoilFert())
    alm.mappings.append(FertWater())
    alm.mappings.append(WaterLight())
    alm.mappings.append(LightTemp())
    alm.mappings.append(TempHumid())
    alm.mappings.append(HumidLoc())

    for mapping in alm.mappings:
        alm.categories.append(mapping.category)

    return alm


def main():
    alm = load_almanac()
    result = 0

    # Need to use readlines() for this one to
    # parse groups of lines as mappings
    filename = sys.argv[1]

    with open(filename, 'r') as f:
        lines = f.readlines()
        len_lines = len(lines)

        # Get seeds from first line
        alm.seeds = [int(seed) for seed in lines[0].split(':')[1].split()]

        # Start at first mapping on third line
        for i in range(2, len_lines):
            line = lines[i]

            # Skip all empty lines
            if line != '\n':
                category = line.split()[0]

                # Match category to mapping category
                for mapping in alm.mappings:
                    if category == mapping.category:
                        curr = mapping

                        # Skip header line
                        i += 1
                        while i < len_lines and lines[i] != '\n':
                            vals = [int(val) for val in lines[i].split()]
                            map_vals = MapVals(vals[0], vals[1], vals[2])
                            curr.maps.append(map_vals)
                            i += 1

                        break

    #print(alm)
    result += get_lowest_location(alm)
    #print(alm)

    # FIXME
    print(result)

    # Demo
    assert result == 35
    '''
    # Final
    assert result == TBD
    '''

    print(f'Success for result: {result}')


if __name__ == "__main__":
    main()
