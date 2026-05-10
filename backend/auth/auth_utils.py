from fastapi import Header, HTTPException
from services import AuthService
from postgre import get_session, Users


async def authorize_private_endpoint_via_refresh(
    token: str = Header(
        ..., title="Authorization Bearer token", example="Bearer [token]"
    )
) -> Users:
    return await authorize_private_endpoint(token=token, accept_access=False)


async def authorize_private_endpoint(
    token: str = Header(
        ..., title="Authorization Bearer token", example="Bearer [token]"
    ),
    accept_access: bool = True,
) -> Users:
    """
    Use in fastAPI `Depends`
    Raise 401 on failed authorization
    """
    postgres_session = await get_session()

    try:
        auth_service: AuthService = await AuthService.create(postgres_session)
        out_user = await auth_service.authorize_request_jwt_and_return_user(
            jwt=token, accept_access=accept_access
        )
        await auth_service.close(commit=True)
        if not out_user:
            raise HTTPException(status_code=401, detail="Unauthorized")
        return out_user
    except Exception as e:
        await auth_service.close(commit=False)
        raise e from e
