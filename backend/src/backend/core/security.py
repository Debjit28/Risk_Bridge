import jwt
from fastapi import Depends , HTTPException , status
from fastapi.security import HTTPAuthorizationCredentials , HTTPBearer
from jwt import PyJWKClient , PyJWTError

from backend.core.config import settings

## 1. Scheme to extract 'Authorization: Bearer <token>' header from requests
http_bearer = HTTPBearer(auto_error=True)

# JWKS client automatically downloads and caches Neon Auth's public keys in memory
jwks_client = (
    PyJWKClient(settings.neon_auth_jwks_url)
    if settings.neon_auth_jwks_url
    else None
)


#Role of get_current_user
# Extract Token: Grab the bearer token from the HTTP request headers via http_bearer.
# Find Public Key: Ask jwks_client to read the token's header (kid) and pick the matching public key from Neon Auth.
# Cryptographically Verify & Decode: Verify that the signature is genuine and the token is not expired.
# Handle Errors Cleanly: If the token is expired or tampered with, immediately return 401 Unauthorized.
# Return Payload: If valid, return the decoded payload dictionary (containing sub for user ID, email, etc.) to the route handler.

def get_current_user(
    credentials : HTTPAuthorizationCredentials = Depends(http_bearer) ,
    ) -> dict:
    
    """Verifies the Neon Auth JWT and returns the users claims."""
    if not jwks_client:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR ,
            detail="Neon Auth JWKS URL isnt configured",
        )
        
    token = credentials.credentials
    
    try:
        # Step 2: Get signing key from the JWT
        signing_key = jwks_client.get_signing_key_from_jwt(token)
        # Step 3: Decode & verify (RS256/ES256)
        payload = jwt.decode(
            token,
            signing_key.key,
            algorithms=["RS256", "ES256"],
            options={"verify_aud": False},
        )
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except PyJWTError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid token: {exc}",
            headers={"WWW-Authenticate": "Bearer"},
        )
    