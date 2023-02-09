from dataclasses import dataclass

# https://docs.python.org/3/library/dataclasses.html
@dataclass
class RunConfig:
    """Class to hold the instrument configuration."""
    IPTS: str
    runNumber: str
    maskFileName: str
    maskFileDirectory: str
    gsasFileDirectory: str
    calibrationState: str

    # if we need specific getter and setter methods, we can use the @property decorator
    # https://docs.python.org/3/library/functions.html#property
    #
    # @property
    # def key(self) -> str:
    #     return self._key

    # @name.setter
    # def key(self, v: str) -> None:
    #     self._key = v