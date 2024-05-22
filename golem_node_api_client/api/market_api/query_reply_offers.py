from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    subscription_id: str,
    query_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/market-api/v1/offers/{subscription_id}/propertyQuery/{query_id}".format(
            subscription_id=subscription_id,
            query_id=query_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Any]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        return None
    if response.status_code == HTTPStatus.BAD_REQUEST:
        return None
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        return None
    if response.status_code == HTTPStatus.NOT_FOUND:
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
    subscription_id: str,
    query_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """QueryReplyOffers - Handles dynamic property query.

     Sends a response to a received property value query.

    The Market Matching Mechanism, when resolving the match relation for the specific Demand-Offer pair,
    is to detect the “dynamic” properties required (via constraints) by the other side. At this point,
    it is able to query the issuing node for those properties and submit the other side’s requested
    properties as the context of the query.

    **Note**: The property query responses may be submitted in “chunks”, ie. the responder may choose to
    resolve ‘quick’/lightweight’ properties faster and provide response sooner, while still working on
    more time-consuming properties in the background. Therefore the response contains both the resolved
    properties, as well as list of properties which responder knows still require resolution.

    **Note**: This method must be implemented for Market API Capability Level 2.

    Args:
        subscription_id (str):
        query_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        subscription_id=subscription_id,
        query_id=query_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    subscription_id: str,
    query_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """QueryReplyOffers - Handles dynamic property query.

     Sends a response to a received property value query.

    The Market Matching Mechanism, when resolving the match relation for the specific Demand-Offer pair,
    is to detect the “dynamic” properties required (via constraints) by the other side. At this point,
    it is able to query the issuing node for those properties and submit the other side’s requested
    properties as the context of the query.

    **Note**: The property query responses may be submitted in “chunks”, ie. the responder may choose to
    resolve ‘quick’/lightweight’ properties faster and provide response sooner, while still working on
    more time-consuming properties in the background. Therefore the response contains both the resolved
    properties, as well as list of properties which responder knows still require resolution.

    **Note**: This method must be implemented for Market API Capability Level 2.

    Args:
        subscription_id (str):
        query_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        subscription_id=subscription_id,
        query_id=query_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
