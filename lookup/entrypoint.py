import logging
logger = logging.getLogger(__name__)

import os
from yaml import safe_load

HIERARCHY = [
  "env/{env}.yaml",
  "common.yaml"
]

DATA_DIRECTORY_NAME = 'data'

def search(key: str, args: dict):

  logger.info(f"Searching for {key} with {args}")

  compiled_paths = [ compile_filename(path, args) for path in HIERARCHY ]
  search_paths = [ os.path.join(DATA_DIRECTORY_NAME, path) for path in compiled_paths if path ]
  search_data = [ read_yaml_file(path) for path in search_paths if os.path.isfile(path) ]

  logger.info(f"Search paths: {search_paths}")

  for data in search_data:

    if key in data:
      return data.get(key)

  return None


def compile_filename(format: str, args) -> str:

  try:
    formatted = format.format(**args)
    logger.info(f"Searching: {formatted}")
    return formatted
  except Exception as e:
    logger.exception(e)
    return None


def read_yaml_file(path: str) -> dict:

  with open(path, 'r') as f:
    return safe_load(f)
