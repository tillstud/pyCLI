from dataclasses import dataclass


@dataclass
class Config:
    ca_bundle: str

    pycli_message: str
