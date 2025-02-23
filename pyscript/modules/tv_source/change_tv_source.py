import sys

if "/config/pyscript/modules/samsungTVlegacy" not in sys.path:
    sys.path.append("/config/pyscript/modules/samsungTVlegacy")

import samsungTVlegacy

@service
def mode_1() -> None:

    config = {
        "name": "HA_TV_Source",
        "description": "TV_Source",
        "id": "",
        "host": "xxx.xxx.x.xxx", #enter TV ip address
        "method": "legacy",
        "port": 55000,
        "timeout": 0
    }

    keylist = ["KEY_TV", "KEY_SOURCE", "KEY_RIGHT", "KEY_ENTER"]

    with samsungTVlegacy.Remote(config) as remote:
         for key in keylist:
           remote.control(key)


@service
def mode_2() -> None:

    config = {
        "name": "HA_TV_Source",
        "description": "TV_Source",
        "id": "",
        "host": "xxx.xxx.x.xxx", #enter TV ip address
        "method": "legacy",
        "port": 55000,
        "timeout": 0
    }

    keylist = ["KEY_TV", "KEY_SOURCE", "KEY_RIGHT", "KEY_RIGHT", "KEY_ENTER"]

    with samsungTVlegacy.Remote(config) as remote:
         for key in keylist:
           remote.control(key)
           
@service
def mode_3() -> None:

    config = {
        "name": "HA_TV_Source",
        "description": "TV_Source",
        "id": "",
        "host": "xxx.xxx.x.xxx", #enter TV ip address
        "method": "legacy",
        "port": 55000,
        "timeout": 0
    }

    keylist = ["KEY_TV", "KEY_SOURCE", "KEY_RIGHT", "KEY_RIGHT", "KEY_RIGHT", "KEY_RIGHT", "KEY_ENTER"]

    with samsungTVlegacy.Remote(config) as remote:
         for key in keylist:
           remote.control(key)
