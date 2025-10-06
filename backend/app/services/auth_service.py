from passlib.context import CryptContext
from datetime import datetime
from typing import Optional
import logging
from app.database import db
from app.models.usuario import UsuarioLogin, UsuarioResponse

logger = logging.getLogger(__name__)

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthService:
    def __init__(self):
        self.pwd_context = pwd_context

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """Verify a password against its hash, handling invalid formats or long inputs"""
        try:
            # Garante que a senha tenha no máximo 72 bytes (limite do bcrypt)
            if plain_password:
                plain_password = plain_password.strip()[:72]
            else:
                return False

            # Verifica se o hash é válido (bcrypt começa com $2)
            if not hashed_password or not str(hashed_password).startswith("$2"):
                logger.warning(f"Hash de senha inválido detectado: {hashed_password[:20]}...")
                return False

            return self.pwd_context.verify(plain_password, hashed_password)

        except Exception as e:
            logger.error(f"Erro ao verificar senha: {e}")
            return False

    def get_password_hash(self, password: str) -> str:
        """Hash a password safely"""
        try:
            if password:
                password = password.strip()[:72]  # Limita comprimento antes de hashear
            return self.pwd_context.hash(password)
        except Exception as e:
            logger.error(f"Erro ao gerar hash de senha: {e}")
            raise

    def authenticate_user(self, email: str, password: str) -> Optional[UsuarioResponse]:
        """Authenticate user with email and password"""
        try:
            # Get user from database
            query = """
                SELECT ID_USUARIO, NOME_USUARIO, EMAIL, SENHA_USUARIO, 
                       APELIDO_STEAM, DATA_CRIACAO, ULTIMO_LOGIN, ID_PERFIL
                FROM CP01_2S_USUARIO 
                WHERE EMAIL = :email
            """
            result = db.execute_query(query, {"email": email})
            
            if not result:
                return None
            
            user_data = result[0]
            stored_password = user_data[3]

            # Verify password
            if not self.verify_password(password, stored_password):
                return None
            
            # Return user without password
            user = UsuarioResponse(
                id_usuario=user_data[0],
                nome_usuario=user_data[1],
                email=user_data[2],
                apelido_steam=user_data[4],
                data_criacao=user_data[5],
                ultimo_login=user_data[6],
                id_perfil=user_data[7]
            )
            
            return user
            
        except Exception as e:
            logger.error(f"Authentication error: {e}")
            return None

    def update_last_login(self, user_id: int) -> bool:
        """Update user's last login timestamp"""
        try:
            query = """
                UPDATE CP01_2S_USUARIO 
                SET ULTIMO_LOGIN = :ultimo_login 
                WHERE ID_USUARIO = :id_usuario
            """
            params = {
                "ultimo_login": datetime.now(),
                "id_usuario": user_id
            }
            db.execute_update(query, params)
            return True
        except Exception as e:
            logger.error(f"Update last login error: {e}")
            return False

# Global auth service instance
auth_service = AuthService()
