import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    debit_note_id: str,
    *,
    after_timestamp: Union[Unset, datetime.datetime] = UNSET,
    max_items: Union[Unset, int] = 10,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_after_timestamp: Union[Unset, str] = UNSET
    if not isinstance(after_timestamp, Unset):
        json_after_timestamp = after_timestamp.isoformat()
    params["afterTimestamp"] = json_after_timestamp

    params["maxItems"] = max_items

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/payment-api/v1/debitNotes/{debit_note_id}/payments".format(
            debit_note_id=debit_note_id,
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
    debit_note_id: str,
    *,
    client: AuthenticatedClient,
    after_timestamp: Union[Unset, datetime.datetime] = UNSET,
    max_items: Union[Unset, int] = 10,
) -> Response[Any]:
    """Get Payments for Debit Note.

     **WARNING:** Operation not implemented.

    Args:
        debit_note_id (str):
        after_timestamp (Union[Unset, datetime.datetime]):
        max_items (Union[Unset, int]):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        debit_note_id=debit_note_id,
        after_timestamp=after_timestamp,
        max_items=max_items,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    debit_note_id: str,
    *,
    client: AuthenticatedClient,
    after_timestamp: Union[Unset, datetime.datetime] = UNSET,
    max_items: Union[Unset, int] = 10,
) -> Response[Any]:
    """Get Payments for Debit Note.

     **WARNING:** Operation not implemented.

    Args:
        debit_note_id (str):
        after_timestamp (Union[Unset, datetime.datetime]):
        max_items (Union[Unset, int]):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        debit_note_id=debit_note_id,
        after_timestamp=after_timestamp,
        max_items=max_items,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
