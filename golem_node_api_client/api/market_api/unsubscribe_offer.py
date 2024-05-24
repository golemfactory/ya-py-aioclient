from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from golem_node_api_client import errors
from golem_node_api_client.client import AuthenticatedClient, Client
from golem_node_api_client.models.error_message import ErrorMessage
from golem_node_api_client.types import Response


def _get_kwargs(
    subscription_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        'method': 'delete',
        'url': '/market-api/v1/offers/{subscription_id}'.format(
            subscription_id=subscription_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ErrorMessage]]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ErrorMessage.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ErrorMessage.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.GONE:
        response_410 = cast(Any, None)
        return response_410
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ErrorMessage]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    subscription_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, ErrorMessage]]:
    """UnsubscribeOffer - Stop subscription for previously published Offer.

     Stop receiving Proposals.

    **Note**: this will terminate all pending `collectDemands` calls on this subscription. This implies,
    that client code should not `unsubscribeOffer` before it has received all expected/useful inputs
    from `collectDemands`.

    Args:
        subscription_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorMessage]]
    """

    kwargs = _get_kwargs(
        subscription_id=subscription_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    subscription_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ErrorMessage]]:
    """UnsubscribeOffer - Stop subscription for previously published Offer.

     Stop receiving Proposals.

    **Note**: this will terminate all pending `collectDemands` calls on this subscription. This implies,
    that client code should not `unsubscribeOffer` before it has received all expected/useful inputs
    from `collectDemands`.

    Args:
        subscription_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorMessage]
    """

    return sync_detailed(
        subscription_id=subscription_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    subscription_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, ErrorMessage]]:
    """UnsubscribeOffer - Stop subscription for previously published Offer.

     Stop receiving Proposals.

    **Note**: this will terminate all pending `collectDemands` calls on this subscription. This implies,
    that client code should not `unsubscribeOffer` before it has received all expected/useful inputs
    from `collectDemands`.

    Args:
        subscription_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorMessage]]
    """

    kwargs = _get_kwargs(
        subscription_id=subscription_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    subscription_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ErrorMessage]]:
    """UnsubscribeOffer - Stop subscription for previously published Offer.

     Stop receiving Proposals.

    **Note**: this will terminate all pending `collectDemands` calls on this subscription. This implies,
    that client code should not `unsubscribeOffer` before it has received all expected/useful inputs
    from `collectDemands`.

    Args:
        subscription_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorMessage]
    """

    return (
        await asyncio_detailed(
            subscription_id=subscription_id,
            client=client,
        )
    ).parsed
