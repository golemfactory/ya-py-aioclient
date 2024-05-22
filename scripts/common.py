from pathlib import Path

ROOT_DIR = Path(__file__).parent / '..'
BUILD_DIR = ROOT_DIR / 'build'
TEMPLATE_DIR = ROOT_DIR / 'templates'
SPEC_DIR = ROOT_DIR / 'ya-client' / 'specs'
SPEC_ROOT_FILE_PATH = TEMPLATE_DIR / 'spec-root.json'
SPEC_NAMES = (
    'activity-api',
    'market-api',
    'net-api-v2',
    'payment-api',
)
SPEC_FINAL_FILE_PATH = BUILD_DIR / 'golem-node-api.json'
HTTP_METHODS = ['get', 'put', 'post', 'delete', 'options', 'head', 'patch', 'trace']
