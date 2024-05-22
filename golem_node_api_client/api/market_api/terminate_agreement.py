from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    agreement_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/market-api/v1/agreements/{agreement_id}/terminate".format(
            agreement_id=agreement_id,
        ),
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
    if response.status_code == HTTPStatus.CONFLICT:
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
) -> Response[Any]:
    r"""TerminateAgreement - Terminates approved Agreement.

     Method to finish/close the Agreement while in `Approved` state.

    The other party gets notified about calling party decision to terminate a \"running\" agreement.

    **Note**: Can be invoked at any time after Agreement was approved by both sides.

    **Note**: Financial and reputational consequences are not defined by this specification.

    Args:
        agreement_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        agreement_id=agreement_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    agreement_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    r"""TerminateAgreement - Terminates approved Agreement.

     Method to finish/close the Agreement while in `Approved` state.

    The other party gets notified about calling party decision to terminate a \"running\" agreement.

    **Note**: Can be invoked at any time after Agreement was approved by both sides.

    **Note**: Financial and reputational consequences are not defined by this specification.

    Args:
        agreement_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        agreement_id=agreement_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
