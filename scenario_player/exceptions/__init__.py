from scenario_player.exceptions.files import CannotImplicitlyChangeFileType
from scenario_player.exceptions.legacy import (
    ChannelError,
    InvalidScenarioVersion,
    MissingNodesConfiguration,
    MultipleTaskDefinitions,
    NodesUnreachableError,
    RESTAPIError,
    RESTAPIStatusMismatchError,
    RESTAPITimeout,
    ScenarioAssertionError,
    ScenarioError,
    ScenarioTxError,
    TokenRegistrationError,
    TransferFailed,
    UnknownTaskTypeError,
)

__all__ = [
    "CannotImplicitlyChangeFileType",
    "ChannelError",
    "InvalidScenarioVersion",
    "MultipleTaskDefinitions",
    "MissingNodesConfiguration",
    "NodesUnreachableError",
    "RESTAPIError",
    "RESTAPIStatusMismatchError",
    "RESTAPITimeout",
    "ScenarioAssertionError",
    "ScenarioError",
    "ScenarioTxError",
    "TokenRegistrationError",
    "TransferFailed",
    "UnknownTaskTypeError",
]
