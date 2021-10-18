from fastapi import HTTPException
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND,\
    HTTP_422_UNPROCESSABLE_ENTITY, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_403_FORBIDDEN, HTTP_409_CONFLICT

InvalidCredentialsException = HTTPException(
    status_code=HTTP_401_UNAUTHORIZED,
    detail="Password provided is invalid",
    headers={"WWW-Authenticate": "Bearer"}
)

OldPasswordProvidedException = HTTPException(
    status_code=HTTP_409_CONFLICT,
    detail="New and old password cannot be same",
    headers={"WWW-Authenticate": "Bearer"}
)

IncorrectPasswordException = HTTPException(
    status_code=HTTP_403_FORBIDDEN,
    detail="Old password is incorrect",
    headers={"WWW-Authenticate": "Bearer"}
)

PasswordNotConfirmedException = HTTPException(
    status_code=HTTP_409_CONFLICT,
    detail="Password and Confirm Password must be same",
    headers={"WWW-Authenticate": "Bearer"}
)


RequestUnauthorizedException = HTTPException(
    status_code=HTTP_401_UNAUTHORIZED,
    detail="This operation is not authorised",
    headers={"WWW-Authenticate": "Bearer"}
)

TokenExpiredException = HTTPException(
    status_code=HTTP_401_UNAUTHORIZED,
    detail="Token has expired",
    headers={"WWW-Authenticate": "Bearer"}
)

RefreshTokenExpiredException = HTTPException(
    status_code=HTTP_422_UNPROCESSABLE_ENTITY,
    detail="Refresh token has expired. Cannot be processed. Consider logging in again",
    headers={"WWW-Authenticate": "Bearer"}
)

EmailNotVerifiedException = HTTPException(
    status_code=HTTP_403_FORBIDDEN,
    detail="Please verify your email account first.",
    headers={"WWW-Authenticate": "Bearer"}
)

OperationNotPermittedException = HTTPException(
    status_code=HTTP_403_FORBIDDEN,
    detail="Operation forbidden, permission denied.",
    headers={"WWW-Authenticate": "Bearer"}
)

UserNotFoundException = HTTPException(
    status_code=HTTP_404_NOT_FOUND,
    detail="No such user exists"
)

InvalidIdException = HTTPException(
    status_code=HTTP_404_NOT_FOUND,
    detail="The id you provided is invalid. Check the ID you provided"
)

UserAlreadyExistsException = HTTPException(
    status_code=HTTP_409_CONFLICT,
    detail="An account with this email already exists"
)


UnprocessableEntity = HTTPException(
    status_code=HTTP_422_UNPROCESSABLE_ENTITY,
    detail="validation error"
)

ServerError = HTTPException(
    status_code=HTTP_500_INTERNAL_SERVER_ERROR,
    detail="server error"
)

NotFoundException = HTTPException(
    status_code=HTTP_404_NOT_FOUND,
    detail="No such resource exists. Check the ID you provided"
)


################Exceptions for entries####################
EntryNotFoundException = HTTPException(
    status_code=HTTP_404_NOT_FOUND,
    detail="No such entry exists"
)

InvalidEntryActionException = HTTPException(
    status_code=HTTP_422_UNPROCESSABLE_ENTITY,
    detail="No such entry exists"
)

OperationNotAllowedException = HTTPException(
    status_code=HTTP_403_FORBIDDEN,
    detail="Cannot take action on your own entry"
)