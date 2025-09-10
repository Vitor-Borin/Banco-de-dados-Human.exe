import oracledb
from config import DATABASE_URL
import logging

logger = logging.getLogger(__name__)

class Database:
    def __init__(self):
        self.connection = None
    
    def get_connection(self):
        """Get database connection"""
        try:
            if self.connection is None:
                self.connection = oracledb.connect(DATABASE_URL)
                logger.info("Database connection established")
            return self.connection
        except Exception as e:
            logger.error(f"Database connection error: {e}")
            raise e
    
    def close_connection(self):
        """Close database connection"""
        if self.connection:
            self.connection.close()
            self.connection = None
            logger.info("Database connection closed")
    
    def execute_query(self, query, params=None):
        """Execute a SELECT query"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute(query, params or {})
            result = cursor.fetchall()
            cursor.close()
            return result
        except Exception as e:
            logger.error(f"Query execution error: {e}")
            raise e
    
    def execute_insert(self, query, params=None):
        """Execute an INSERT query"""
        conn = None
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute(query, params or {})
            conn.commit()
            cursor.close()
            return cursor.rowcount
        except Exception as e:
            logger.error(f"Insert execution error: {e}")
            if conn:
                conn.rollback()
            raise e
    
    def execute_update(self, query, params=None):
        """Execute an UPDATE query"""
        conn = None
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute(query, params or {})
            conn.commit()
            cursor.close()
            return cursor.rowcount
        except Exception as e:
            logger.error(f"Update execution error: {e}")
            if conn:
                conn.rollback()
            raise e
    
    def execute_delete(self, query, params=None):
        """Execute a DELETE query"""
        conn = None
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute(query, params or {})
            conn.commit()
            cursor.close()
            return cursor.rowcount
        except Exception as e:
            logger.error(f"Delete execution error: {e}")
            if conn:
                conn.rollback()
            raise e

# Global database instance
db = Database()
