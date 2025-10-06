from passlib.context import CryptContext
from datetime import datetime
from typing import Optional
import logging

from app.database import db
from app.models.usuario import UsuarioLogin, UsuarioResponse

logger = logging.getLogger(__name__)

# Password hashing (bcrypt)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def _normalize_password_bytes(pwd: str) -> str:
    """
    Trunca a senha com base em BYTES (limite do bcrypt é 72 bytes).
    Converte para utf-8, corta em 72 bytes e volta para str, ignorando
    qualquer byte parcial final.
    """
    if pwd is None:
        return ""
    b = pwd.encode("utf-8")[:72]
    return b.decode("utf-8", errors="ignore")


class AuthService:
    def __init__(self):
        self.pwd_context = pwd_context

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """Verify a password against its hash, handling invalid formats or long inputs."""
        try:
            if not plain_password or not hashed_password:
                return False

            normalized = _normalize_password_bytes(plain_password)

            # Se o hash não parecer bcrypt, não tente verificar
            if not str(hashed_password).startswith("$2"):
                logger.warning(
                    "Hash com formato inválido (não-bcrypt) detectado ao verificar senha."
                )
                return False

            # Logs úteis (não expõe a senha)
            try:
                logger.info(
                    f"[AUTH] Verifying password | len_chars={len(plain_password)} "
                    f"| len_bytes={len(plain_password.encode('utf-8'))} "
                    f"| len_bytes_trunc={len(normalized.encode('utf-8'))}"
                )
            except Exception:
                pass

            return self.pwd_context.verify(normalized, hashed_password)

        except Exception as e:
            logger.error(f"Erro ao verificar senha: {e}")
            return False

    def get_password_hash(self, password: str) -> str:
        """Hash a password safely (truncate by bytes before bcrypt)."""
        try:
            normalized = _normalize_password_bytes(password)

            # Logs úteis (não expõe a senha)
            try:
                logger.info(
                    f"[AUTH] Hashing password | len_chars={len(password) if password else 0} "
                    f"| len_bytes={len(password.encode('utf-8')) if password else 0} "
                    f"| len_bytes_trunc={len(normalized.encode('utf-8'))}"
                )
            except Exception:
                pass

            return self.pwd_context.hash(normalized)
        except Exception as e:
            logger.error(f"Erro ao gerar hash de senha: {e}")
            raise

    def authenticate_user(self, email: str, password: str) -> Optional[UsuarioResponse]:
        """Authenticate user with email and password"""
        try:
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

            if not self.verify_password(password, stored_password):
                return None

            user = UsuarioResponse(
                id_usuario=user_data[0],
                nome_usuario=user_data[1],
                email=user_data[2],
                apelido_steam=user_data[4],
                data_criacao=user_data[5],
                ultimo_login=user_data[6],
                id_perfil=user_data[7],
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
            params = {"ultimo_login": datetime.now(), "id_usuario": user_id}
            db.execute_update(query, params)
            return True
        except Exception as e:
            logger.error(f"Update last login error: {e}")
            return False


# Global auth service instance
auth_service = AuthService()