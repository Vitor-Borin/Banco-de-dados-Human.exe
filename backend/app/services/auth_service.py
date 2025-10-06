from passlib.context import CryptContext
from datetime import datetime
from typing import Optional
import logging
from app.database import db
from app.models.usuario import UsuarioLogin, UsuarioResponse

logger = logging.getLogger(__name__)

# Password hashing
# Define bcrypt to não lançar erro ao ultrapassar 72 bytes; trunca silenciosamente
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
    bcrypt__truncate_error=False
)

class AuthService:
    def __init__(self):
        self.pwd_context = pwd_context
    
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """Verify a password against its hash"""
        return self.pwd_context.verify(plain_password, hashed_password)
    
    def get_password_hash(self, password: str) -> str:
        """Hash a password"""
        return self.pwd_context.hash(password)
    
    def authenticate_user(self, email: str, password: str) -> Optional[UsuarioResponse]:
        """Authenticate user with email and password"""
        try:
            # Get user from database
            # A ordem das colunas aqui é importante e deve ser consistente
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
            # Mapeamento de índices:
            # 0: ID_USUARIO, 1: NOME_USUARIO, 2: EMAIL, 3: SENHA_USUARIO
            # 4: APELIDO_STEAM, 5: DATA_CRIACAO, 6: ULTIMO_LOGIN, 7: ID_PERFIL
            
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