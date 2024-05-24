from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from golem_node_api_client import errors
from golem_node_api_client.client import AuthenticatedClient, Client
from golem_node_api_client.models.agreement import Agreement
from golem_node_api_client.models.error_message import ErrorMessage
from golem_node_api_client.types import Response


def _get_kwargs(
    agreement_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        'method': 'get',
        'url': '/market-api/v1/agreements/{agreement_id}'.format(
            agreement_id=agreement_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Agreement, ErrorMessage]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Agreement.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ErrorMessage.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ErrorMessage.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Agreement, ErrorMessage]]:
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
) -> Response[Union[Agreement, ErrorMessage]]:
    """GetAgreement - Fetches agreement with given agreement id.

    Args:
        agreement_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Agreement, ErrorMessage]]
    """

    kwargs = _get_kwargs(
        agreement_id=agreement_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    agreement_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Agreement, ErrorMessage]]:
    """GetAgreement - Fetches agreement with given agreement id.

    Args:
        agreement_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Agreement, ErrorMessage]
    """

    return sync_detailed(
        agreement_id=agreement_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    agreement_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Agreement, ErrorMessage]]:
    """GetAgreement - Fetches agreement with given agreement id.

    Args:
        agreement_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Agreement, ErrorMessage]]
    """

    kwargs = _get_kwargs(
        agreement_id=agreement_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    agreement_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Agreement, ErrorMessage]]:
    """GetAgreement - Fetches agreement with given agreement id.

    Args:
        agreement_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Agreement, ErrorMessage]
    """

    return (
        await asyncio_detailed(
            agreement_id=agreement_id,
            client=client,
        )
    ).parsed
