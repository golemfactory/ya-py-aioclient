from enum import Enum


class DriverStatusPropertyKind(str, Enum):
    CANTSIGN = "CantSign"
    INSUFFICIENTGAS = "InsufficientGas"
    INSUFFICIENTTOKEN = "InsufficientToken"
    INVALIDCHAINID = "InvalidChainId"
    RPCERROR = "RpcError"
    TXSTUCK = "TxStuck"

    def __str__(self) -> str:
        return str(self.value)
