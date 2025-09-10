from typing import List, Optional
import logging
from app.database import db
from app.models.login import Login, LoginCreate, LoginResponse

logger = logging.getLogger(__name__)

class LoginService:
    def __init__(self):
        pass
    
    def create_login_record(self, login: LoginCreate) -> Optional[LoginResponse]:
        """Create a new login record for audit"""
        try:
            query = """
                INSERT INTO CP01_2S_LOGIN (IP_LOGIN, USER_AGENT, DATA_LOGIN, ID_USUARIO)
                VALUES (:ip_login, :user_agent, :data_login, :id_usuario)
            """
            params = {
                "ip_login": login.ip_login,
                "user_agent": login.user_agent,
                "data_login": login.data_login,
                "id_usuario": login.id_usuario
            }
            
            db.execute_insert(query, params)
            
            # Get the created login record
            return self.get_latest_login_by_user(login.id_usuario)
            
        except Exception as e:
            logger.error(f"Create login record error: {e}")
            return None
    
    def get_login_by_id(self, login_id: int) -> Optional[LoginResponse]:
        """Get login record by ID"""
        try:
            query = """
                SELECT ID_LOGIN, IP_LOGIN, USER_AGENT, DATA_LOGIN, ID_USUARIO
                FROM CP01_2S_LOGIN 
                WHERE ID_LOGIN = :id_login
            """
            result = db.execute_query(query, {"id_login": login_id})
            
            if not result:
                return None
            
            login_data = result[0]
            return LoginResponse(
                id_login=login_data[0],
                ip_login=login_data[1],
                user_agent=login_data[2],
                data_login=login_data[3],
                id_usuario=login_data[4]
            )
            
        except Exception as e:
            logger.error(f"Get login by ID error: {e}")
            return None
    
    def get_logins_by_user(self, user_id: int) -> List[LoginResponse]:
        """Get all login records for a specific user"""
        try:
            query = """
                SELECT ID_LOGIN, IP_LOGIN, USER_AGENT, DATA_LOGIN, ID_USUARIO
                FROM CP01_2S_LOGIN 
                WHERE ID_USUARIO = :id_usuario
                ORDER BY DATA_LOGIN DESC
            """
            result = db.execute_query(query, {"id_usuario": user_id})
            
            logins = []
            for login_data in result:
                logins.append(LoginResponse(
                    id_login=login_data[0],
                    ip_login=login_data[1],
                    user_agent=login_data[2],
                    data_login=login_data[3],
                    id_usuario=login_data[4]
                ))
            
            return logins
            
        except Exception as e:
            logger.error(f"Get logins by user error: {e}")
            return []
    
    def get_latest_login_by_user(self, user_id: int) -> Optional[LoginResponse]:
        """Get the latest login record for a specific user"""
        try:
            query = """
                SELECT ID_LOGIN, IP_LOGIN, USER_AGENT, DATA_LOGIN, ID_USUARIO
                FROM CP01_2S_LOGIN 
                WHERE ID_USUARIO = :id_usuario
                ORDER BY DATA_LOGIN DESC
                FETCH FIRST 1 ROWS ONLY
            """
            result = db.execute_query(query, {"id_usuario": user_id})
            
            if not result:
                return None
            
            login_data = result[0]
            return LoginResponse(
                id_login=login_data[0],
                ip_login=login_data[1],
                user_agent=login_data[2],
                data_login=login_data[3],
                id_usuario=login_data[4]
            )
            
        except Exception as e:
            logger.error(f"Get latest login by user error: {e}")
            return None
    
    def get_all_logins(self) -> List[LoginResponse]:
        """Get all login records"""
        try:
            query = """
                SELECT ID_LOGIN, IP_LOGIN, USER_AGENT, DATA_LOGIN, ID_USUARIO
                FROM CP01_2S_LOGIN
                ORDER BY DATA_LOGIN DESC
            """
            result = db.execute_query(query)
            
            logins = []
            for login_data in result:
                logins.append(LoginResponse(
                    id_login=login_data[0],
                    ip_login=login_data[1],
                    user_agent=login_data[2],
                    data_login=login_data[3],
                    id_usuario=login_data[4]
                ))
            
            return logins
            
        except Exception as e:
            logger.error(f"Get all logins error: {e}")
            return []

# Global login service instance
login_service = LoginService()
