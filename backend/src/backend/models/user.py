import uuid
from datetime import datetime , timezone

from sqlalchemy import DateTime , ForeignKey , String , Uuid
from sqlalchemy.orm import Mapped , mapped_column

from backend.core.database import Base


class User(Base):
    __tablename__ = "users"
    
    # Neon Auth ka User ID (JWT ke "sub" claim se aayega , e.g. "user_2abc123")
    id : Mapped[str] = mapped_column(
        String(255) ,
        primary_key=True , 
    )
    
    # here user ka email le raha hu
    email: Mapped[str] = mapped_column(
        String(255) ,
        unique=True ,
        index=True ,
        nullable=False ,
    )
    
    #Foreign Key : Yeh kis Organisation ka hissa hai
    organization_id : Mapped[uuid.UUID] = mapped_column(
        Uuid ,
        ForeignKey("organizations.id" , ondelete="CASCADE") ,
        nullable=False
    )
    
    #RBAC Ka Storage
    role : Mapped[str] = mapped_column (
        String(50) ,
        default="analyst",
        nullable=False,
    )
    
    #User creation Timestamp (UTC) ---> matlab kabh user create hua tha
    created_at : Mapped[datetime] = mapped_column(
        DateTime(timezone=True) ,
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )