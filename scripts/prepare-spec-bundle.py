import json
import os
from pathlib import Path
from typing import Dict

from scripts.common import (
    BUILD_DIR,
    SPEC_DIR,
    SPEC_ROOT_FILE_PATH,
    SPEC_NAMES,
    HTTP_METHODS,
    SPEC_FINAL_FILE_PATH,
)


def get_spec_file_path(dir: Path, spec_name: str, suffix: str) -> Path:
    return (dir / spec_name).with_suffix(suffix).resolve()


def prepare_source_specs():
    os.system(
        'npx @redocly/cli bundle {spec_files} --output {output} --ext json'.format(
            spec_files=' '.join(
                str(get_spec_file_path(SPEC_DIR, spec_name, '.yaml')) for spec_name in SPEC_NAMES
            ),
            output=BUILD_DIR.resolve(),
        )
    )


def transform_tags(spec_dict: Dict, spec_name: str) -> None:
    tag_name = spec_name
    spec_dict['tags'] = [
        {'name': tag_name, 'description': spec_dict['info']['description'].strip()}
    ]

    for path in spec_dict['paths'].values():
        for method_name, method in path.items():
            if method_name.lower() not in HTTP_METHODS:
                continue

            method['tags'] = [tag_name]


def transform_paths(spec_dict: Dict) -> None:
    base_url = spec_dict['servers'].pop()['url']
    spec_paths = spec_dict['paths']
    original_paths = list(spec_paths.keys())

    for original_path in original_paths:
        spec_paths[f'{base_url}{original_path}'] = spec_paths.pop(original_path)


def join_build_specs():
    os.system(
        'npx @redocly/cli join {root_spec_file} {spec_files} --output {output}.json'.format(
            root_spec_file=SPEC_ROOT_FILE_PATH.resolve(),
            spec_files=' '.join(
                str(get_spec_file_path(BUILD_DIR, spec_name, '.json')) for spec_name in SPEC_NAMES
            ),
            output=SPEC_FINAL_FILE_PATH.with_suffix(''),
        )
    )


def load_spec_dict(spec_file_path: Path) -> Dict:
    with spec_file_path.open('r') as spec_file:
        return json.load(spec_file)


def save_spec_dict(spec_file_path: Path, spec_dict: Dict) -> None:
    with spec_file_path.open('w') as spec_file:
        json.dump(spec_dict, spec_file, indent=4)


def main():
    prepare_source_specs()

    for spec_name in SPEC_NAMES:
        spec_file_path = get_spec_file_path(BUILD_DIR, spec_name, '.json')
        spec_dict = load_spec_dict(spec_file_path)

        transform_tags(spec_dict, spec_name)
        transform_paths(spec_dict)

        save_spec_dict(spec_file_path, spec_dict)

    join_build_specs()


if __name__ == '__main__':
    main()
