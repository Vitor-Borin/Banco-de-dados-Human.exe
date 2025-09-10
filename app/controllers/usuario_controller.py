from fastapi import APIRouter, HTTPException, status
from typing import List
import logging

from app.models.usuario import Usuario, UsuarioCreate, UsuarioUpdate, UsuarioResponse
from app.services.usuario_service import usuario_service

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/usuarios", tags=["Users"])

@router.post("/", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
async def create_usuario(usuario: UsuarioCreate):
    """Create a new user"""
    try:
        # Check if user already exists
        existing_user = usuario_service.get_usuario_by_email(usuario.email)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
        
        new_usuario = usuario_service.create_usuario(usuario)
        if not new_usuario:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to create user"
            )
        
        return new_usuario
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Create user error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )

@router.get("/", response_model=List[UsuarioResponse])
async def get_all_usuarios():
    """Get all users"""
    try:
        usuarios = usuario_service.get_all_usuarios()
        return usuarios
        
    except Exception as e:
        logger.error(f"Get all users error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )

@router.get("/{user_id}", response_model=UsuarioResponse)
async def get_usuario(user_id: int):
    """Get user by ID"""
    try:
        usuario = usuario_service.get_usuario_by_id(user_id)
        if not usuario:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        
        return usuario
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Get user error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )

@router.put("/{user_id}", response_model=UsuarioResponse)
async def update_usuario(user_id: int, usuario_update: UsuarioUpdate):
    """Update user"""
    try:
        # Check if user exists
        existing_usuario = usuario_service.get_usuario_by_id(user_id)
        if not existing_usuario:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        
        # Check if email is being changed and if it already exists
        if usuario_update.email and usuario_update.email != existing_usuario.email:
            email_exists = usuario_service.get_usuario_by_email(usuario_update.email)
            if email_exists:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Email already registered"
                )
        
        updated_usuario = usuario_service.update_usuario(user_id, usuario_update)
        if not updated_usuario:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to update user"
            )
        
        return updated_usuario
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Update user error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )

@router.delete("/{user_id}")
async def delete_usuario(user_id: int):
    """Delete user"""
    try:
        # Check if user exists
        existing_usuario = usuario_service.get_usuario_by_id(user_id)
        if not existing_usuario:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        
        success = usuario_service.delete_usuario(user_id)
        if not success:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to delete user"
            )
        
        return {"message": "User deleted successfully"}
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Delete user error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )
