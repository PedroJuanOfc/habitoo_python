from fastapi import APIRouter, HTTPException, status

from app.auth.schemas import LoginRequest, AuthResponse, Token, UserPublic
from app.core.security import verify_password, create_access_token, hash_password

router = APIRouter()

# Usuário fake em memória (apenas para testes do login)
# Credenciais: email=dev@habitoo.dev  senha=senha123
_FAKE_USERS_BY_EMAIL = {
    "dev@habitoo.dev": {
        "id": "user_1",
        "email": "dev@habitoo.dev",
        "name": "Dev Habitoo",
        # geramos o hash no startup do módulo para não expor a senha em claro
        "password_hash": hash_password("senha123"),
    }
}


@router.post("/login", response_model=AuthResponse, summary="Login com e-mail e senha")
def login(payload: LoginRequest) -> AuthResponse:
    email = payload.email.lower()
    user = _FAKE_USERS_BY_EMAIL.get(email)
    if not user or not verify_password(payload.password, user["password_hash"]):
        # credenciais inválidas → 401
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas",
        )

    # cria JWT com subject=id do usuário e algumas claims úteis
    token_str = create_access_token(
        subject=user["id"],
        extra_claims={"email": user["email"], "name": user["name"]},
    )

    return AuthResponse(
        token=Token(access_token=token_str),
        user=UserPublic(id=user["id"], email=user["email"], name=user["name"]),
    )
