# -*- encoding=utf8 -*-
__author__ = "hulu"

from airtest.core.api import *
from poco.drivers.ios import iosPoco
auto_setup(__file__)
connect_device("ios:///127.0.0.1:8100")
poco = iosPoco()
poco('0128105536').click()
poco('美食').click()