from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    invoice_id: str,
    *,
    timeout: Union[Unset, float] = 5.0,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["timeout"] = timeout

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/payment-api/v1/invoices/{invoice_id}/cancel".format(
            invoice_id=invoice_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        return None
    if response.status_code == HTTPStatus.NOT_FOUND:
        return None
    if response.status_code == HTTPStatus.CONFLICT:
        return None
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        return None
    if response.status_code == HTTPStatus.GATEWAY_TIMEOUT:
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
    invoice_id: str,
    *,
    client: AuthenticatedClient,
    timeout: Union[Unset, float] = 5.0,
) -> Response[Any]:
    """Cancel Invoice.

     This is a blocking operation. It will not return until the Requestor has acknowledged cancelling the
    Invoice or timeout has passed. The Requestor may refuse to cancel the Invoice if they have already
    accepted it.

    Args:
        invoice_id (str):
        timeout (Union[Unset, float]):  Default: 5.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        invoice_id=invoice_id,
        timeout=timeout,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    invoice_id: str,
    *,
    client: AuthenticatedClient,
    timeout: Union[Unset, float] = 5.0,
) -> Response[Any]:
    """Cancel Invoice.

     This is a blocking operation. It will not return until the Requestor has acknowledged cancelling the
    Invoice or timeout has passed. The Requestor may refuse to cancel the Invoice if they have already
    accepted it.

    Args:
        invoice_id (str):
        timeout (Union[Unset, float]):  Default: 5.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        invoice_id=invoice_id,
        timeout=timeout,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
