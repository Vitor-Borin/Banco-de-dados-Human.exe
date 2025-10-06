from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging
import uvicorn

from app.controllers.auth_controller import router as auth_router
from app.controllers.usuario_controller import router as usuario_router
from app.controllers.login_controller import router as login_router

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="Game Starter API",
    description="API para sistema de login com auditoria",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://*.vercel.app",  # Permite qualquer subdomínio do Vercel
    "https://banco-de-dados-human-exe-5l9x.vercel.app",  # URL do frontend
    "https://banco-de-dados-human-exe-519x.vercel.app",  # URL alternativa do frontend
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Temporariamente permite todas as origens para debug
    allow_credentials=False,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_router)
app.include_router(usuario_router)
app.include_router(login_router)

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Game Starter API",
        "version": "1.0.0",
        "docs": "/docs"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

@app.get("/test")
async def test_endpoint():
    """Test endpoint"""
    return {"message": "API funcionando!", "cors": "OK"}

# Global exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    # Não captura HTTPException para que o FastAPI possa lidar com elas
    if isinstance(exc, HTTPException):
        raise exc
    
    logger.error(f"Global exception: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"detail": f"Ocorreu um erro interno no servidor: {exc}"}
    )

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )