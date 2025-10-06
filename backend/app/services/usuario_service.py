from typing import List, Optional
import logging
from datetime import datetime
from fastapi import HTTPException, status

from app.database import db
from app.models.usuario import UsuarioCreate, UsuarioUpdate, UsuarioResponse
from app.services.auth_service import auth_service

logger = logging.getLogger(__name__)


class UsuarioService:
    def __init__(self):
        self.auth_service = auth_service

    def create_usuario(self, usuario: UsuarioCreate) -> Optional[UsuarioResponse]:
        """Create a new user"""
        try:
            # Verifica e-mail
            existing_user = self.get_usuario_by_email(usuario.email)
            if existing_user:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Este e-mail já está em uso.",
                )

            # Hash password (truncamento por bytes é feito dentro do auth_service)
            hashed_password = self.auth_service.get_password_hash(usuario.senha_usuario)

            query = """
                INSERT INTO CP01_2S_USUARIO 
                (ID_USUARIO, NOME_USUARIO, EMAIL, SENHA_USUARIO, APELIDO_STEAM, DATA_CRIACAO, ULTIMO_LOGIN, ID_PERFIL)
                VALUES (SEQ_USUARIO.NEXTVAL, :nome_usuario, :email, :senha_usuario, :apelido_steam, :data_criacao, :ultimo_login, :id_perfil)
            """
            params = {
                "nome_usuario": usuario.nome_usuario,
                "email": usuario.email,
                "senha_usuario": hashed_password,
                "apelido_steam": usuario.apelido_steam,
                "data_criacao": datetime.now(),
                "id_perfil": usuario.id_perfil,
                "ultimo_login": datetime.now(),
            }

            db.execute_insert(query, params)

            return self.get_usuario_by_email(usuario.email)

        except HTTPException as http_exc:
            raise http_exc
        except Exception as e:
            logger.error(f"Create user error: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Ocorreu um erro interno ao criar o usuário.",
            )

    def get_usuario_by_id(self, user_id: int) -> Optional[UsuarioResponse]:
        """Get user by ID"""
        try:
            query = """
                SELECT ID_USUARIO, NOME_USUARIO, EMAIL, APELIDO_STEAM, 
                       DATA_CRIACAO, ID_PERFIL, ULTIMO_LOGIN
                FROM CP01_2S_USUARIO 
                WHERE ID_USUARIO = :id_usuario
            """
            result = db.execute_query(query, {"id_usuario": user_id})

            if not result:
                return None

            user_data = result[0]
            return UsuarioResponse(
                id_usuario=user_data[0],
                nome_usuario=user_data[1],
                email=user_data[2],
                apelido_steam=user_data[3],
                data_criacao=user_data[4],
                id_perfil=user_data[5],
                ultimo_login=user_data[6],
            )

        except Exception as e:
            logger.error(f"Get user by ID error: {e}")
            return None

    def get_usuario_by_email(self, email: str) -> Optional[UsuarioResponse]:
        """Get user by email"""
        try:
            query = """
                SELECT ID_USUARIO, NOME_USUARIO, EMAIL, APELIDO_STEAM, 
                       DATA_CRIACAO, ID_PERFIL, ULTIMO_LOGIN
                FROM CP01_2S_USUARIO 
                WHERE EMAIL = :email
            """
            result = db.execute_query(query, {"email": email})

            if not result:
                return None

            user_data = result[0]
            return UsuarioResponse(
                id_usuario=user_data[0],
                nome_usuario=user_data[1],
                email=user_data[2],
                apelido_steam=user_data[3],
                data_criacao=user_data[4],
                id_perfil=user_data[5],
                ultimo_login=user_data[6],
            )

        except Exception as e:
            logger.error(f"Get user by email error: {e}")
            return None

    def get_all_usuarios(self) -> List[UsuarioResponse]:
        """Get all users"""
        try:
            query = """
                SELECT ID_USUARIO, NOME_USUARIO, EMAIL, APELIDO_STEAM, 
                       DATA_CRIACAO, ID_PERFIL, ULTIMO_LOGIN
                FROM CP01_2S_USUARIO
                ORDER BY DATA_CRIACAO DESC
            """
            result = db.execute_query(query)

            usuarios: List[UsuarioResponse] = []
            for user_data in result:
                usuarios.append(
                    UsuarioResponse(
                        id_usuario=user_data[0],
                        nome_usuario=user_data[1],
                        email=user_data[2],
                        apelido_steam=user_data[3],
                        data_criacao=user_data[4],
                        id_perfil=user_data[5],
                        ultimo_login=user_data[6],
                    )
                )

            return usuarios

        except Exception as e:
            logger.error(f"Get all users error: {e}")
            return []

    def update_usuario(self, user_id: int, usuario_update: UsuarioUpdate) -> Optional[UsuarioResponse]:
        """Update user"""
        try:
            update_fields = []
            params = {"id_usuario": user_id}

            if usuario_update.nome_usuario is not None:
                update_fields.append("NOME_USUARIO = :nome_usuario")
                params["nome_usuario"] = usuario_update.nome_usuario

            if usuario_update.email is not None:
                update_fields.append("EMAIL = :email")
                params["email"] = usuario_update.email

            if usuario_update.senha_usuario is not None:
                hashed_password = self.auth_service.get_password_hash(usuario_update.senha_usuario)
                update_fields.append("SENHA_USUARIO = :senha_usuario")
                params["senha_usuario"] = hashed_password

            if usuario_update.apelido_steam is not None:
                update_fields.append("APELIDO_STEAM = :apelido_steam")
                params["apelido_steam"] = usuario_update.apelido_steam

            if usuario_update.id_perfil is not None:
                update_fields.append("ID_PERFIL = :id_perfil")
                params["id_perfil"] = usuario_update.id_perfil

            if not update_fields:
                return self.get_usuario_by_id(user_id)

            query = f"""
                UPDATE CP01_2S_USUARIO 
                SET {', '.join(update_fields)}
                WHERE ID_USUARIO = :id_usuario
            """

            db.execute_update(query, params)
            return self.get_usuario_by_id(user_id)

        except Exception as e:
            logger.error(f"Update user error: {e}")
            return None

    def delete_usuario(self, user_id: int) -> bool:
        """Delete user"""
        try:
            query = "DELETE FROM CP01_2S_USUARIO WHERE ID_USUARIO = :id_usuario"
            result = db.execute_delete(query, {"id_usuario": user_id})
            return result > 0

        except Exception as e:
            logger.error(f"Delete user error: {e}")
            return False


# Global usuario service instance
usuario_service = UsuarioService()