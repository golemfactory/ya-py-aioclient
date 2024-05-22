import os

from scripts.common import SPEC_FINAL_FILE_PATH, TEMPLATE_DIR


def main():
    os.system(
        f'openapi-python-client update --path {SPEC_FINAL_FILE_PATH} --meta none --custom-template-path {TEMPLATE_DIR}'
    )


if __name__ == '__main__':
    main()
