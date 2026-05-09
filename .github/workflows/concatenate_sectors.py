import os
import json
import re


def compact_arrays(obj):
    """Serialise obj with indentation, then collapse multi-line arrays to one line."""
    raw = json.dumps(obj, indent=2)
    def collapse(match):
        return re.sub(r'\s+', ' ', match.group(0))
    return re.sub(r'\[.*?\]', collapse, raw, flags=re.DOTALL)


def build_sectors(source_directory, output_file):
    result = {}
    for dirpath, _, filenames in os.walk(source_directory):
        for filename in sorted(filenames):
            if not filename.endswith('.json'):
                continue
            file_path = os.path.join(dirpath, filename)
            fir_key = os.path.splitext(filename)[0]
            with open(file_path, 'r') as infile:
                result[fir_key] = json.load(infile)
    with open(output_file, 'w') as outfile:
        outfile.write(compact_arrays(result))


def main():
    source_directory = '.data/sectors'
    output_file = 'sectors.json'
    print(f'Building {output_file} from {source_directory}')
    build_sectors(source_directory, output_file)
    print(f'{output_file} built successfully.')


if __name__ == '__main__':
    main()
