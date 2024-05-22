from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs() -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/market-api/v1/agreements",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, str]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = cast(str, response.json())
        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = cast(Any, None)
        return response_409
    if response.status_code == HTTPStatus.GONE:
        response_410 = cast(Any, None)
        return response_410
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, str]]:
    """CreateAgreement - Creates Agreement from selected Proposal.

     Initiates the Agreement handshake phase.

    Formulates an Agreement artifact from the Proposal indicated by the received Proposal Id. Created
    Agreement is in `Proposal` state.

    The Approval Expiry Date is added to Agreement artifact and implies the effective timeout on the
    whole Agreement Confirmation sequence.

    A successful call to `createAgreement` shall immediately be followed by a `confirmAgreement` and
    `waitForApproval` call in order to listen for responses from the Provider.

    **Note**: Moves given Proposal to `Approved` state.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, str]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, str]]:
    """CreateAgreement - Creates Agreement from selected Proposal.

     Initiates the Agreement handshake phase.

    Formulates an Agreement artifact from the Proposal indicated by the received Proposal Id. Created
    Agreement is in `Proposal` state.

    The Approval Expiry Date is added to Agreement artifact and implies the effective timeout on the
    whole Agreement Confirmation sequence.

    A successful call to `createAgreement` shall immediately be followed by a `confirmAgreement` and
    `waitForApproval` call in order to listen for responses from the Provider.

    **Note**: Moves given Proposal to `Approved` state.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, str]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, str]]:
    """CreateAgreement - Creates Agreement from selected Proposal.

     Initiates the Agreement handshake phase.

    Formulates an Agreement artifact from the Proposal indicated by the received Proposal Id. Created
    Agreement is in `Proposal` state.

    The Approval Expiry Date is added to Agreement artifact and implies the effective timeout on the
    whole Agreement Confirmation sequence.

    A successful call to `createAgreement` shall immediately be followed by a `confirmAgreement` and
    `waitForApproval` call in order to listen for responses from the Provider.

    **Note**: Moves given Proposal to `Approved` state.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, str]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, str]]:
    """CreateAgreement - Creates Agreement from selected Proposal.

     Initiates the Agreement handshake phase.

    Formulates an Agreement artifact from the Proposal indicated by the received Proposal Id. Created
    Agreement is in `Proposal` state.

    The Approval Expiry Date is added to Agreement artifact and implies the effective timeout on the
    whole Agreement Confirmation sequence.

    A successful call to `createAgreement` shall immediately be followed by a `confirmAgreement` and
    `waitForApproval` call in order to listen for responses from the Provider.

    **Note**: Moves given Proposal to `Approved` state.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, str]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
