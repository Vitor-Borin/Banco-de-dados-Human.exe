from fastapi import APIRouter, HTTPException, status
from typing import List
import logging

from app.models.login import LoginResponse
from app.services.login_service import login_service

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/logins", tags=["Login Audit"])

@router.get("/", response_model=List[LoginResponse])
async def get_all_logins():
    """Get all login records"""
    try:
        logins = login_service.get_all_logins()
        return logins
        
    except Exception as e:
        logger.error(f"Get all logins error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )

@router.get("/{login_id}", response_model=LoginResponse)
async def get_login(login_id: int):
    """Get login record by ID"""
    try:
        login = login_service.get_login_by_id(login_id)
        if not login:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Login record not found"
            )
        
        return login
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Get login error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )

@router.get("/user/{user_id}", response_model=List[LoginResponse])
async def get_user_logins(user_id: int):
    """Get all login records for a specific user"""
    try:
        logins = login_service.get_logins_by_user(user_id)
        return logins
        
    except Exception as e:
        logger.error(f"Get user logins error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )
