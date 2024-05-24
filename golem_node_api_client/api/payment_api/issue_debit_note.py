from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from golem_node_api_client import errors
from golem_node_api_client.client import AuthenticatedClient, Client
from golem_node_api_client.models.debit_note import DebitNote
from golem_node_api_client.models.error_message import ErrorMessage
from golem_node_api_client.types import Response


def _get_kwargs(
    *,
    body: DebitNote,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        'method': 'post',
        'url': '/payment-api/v1/debitNotes',
    }

    _body = body.to_dict()

    _kwargs['json'] = _body
    headers['Content-Type'] = 'application/json'

    _kwargs['headers'] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DebitNote, ErrorMessage]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = DebitNote.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorMessage.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ErrorMessage.from_dict(response.json())

        return response_401
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
    *,
    client: AuthenticatedClient,
    body: DebitNote,
) -> Response[Union[DebitNote, ErrorMessage]]:
    """Issue a Debit Note.

    Args:
        body (DebitNote): A Debit Note is an artifact issued by the Provider to the Requestor, in
            the context of a specific Activity. It is a notification of Total Amount Due incurred by
            the Activity until the moment the Debit Note is issued. This is expected to be used as
            trigger for payment in upfront-payment or pay-as-you-go scenarios.

            **NOTE:** Only Debit Notes with non-null paymentDueDate are expected to trigger payments.

            **NOTE:** Debit Notes flag the current Total Amount Due, which is accumulated from the
            start of Activity. Debit Notes are expected to trigger payments, therefore payment amount
            for the newly received Debit Note is expected to be determined by difference of Total
            Payments for the Agreement vs Total Amount Due.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DebitNote, ErrorMessage]]
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
    body: DebitNote,
) -> Optional[Union[DebitNote, ErrorMessage]]:
    """Issue a Debit Note.

    Args:
        body (DebitNote): A Debit Note is an artifact issued by the Provider to the Requestor, in
            the context of a specific Activity. It is a notification of Total Amount Due incurred by
            the Activity until the moment the Debit Note is issued. This is expected to be used as
            trigger for payment in upfront-payment or pay-as-you-go scenarios.

            **NOTE:** Only Debit Notes with non-null paymentDueDate are expected to trigger payments.

            **NOTE:** Debit Notes flag the current Total Amount Due, which is accumulated from the
            start of Activity. Debit Notes are expected to trigger payments, therefore payment amount
            for the newly received Debit Note is expected to be determined by difference of Total
            Payments for the Agreement vs Total Amount Due.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DebitNote, ErrorMessage]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: DebitNote,
) -> Response[Union[DebitNote, ErrorMessage]]:
    """Issue a Debit Note.

    Args:
        body (DebitNote): A Debit Note is an artifact issued by the Provider to the Requestor, in
            the context of a specific Activity. It is a notification of Total Amount Due incurred by
            the Activity until the moment the Debit Note is issued. This is expected to be used as
            trigger for payment in upfront-payment or pay-as-you-go scenarios.

            **NOTE:** Only Debit Notes with non-null paymentDueDate are expected to trigger payments.

            **NOTE:** Debit Notes flag the current Total Amount Due, which is accumulated from the
            start of Activity. Debit Notes are expected to trigger payments, therefore payment amount
            for the newly received Debit Note is expected to be determined by difference of Total
            Payments for the Agreement vs Total Amount Due.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DebitNote, ErrorMessage]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: DebitNote,
) -> Optional[Union[DebitNote, ErrorMessage]]:
    """Issue a Debit Note.

    Args:
        body (DebitNote): A Debit Note is an artifact issued by the Provider to the Requestor, in
            the context of a specific Activity. It is a notification of Total Amount Due incurred by
            the Activity until the moment the Debit Note is issued. This is expected to be used as
            trigger for payment in upfront-payment or pay-as-you-go scenarios.

            **NOTE:** Only Debit Notes with non-null paymentDueDate are expected to trigger payments.

            **NOTE:** Debit Notes flag the current Total Amount Due, which is accumulated from the
            start of Activity. Debit Notes are expected to trigger payments, therefore payment amount
            for the newly received Debit Note is expected to be determined by difference of Total
            Payments for the Agreement vs Total Amount Due.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DebitNote, ErrorMessage]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
