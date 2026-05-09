import os
import json


def build_runways(source_directory, output_file):
    result = {}
    for filename in sorted(os.listdir(source_directory)):
        if not filename.endswith('.json'):
            continue
        file_path = os.path.join(source_directory, filename)
        airport_icao = os.path.splitext(filename)[0]
        with open(file_path, 'r') as infile:
            result[airport_icao] = json.load(infile)
    with open(output_file, 'w') as outfile:
        json.dump(result, outfile, indent=2)


def main():
    source_directory = '.data/runways'
    output_file = 'runways.json'
    print(f'Building {output_file} from {source_directory}')
    build_runways(source_directory, output_file)
    print(f'{output_file} built successfully.')


if __name__ == '__main__':
    main()
