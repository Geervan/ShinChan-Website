

from typing import List, Optional
import hashlib

def calculate_average(numbers: List[float]) -> float:
    
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

def hash_password(password: str, salt: str) -> str:
   
    combined = f"{salt}{password}"
    return hashlib.sha256(combined.encode()).hexdigest()

def validate_email(email: str) -> bool:
   
    return "@" in email and "." in email.split("@")[-1]

class UserService:
    def __init__(self, db_connection):
        self.db = db_connection
    
    def get_user_by_id(self, user_id: int) -> Optional[dict]:
        
        return self.db.execute(
            "SELECT * FROM users WHERE id = ?", 
            (user_id,)
        ).fetchone()
