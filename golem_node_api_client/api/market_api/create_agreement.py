from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from golem_node_api_client import errors
from golem_node_api_client.client import AuthenticatedClient, Client
from golem_node_api_client.models.agreement_proposal import AgreementProposal
from golem_node_api_client.models.error_message import ErrorMessage
from golem_node_api_client.types import Response


def _get_kwargs(
    *,
    body: AgreementProposal,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        'method': 'post',
        'url': '/market-api/v1/agreements',
    }

    _body = body.to_dict()

    _kwargs['json'] = _body
    headers['Content-Type'] = 'application/json'

    _kwargs['headers'] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorMessage, str]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = cast(str, response.json())
        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorMessage.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ErrorMessage.from_dict(response.json())

        return response_401
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
) -> Response[Union[ErrorMessage, str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AgreementProposal,
) -> Response[Union[ErrorMessage, str]]:
    """CreateAgreement - Creates Agreement from selected Proposal.

     Initiates the Agreement handshake phase.

    Formulates an Agreement artifact from the Proposal indicated by the received Proposal Id. Created
    Agreement is in `Proposal` state.

    The Approval Expiry Date is added to Agreement artifact and implies the effective timeout on the
    whole Agreement Confirmation sequence.

    A successful call to `createAgreement` shall immediately be followed by a `confirmAgreement` and
    `waitForApproval` call in order to listen for responses from the Provider.

    **Note**: Moves given Proposal to `Approved` state.

    Args:
        body (AgreementProposal):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorMessage, str]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: AgreementProposal,
) -> Optional[Union[ErrorMessage, str]]:
    """CreateAgreement - Creates Agreement from selected Proposal.

     Initiates the Agreement handshake phase.

    Formulates an Agreement artifact from the Proposal indicated by the received Proposal Id. Created
    Agreement is in `Proposal` state.

    The Approval Expiry Date is added to Agreement artifact and implies the effective timeout on the
    whole Agreement Confirmation sequence.

    A successful call to `createAgreement` shall immediately be followed by a `confirmAgreement` and
    `waitForApproval` call in order to listen for responses from the Provider.

    **Note**: Moves given Proposal to `Approved` state.

    Args:
        body (AgreementProposal):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorMessage, str]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AgreementProposal,
) -> Response[Union[ErrorMessage, str]]:
    """CreateAgreement - Creates Agreement from selected Proposal.

     Initiates the Agreement handshake phase.

    Formulates an Agreement artifact from the Proposal indicated by the received Proposal Id. Created
    Agreement is in `Proposal` state.

    The Approval Expiry Date is added to Agreement artifact and implies the effective timeout on the
    whole Agreement Confirmation sequence.

    A successful call to `createAgreement` shall immediately be followed by a `confirmAgreement` and
    `waitForApproval` call in order to listen for responses from the Provider.

    **Note**: Moves given Proposal to `Approved` state.

    Args:
        body (AgreementProposal):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorMessage, str]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: AgreementProposal,
) -> Optional[Union[ErrorMessage, str]]:
    """CreateAgreement - Creates Agreement from selected Proposal.

     Initiates the Agreement handshake phase.

    Formulates an Agreement artifact from the Proposal indicated by the received Proposal Id. Created
    Agreement is in `Proposal` state.

    The Approval Expiry Date is added to Agreement artifact and implies the effective timeout on the
    whole Agreement Confirmation sequence.

    A successful call to `createAgreement` shall immediately be followed by a `confirmAgreement` and
    `waitForApproval` call in order to listen for responses from the Provider.

    **Note**: Moves given Proposal to `Approved` state.

    Args:
        body (AgreementProposal):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorMessage, str]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
