from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from golem_node_api_client import errors
from golem_node_api_client.client import AuthenticatedClient, Client
from golem_node_api_client.models.error_message import ErrorMessage
from golem_node_api_client.models.reason import Reason
from golem_node_api_client.types import Response


def _get_kwargs(
    agreement_id: str,
    *,
    body: Reason,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        'method': 'post',
        'url': '/market-api/v1/agreements/{agreement_id}/terminate'.format(
            agreement_id=agreement_id,
        ),
    }

    _body = body.to_dict()

    _kwargs['json'] = _body
    headers['Content-Type'] = 'application/json'

    _kwargs['headers'] = headers
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
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = ErrorMessage.from_dict(response.json())

        return response_409
    if response.status_code == HTTPStatus.GONE:
        response_410 = ErrorMessage.from_dict(response.json())

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
    agreement_id: str,
    *,
    client: AuthenticatedClient,
    body: Reason,
) -> Response[Union[Any, ErrorMessage]]:
    r"""TerminateAgreement - Terminates approved Agreement.

     Method to finish/close the Agreement while in `Approved` state.

    The other party gets notified about calling party decision to terminate a \"running\" agreement.

    **Note**: Can be invoked at any time after Agreement was approved by both sides.

    **Note**: Financial and reputational consequences are not defined by this specification.

    Args:
        agreement_id (str):
        body (Reason): Generic Event reason information structure.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorMessage]]
    """

    kwargs = _get_kwargs(
        agreement_id=agreement_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    agreement_id: str,
    *,
    client: AuthenticatedClient,
    body: Reason,
) -> Optional[Union[Any, ErrorMessage]]:
    r"""TerminateAgreement - Terminates approved Agreement.

     Method to finish/close the Agreement while in `Approved` state.

    The other party gets notified about calling party decision to terminate a \"running\" agreement.

    **Note**: Can be invoked at any time after Agreement was approved by both sides.

    **Note**: Financial and reputational consequences are not defined by this specification.

    Args:
        agreement_id (str):
        body (Reason): Generic Event reason information structure.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorMessage]
    """

    return sync_detailed(
        agreement_id=agreement_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    agreement_id: str,
    *,
    client: AuthenticatedClient,
    body: Reason,
) -> Response[Union[Any, ErrorMessage]]:
    r"""TerminateAgreement - Terminates approved Agreement.

     Method to finish/close the Agreement while in `Approved` state.

    The other party gets notified about calling party decision to terminate a \"running\" agreement.

    **Note**: Can be invoked at any time after Agreement was approved by both sides.

    **Note**: Financial and reputational consequences are not defined by this specification.

    Args:
        agreement_id (str):
        body (Reason): Generic Event reason information structure.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorMessage]]
    """

    kwargs = _get_kwargs(
        agreement_id=agreement_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    agreement_id: str,
    *,
    client: AuthenticatedClient,
    body: Reason,
) -> Optional[Union[Any, ErrorMessage]]:
    r"""TerminateAgreement - Terminates approved Agreement.

     Method to finish/close the Agreement while in `Approved` state.

    The other party gets notified about calling party decision to terminate a \"running\" agreement.

    **Note**: Can be invoked at any time after Agreement was approved by both sides.

    **Note**: Financial and reputational consequences are not defined by this specification.

    Args:
        agreement_id (str):
        body (Reason): Generic Event reason information structure.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorMessage]
    """

    return (
        await asyncio_detailed(
            agreement_id=agreement_id,
            client=client,
            body=body,
        )
    ).parsed
