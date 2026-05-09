import os
import json


def compact_arrays(obj, indent=0):
    """Recursively serialise obj, collapsing simple arrays to one line."""
    pad = "  " * indent
    inner_pad = "  " * (indent + 1)

    if isinstance(obj, dict):
        if not obj:
            return "{}"
        lines = []
        for key, value in obj.items():
            lines.append(f'{inner_pad}{json.dumps(key)}: {compact_arrays(value, indent + 1)}')
        return "{\n" + ",\n".join(lines) + "\n" + pad + "}"

    if isinstance(obj, list):
        if not obj:
            return "[]"
        if all(not isinstance(item, (dict, list)) for item in obj):
            return "[" + ", ".join(json.dumps(item) for item in obj) + "]"
        lines = []
        for item in obj:
            lines.append(f'{inner_pad}{compact_arrays(item, indent + 1)}')
        return "[\n" + ",\n".join(lines) + "\n" + pad + "]"

    return json.dumps(obj)


def build_sectors(source_directory, output_file):
    result = {}
    for dirpath, _, filenames in os.walk(source_directory):
        for filename in sorted(filenames):
            if not filename.endswith('.json'):
                continue
            file_path = os.path.join(dirpath, filename)
            key = os.path.splitext(filename)[0]
            with open(file_path, 'r') as infile:
                result[key] = json.load(infile)
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
