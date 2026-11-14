from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="RiskBridge API",
    description="Continuous GRC & Compliance Intelligence Platform",
    version="0.1.0",
)

# Allow Next.js frontend to talk to FastAPI backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {
        "status": "online",
        "service": "RiskBridge GRC Engine",
        "version": "0.1.0"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}
