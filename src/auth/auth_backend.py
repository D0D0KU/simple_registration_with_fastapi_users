from fastapi_users.authentication import CookieTransport

from fastapi_users.authentication import AuthenticationBackend, JWTStrategy

from src.auth.config import SECRET


cookie_transport = CookieTransport(cookie_name='auth', cookie_max_age=3600)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)