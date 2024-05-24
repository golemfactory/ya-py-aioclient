from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from golem_node_api_client import errors
from golem_node_api_client.client import AuthenticatedClient, Client
from golem_node_api_client.models.debit_note import DebitNote
from golem_node_api_client.models.error_message import ErrorMessage
from golem_node_api_client.types import Response


def _get_kwargs(
    debit_note_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        'method': 'get',
        'url': '/payment-api/v1/debitNotes/{debit_note_id}'.format(
            debit_note_id=debit_note_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DebitNote, ErrorMessage]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DebitNote.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ErrorMessage.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ErrorMessage.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ErrorMessage.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[DebitNote, ErrorMessage]]:
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
) -> Response[Union[DebitNote, ErrorMessage]]:
    """Get Debit Note.

    Args:
        debit_note_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DebitNote, ErrorMessage]]
    """

    kwargs = _get_kwargs(
        debit_note_id=debit_note_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    debit_note_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[DebitNote, ErrorMessage]]:
    """Get Debit Note.

    Args:
        debit_note_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DebitNote, ErrorMessage]
    """

    return sync_detailed(
        debit_note_id=debit_note_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    debit_note_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[DebitNote, ErrorMessage]]:
    """Get Debit Note.

    Args:
        debit_note_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DebitNote, ErrorMessage]]
    """

    kwargs = _get_kwargs(
        debit_note_id=debit_note_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    debit_note_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[DebitNote, ErrorMessage]]:
    """Get Debit Note.

    Args:
        debit_note_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DebitNote, ErrorMessage]
    """

    return (
        await asyncio_detailed(
            debit_note_id=debit_note_id,
            client=client,
        )
    ).parsed
