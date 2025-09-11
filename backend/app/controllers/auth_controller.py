from fastapi import APIRouter, HTTPException, status, Request
from typing import Optional
import logging

from app.models.auth import LoginRequest, LoginResponse
from app.models.usuario import UsuarioResponse
from app.services.auth_service import auth_service
from app.services.usuario_service import usuario_service
from app.services.login_service import login_service
from app.models.login import LoginCreate

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/login", response_model=LoginResponse)
async def login(request: Request, login_data: LoginRequest):
    """Authenticate user with email and password"""
    try:
        # Authenticate user
        user = auth_service.authenticate_user(login_data.email, login_data.password)
        if not user:
            return LoginResponse(
                success=False,
                message="Email ou senha incorretos"
            )
        
        # Log login attempt for audit
        client_ip = request.client.host
        user_agent = request.headers.get("user-agent", "")
        
        login_record = LoginCreate(
            ip_login=client_ip,
            user_agent=user_agent,
            id_usuario=user.id_usuario
        )
        login_service.create_login_record(login_record)
        
        # Update last login timestamp
        auth_service.update_last_login(user.id_usuario)
        
        return LoginResponse(
            success=True,
            message="Login realizado com sucesso",
            user_id=user.id_usuario,
            user_name=user.nome_usuario
        )
        
    except Exception as e:
        logger.error(f"Login error: {e}")
        return LoginResponse(
            success=False,
            message="Erro interno do servidor"
        )

@router.post("/verify", response_model=LoginResponse)
async def verify_user(request: Request, login_data: LoginRequest):
    """Verify user credentials without logging in"""
    try:
        user = auth_service.authenticate_user(login_data.email, login_data.password)
        if not user:
            return LoginResponse(
                success=False,
                message="Email ou senha incorretos"
            )
        
        return LoginResponse(
            success=True,
            message="Credenciais válidas",
            user_id=user.id_usuario,
            user_name=user.nome_usuario
        )
        
    except Exception as e:
        logger.error(f"Verify user error: {e}")
        return LoginResponse(
            success=False,
            message="Erro interno do servidor"
        )
