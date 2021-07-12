from typing import Optional, List, Union
from datetime import datetime
from typing_extensions import Literal, Final

class TerminateCommandBody(object):

    def __init__(self) -> None: ...
    def to_dict(self) -> dict: ...


class ErrorMessage(object):
    message: Optional[str]  # readonly: False

    def __init__(self,
        message: Optional[str] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class CreateActivityRequest(object):
    agreement_id: str  # readonly: False
    requestor_pub_key: Optional[str]  # readonly: False

    def __init__(self,
        agreement_id: str,
        requestor_pub_key: Optional[str] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class ActivityState(object):
    state: list  # readonly: False
    reason: Optional[str]  # readonly: False
    error_message: Optional[str]  # readonly: False

    def __init__(self,
        state: list,
        reason: Optional[str] = None,
        error_message: Optional[str] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class SignCommandBody(object):

    def __init__(self) -> None: ...
    def to_dict(self) -> dict: ...


class RuntimeEvent(object):
    batch_id: str  # readonly: False
    index: int  # readonly: False
    timestamp: str  # readonly: False
    kind: RuntimeEventKind  # readonly: False

    def __init__(self,
        batch_id: str,
        index: int,
        timestamp: str,
        kind: RuntimeEventKind
    ) -> None: ...
    def to_dict(self) -> dict: ...


class ExeScriptCommandResult(object):
    index: int  # readonly: False
    event_date: datetime  # readonly: False
    result: Literal["Ok","Error"]  # readonly: False
    stdout: Optional[str]  # readonly: False
    stderr: Optional[str]  # readonly: False
    message: Optional[str]  # readonly: False
    is_batch_finished: Optional[bool]  # readonly: False

    def __init__(self,
        index: int,
        event_date: datetime,
        result: Literal["Ok","Error"],
        stdout: Optional[str] = None,
        stderr: Optional[str] = None,
        message: Optional[str] = None,
        is_batch_finished: Optional[bool] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class CreateActivityResult(object):
    activity_id: str  # readonly: False
    credentials: Credentials  # readonly: False

    def __init__(self,
        activity_id: str,
        credentials: Credentials = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class CommandOutput(object):

    def __init__(self) -> None: ...
    def to_dict(self) -> dict: ...


class RuntimeEventKindFinishedBody(object):
    return_code: int  # readonly: False
    message: Optional[str]  # readonly: False

    def __init__(self,
        return_code: int,
        message: Optional[str] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class ProviderEvent(object):
    event_type: str  # readonly: False
    event_date: datetime  # readonly: False
    activity_id: str  # readonly: False
    agreement_id: str  # readonly: False

    def __init__(self,
        event_type: str,
        event_date: datetime,
        activity_id: str,
        agreement_id: str
    ) -> None: ...
    def to_dict(self) -> dict: ...


class TransferCommandBody(object):
    _from: str  # readonly: False
    to: str  # readonly: False
    _format: Optional[str]  # readonly: False
    depth: Union[float, int]  # readonly: False
    fileset: Optional[list]  # readonly: False

    def __init__(self,
        _from: str,
        to: str,
        _format: Optional[str] = None,
        depth: Union[float, int] = None,
        fileset: Optional[list] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class RunCommandBody(object):
    entry_point: str  # readonly: False
    args: Optional[list]  # readonly: False

    def __init__(self,
        entry_point: str,
        args: Optional[list] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class RuntimeEventKind(object):

    def __init__(self) -> None: ...
    def to_dict(self) -> dict: ...


class ExeScriptCommandState(object):
    batch_id: str  # readonly: False
    command: str  # readonly: False
    progress: Optional[str]  # readonly: False
    params: Optional[list]  # readonly: False

    def __init__(self,
        batch_id: str,
        command: str,
        progress: Optional[str] = None,
        params: Optional[list] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class FileSet(object):

    def __init__(self) -> None: ...
    def to_dict(self) -> dict: ...


class SgxCredentials(object):
    enclave_pub_key: str  # readonly: False
    requestor_pub_key: str  # readonly: False
    payload_hash: str  # readonly: False
    ias_report: str  # readonly: False
    ias_sig: str  # readonly: False

    def __init__(self,
        enclave_pub_key: str,
        requestor_pub_key: str,
        payload_hash: str,
        ias_report: str,
        ias_sig: str
    ) -> None: ...
    def to_dict(self) -> dict: ...


class StartCommandBody(object):
    args: Optional[list]  # readonly: False

    def __init__(self,
        args: Optional[list] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class ActivityUsage(object):
    current_usage: Optional[list]  # readonly: False
    timestamp: int  # readonly: False

    def __init__(self,
        timestamp: int,
        current_usage: Optional[list] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class Credentials(object):
    sgx: SgxCredentials  # readonly: False

    def __init__(self,
        sgx: SgxCredentials
    ) -> None: ...
    def to_dict(self) -> dict: ...


class ExeScriptCommand(object):

    def __init__(self) -> None: ...
    def to_dict(self) -> dict: ...


class ExeScriptRequest(object):
    text: str  # readonly: False

    def __init__(self,
        text: str
    ) -> None: ...
    def to_dict(self) -> dict: ...


class CommandOutputBinAllOf(CommandOutput):
    _bin: Optional[list]  # readonly: False

    def __init__(self,
        _bin: Optional[list] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class RuntimeEventKindFinished(RuntimeEventKind):
    finished: RuntimeEventKindFinishedBody  # readonly: False

    def __init__(self,
        finished: RuntimeEventKindFinishedBody = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class RuntimeEventKindStdOutAllOf(RuntimeEventKind):
    stdout: CommandOutput  # readonly: False

    def __init__(self,
        stdout: CommandOutput = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class CreateActivityAllOf(ProviderEvent):
    requestor_pub_key: Optional[str]  # readonly: False

    def __init__(self,
        event_type: str,
        event_date: datetime,
        activity_id: str,
        agreement_id: str,
        requestor_pub_key: Optional[str] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class CreateActivity(ProviderEvent):
    requestor_pub_key: Optional[str]  # readonly: False

    def __init__(self,
        event_type: str,
        event_date: datetime,
        activity_id: str,
        agreement_id: str,
        requestor_pub_key: Optional[str] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class CommandOutputStr(CommandOutput):
    _str: Optional[str]  # readonly: False

    def __init__(self,
        _str: Optional[str] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class SignCommand(ExeScriptCommand):
    sign: SignCommandBody  # readonly: False

    def __init__(self,
        sign: SignCommandBody = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class RunCommand(ExeScriptCommand):
    run: RunCommandBody  # readonly: False

    def __init__(self,
        run: RunCommandBody = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class DeployCommand(ExeScriptCommand):
    deploy: dict  # readonly: False

    def __init__(self,
        deploy: dict = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class TransferCommand(ExeScriptCommand):
    transfer: TransferCommandBody  # readonly: False

    def __init__(self,
        transfer: TransferCommandBody = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class StartCommand(ExeScriptCommand):
    start: StartCommandBody  # readonly: False

    def __init__(self,
        start: StartCommandBody = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class StartCommandAllOf(ExeScriptCommand):
    start: StartCommandBody  # readonly: False

    def __init__(self,
        start: StartCommandBody = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class RuntimeEventKindStdErrAllOf(RuntimeEventKind):
    stderr: CommandOutput  # readonly: False

    def __init__(self,
        stderr: CommandOutput = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class RunCommandAllOf(ExeScriptCommand):
    run: RunCommandBody  # readonly: False

    def __init__(self,
        run: RunCommandBody = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class DeployCommandAllOf(ExeScriptCommand):
    deploy: dict  # readonly: False

    def __init__(self,
        deploy: dict = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class RuntimeEventKindStartedAllOf(RuntimeEventKind):
    started: ExeScriptCommand  # readonly: False

    def __init__(self,
        started: ExeScriptCommand = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class RuntimeEventKindFinishedAllOf(RuntimeEventKind):
    finished: RuntimeEventKindFinishedBody  # readonly: False

    def __init__(self,
        finished: RuntimeEventKindFinishedBody = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class TerminateCommand(ExeScriptCommand):
    terminate: TerminateCommandBody  # readonly: False

    def __init__(self,
        terminate: TerminateCommandBody = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class RuntimeEventKindStarted(RuntimeEventKind):
    started: ExeScriptCommand  # readonly: False

    def __init__(self,
        started: ExeScriptCommand = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class CommandOutputBin(CommandOutput):
    _bin: Optional[list]  # readonly: False

    def __init__(self,
        _bin: Optional[list] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class SignCommandAllOf(ExeScriptCommand):
    sign: SignCommandBody  # readonly: False

    def __init__(self,
        sign: SignCommandBody = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class CommandOutputStrAllOf(CommandOutput):
    _str: Optional[str]  # readonly: False

    def __init__(self,
        _str: Optional[str] = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class RuntimeEventKindStdOut(RuntimeEventKind):
    stdout: CommandOutput  # readonly: False

    def __init__(self,
        stdout: CommandOutput = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class RuntimeEventKindStdErr(RuntimeEventKind):
    stderr: CommandOutput  # readonly: False

    def __init__(self,
        stderr: CommandOutput = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class TerminateCommandAllOf(ExeScriptCommand):
    terminate: TerminateCommandBody  # readonly: False

    def __init__(self,
        terminate: TerminateCommandBody = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


class TransferCommandAllOf(ExeScriptCommand):
    transfer: TransferCommandBody  # readonly: False

    def __init__(self,
        transfer: TransferCommandBody = None
    ) -> None: ...
    def to_dict(self) -> dict: ...


