import logging
from typing import List, Tuple
from pathlib import Path

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%H:%M:%S')

class NumberProcessorBase:
    #Base class that handles file operations
    def __init__(self, input_path: str):
        self.input_path = Path(input_path)

    def file_validation (self) -> bool:
        if not self.input_path.exists():
