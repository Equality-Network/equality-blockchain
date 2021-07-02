from typing import KeysView, Generator

SERVICES_FOR_GROUP = {
    "all": "equality_harvester equality_timelord_launcher equality_timelord equality_farmer equality_full_node equality_wallet".split(),
    "node": "equality_full_node".split(),
    "harvester": "equality_harvester".split(),
    "farmer": "equality_harvester equality_farmer equality_full_node equality_wallet".split(),
    "farmer-no-wallet": "equality_harvester equality_farmer equality_full_node".split(),
    "farmer-only": "equality_farmer".split(),
    "timelord": "equality_timelord_launcher equality_timelord equality_full_node".split(),
    "timelord-only": "equality_timelord".split(),
    "timelord-launcher-only": "equality_timelord_launcher".split(),
    "wallet": "equality_wallet equality_full_node".split(),
    "wallet-only": "equality_wallet".split(),
    "introducer": "equality_introducer".split(),
    "simulator": "equality_full_node_simulator".split(),
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
