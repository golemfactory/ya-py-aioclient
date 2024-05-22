from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agreement import Agreement
from ...types import Response


def _get_kwargs(
    agreement_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/market-api/v1/agreements/{agreement_id}".format(
            agreement_id=agreement_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Agreement, Any]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Agreement.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Agreement, Any]]:
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
) -> Response[Union[Agreement, Any]]:
    """GetAgreement - Fetches agreement with given agreement id.

    Args:
        agreement_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Agreement, Any]]
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
) -> Optional[Union[Agreement, Any]]:
    """GetAgreement - Fetches agreement with given agreement id.

    Args:
        agreement_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Agreement, Any]
    """

    return sync_detailed(
        agreement_id=agreement_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    agreement_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Agreement, Any]]:
    """GetAgreement - Fetches agreement with given agreement id.

    Args:
        agreement_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Agreement, Any]]
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
) -> Optional[Union[Agreement, Any]]:
    """GetAgreement - Fetches agreement with given agreement id.

    Args:
        agreement_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Agreement, Any]
    """

    return (
        await asyncio_detailed(
            agreement_id=agreement_id,
            client=client,
        )
    ).parsed
