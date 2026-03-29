from dataclasses import dataclass
from pathlib import Path
@dataclass(frozen=True)
class DataIngestionConfig:
    raw_data_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path 

@dataclass(frozen=True)
class DataValidationConfig:
    raw_data_dir: Path
    STATUS_FILE: Path
    ALL_REQUIRED_FILES: list[str]
