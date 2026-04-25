import logging
from typing import List, Tuple
from pathlib import Path

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%H:%M:%S')

class IntegerProcessorBase:
    #Base class that handles file operations
    def __init__(self, input_path: str):
        self.input_path = Path(input_path)

    def file_validation (self) -> bool:
        if not self.input_path.exists():
            logging.error(f"Input file {self.input_path} is missing.")
            return False
        return True

class IntegerProcessor(IntegerProcessorBase):
    #Class for the sorting of even and odd numbers
    def __init__(self):
