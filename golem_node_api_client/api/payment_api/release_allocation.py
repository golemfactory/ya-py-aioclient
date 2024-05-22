from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    allocation_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": "/payment-api/v1/allocations/{allocation_id}".format(
            allocation_id=allocation_id,
        ),
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
    if response.status_code == HTTPStatus.GONE:
        return None
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
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
    allocation_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Release Allocation.

     The Allocation of amount is released. Note that this operation releases currently allocated amount
    (which may have been reduced by subsequent Invoice Payments).

    **WARNING:** Deposits not implemented.

    If the Allocation was connected with a Deposit the release amount from Deposit shall be marked as
    pending to be paid back to Requestor - and eventually will be paid back, unless a subsequent
    Allocation with Deposit is made. The Payment Platform implementations may optimize unnecessary fund
    transfers (i.e. will not pay back the Deposit if released funds can be assigned to a new Allocation
    with Deposit).

    Args:
        allocation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        allocation_id=allocation_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    allocation_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Release Allocation.

     The Allocation of amount is released. Note that this operation releases currently allocated amount
    (which may have been reduced by subsequent Invoice Payments).

    **WARNING:** Deposits not implemented.

    If the Allocation was connected with a Deposit the release amount from Deposit shall be marked as
    pending to be paid back to Requestor - and eventually will be paid back, unless a subsequent
    Allocation with Deposit is made. The Payment Platform implementations may optimize unnecessary fund
    transfers (i.e. will not pay back the Deposit if released funds can be assigned to a new Allocation
    with Deposit).

    Args:
        allocation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        allocation_id=allocation_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
