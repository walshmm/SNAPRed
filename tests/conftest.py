import os
import unittest.mock as mock

import pytest

# import sys
# sys.path.append('.')
# os.environ['PYTHONPATH'] = './src'
os.environ["env"] = "test"

from mantid.kernel import ConfigService  # noqa: E402
from snapred.meta.Config import (  # noqa: E402
    Config,  # noqa: E402
    Resource,  # noqa: E402
)


def mock_decorator(orig_cls):
    return orig_cls


# PATCH THE DECORATOR HERE
mockSingleton = mock.Mock()
mockSingleton.Singleton = mock_decorator
mock.patch.dict("sys.modules", {"snapred.meta.decorators.Singleton": mockSingleton}).start()

# manually alter the config to point to the test resources
Config._config["instrument"]["home"] = Resource.getPath(Config["instrument.home"])
mantidConfig = config = ConfigService.Instance()
mantidConfig["CheckMantidVersion.OnStartup"] = "0"
mantidConfig["UpdateInstrumentDefinitions.OnStartup"] = "0"
mantidConfig["usagereports.enabled"] = "0"
