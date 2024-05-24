from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from golem_node_api_client import errors
from golem_node_api_client.client import AuthenticatedClient, Client
from golem_node_api_client.models.error_message import ErrorMessage
from golem_node_api_client.types import UNSET, Response, Unset


def _get_kwargs(
    agreement_id: str,
    *,
    app_session_id: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params['appSessionId'] = app_session_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        'method': 'post',
        'url': '/market-api/v1/agreements/{agreement_id}/confirm'.format(
            agreement_id=agreement_id,
        ),
        'params': params,
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
    app_session_id: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ErrorMessage]]:
    """ConfirmAgreement - Sends Agreement proposal to the Provider.

     Signs self-created Agreement and sends it to the Provider.

    This call should immediately follow `createAgreement`.

    Args:
        agreement_id (str):
        app_session_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorMessage]]
    """

    kwargs = _get_kwargs(
        agreement_id=agreement_id,
        app_session_id=app_session_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    agreement_id: str,
    *,
    client: AuthenticatedClient,
    app_session_id: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ErrorMessage]]:
    """ConfirmAgreement - Sends Agreement proposal to the Provider.

     Signs self-created Agreement and sends it to the Provider.

    This call should immediately follow `createAgreement`.

    Args:
        agreement_id (str):
        app_session_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorMessage]
    """

    return sync_detailed(
        agreement_id=agreement_id,
        client=client,
        app_session_id=app_session_id,
    ).parsed


async def asyncio_detailed(
    agreement_id: str,
    *,
    client: AuthenticatedClient,
    app_session_id: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ErrorMessage]]:
    """ConfirmAgreement - Sends Agreement proposal to the Provider.

     Signs self-created Agreement and sends it to the Provider.

    This call should immediately follow `createAgreement`.

    Args:
        agreement_id (str):
        app_session_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorMessage]]
    """

    kwargs = _get_kwargs(
        agreement_id=agreement_id,
        app_session_id=app_session_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    agreement_id: str,
    *,
    client: AuthenticatedClient,
    app_session_id: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ErrorMessage]]:
    """ConfirmAgreement - Sends Agreement proposal to the Provider.

     Signs self-created Agreement and sends it to the Provider.

    This call should immediately follow `createAgreement`.

    Args:
        agreement_id (str):
        app_session_id (Union[Unset, str]):

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
            app_session_id=app_session_id,
        )
    ).parsed
