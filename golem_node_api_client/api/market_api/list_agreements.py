import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agreement_state import AgreementState
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    app_session_id: Union[Unset, str] = UNSET,
    state: Union[Unset, AgreementState] = UNSET,
    after_timestamp: Union[Unset, datetime.datetime] = UNSET,
    before_timestamp: Union[Unset, datetime.datetime] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["appSessionId"] = app_session_id

    json_state: Union[Unset, str] = UNSET
    if not isinstance(state, Unset):
        json_state = state.value

    params["state"] = json_state

    json_after_timestamp: Union[Unset, str] = UNSET
    if not isinstance(after_timestamp, Unset):
        json_after_timestamp = after_timestamp.isoformat()
    params["afterTimestamp"] = json_after_timestamp

    json_before_timestamp: Union[Unset, str] = UNSET
    if not isinstance(before_timestamp, Unset):
        json_before_timestamp = before_timestamp.isoformat()
    params["beforeTimestamp"] = json_before_timestamp

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/market-api/v1/agreements",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if response.status_code == HTTPStatus.BAD_REQUEST:
        return None
    if response.status_code == HTTPStatus.UNAUTHORIZED:
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
    *,
    client: AuthenticatedClient,
    app_session_id: Union[Unset, str] = UNSET,
    state: Union[Unset, AgreementState] = UNSET,
    after_timestamp: Union[Unset, datetime.datetime] = UNSET,
    before_timestamp: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Any]:
    """ListAgreements - Lists agreements with optional filters

     List agreements.
    Supported filters: * state * creation datetime * app session id
    A well-formed call will result in a collection of objects with the following fields: * id *
    creationTs * approveTs * role

    Args:
        app_session_id (Union[Unset, str]):
        state (Union[Unset, AgreementState]): * `Proposal` - newly created by a Requestor (draft
            based on Proposal)
            * `Pending` - confirmed by a Requestor and send to Provider for approval
            * `Cancelled` by a Requestor
            * `Rejected` by a Provider
            * `Approved` by both sides
            * `Expired` - not approved, rejected nor cancelled within validity period
            * `Terminated` - finished after approval.
        after_timestamp (Union[Unset, datetime.datetime]):
        before_timestamp (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        app_session_id=app_session_id,
        state=state,
        after_timestamp=after_timestamp,
        before_timestamp=before_timestamp,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    app_session_id: Union[Unset, str] = UNSET,
    state: Union[Unset, AgreementState] = UNSET,
    after_timestamp: Union[Unset, datetime.datetime] = UNSET,
    before_timestamp: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Any]:
    """ListAgreements - Lists agreements with optional filters

     List agreements.
    Supported filters: * state * creation datetime * app session id
    A well-formed call will result in a collection of objects with the following fields: * id *
    creationTs * approveTs * role

    Args:
        app_session_id (Union[Unset, str]):
        state (Union[Unset, AgreementState]): * `Proposal` - newly created by a Requestor (draft
            based on Proposal)
            * `Pending` - confirmed by a Requestor and send to Provider for approval
            * `Cancelled` by a Requestor
            * `Rejected` by a Provider
            * `Approved` by both sides
            * `Expired` - not approved, rejected nor cancelled within validity period
            * `Terminated` - finished after approval.
        after_timestamp (Union[Unset, datetime.datetime]):
        before_timestamp (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        app_session_id=app_session_id,
        state=state,
        after_timestamp=after_timestamp,
        before_timestamp=before_timestamp,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
