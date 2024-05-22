from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    agreement_id: str,
    *,
    app_session_id: Union[Unset, str] = UNSET,
    timeout: Union[Unset, float] = 5.0,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["appSessionId"] = app_session_id

    params["timeout"] = timeout

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/market-api/v1/agreements/{agreement_id}/approve".format(
            agreement_id=agreement_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Any]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        return None
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        return None
    if response.status_code == HTTPStatus.NOT_FOUND:
        return None
    if response.status_code == HTTPStatus.REQUEST_TIMEOUT:
        return None
    if response.status_code == HTTPStatus.GONE:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    agreement_id: str,
    *,
    client: AuthenticatedClient,
    app_session_id: Union[Unset, str] = UNSET,
    timeout: Union[Unset, float] = 5.0,
) -> Response[Any]:
    """ApproveAgreement - Approves Agreement proposed by the Reqestor.

     This is a blocking operation. The call may be aborted by Provider caller code. After the call is
    aborted or timed out, another `approveAgreement` call can be raised on the same `agreementId`.

    **Note**: It is expected from the Provider node implementation to “ring-fence” the resources
    required to fulfill the Agreement before the ApproveAgreement is sent. However, the resources should
    not be fully committed until `Approved` response is received from the `approveAgreement` call.

    **Note**: Mutually exclusive with `rejectAgreement`.

    Args:
        agreement_id (str):
        app_session_id (Union[Unset, str]):
        timeout (Union[Unset, float]):  Default: 5.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        agreement_id=agreement_id,
        app_session_id=app_session_id,
        timeout=timeout,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    agreement_id: str,
    *,
    client: AuthenticatedClient,
    app_session_id: Union[Unset, str] = UNSET,
    timeout: Union[Unset, float] = 5.0,
) -> Response[Any]:
    """ApproveAgreement - Approves Agreement proposed by the Reqestor.

     This is a blocking operation. The call may be aborted by Provider caller code. After the call is
    aborted or timed out, another `approveAgreement` call can be raised on the same `agreementId`.

    **Note**: It is expected from the Provider node implementation to “ring-fence” the resources
    required to fulfill the Agreement before the ApproveAgreement is sent. However, the resources should
    not be fully committed until `Approved` response is received from the `approveAgreement` call.

    **Note**: Mutually exclusive with `rejectAgreement`.

    Args:
        agreement_id (str):
        app_session_id (Union[Unset, str]):
        timeout (Union[Unset, float]):  Default: 5.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        agreement_id=agreement_id,
        app_session_id=app_session_id,
        timeout=timeout,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
