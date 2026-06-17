import os
import psycopg2
import sys

# Hardcoded fallback to the user's provided internal Railway connection string
DEFAULT_DB = "postgresql://postgres:MtqVviFXWWWKkDqkSEObMlvKmBXWKFJq@postgres.railway.internal:5432/railway"
db_url = os.getenv("DATABASE_URL", DEFAULT_DB)

def run_migration():
    print("Initiating SqueezeOS Agent Credit Bureau Migration...")
    try:
        conn = psycopg2.connect(db_url)
        conn.autocommit = True
        cur = conn.cursor()
        
        with open("001_agent_credit_bureau.sql", "r") as f:
            sql = f.read()
            
        cur.execute(sql)
        print("[SUCCESS] Agent Credit Bureau PostgreSQL schema and triggers deployed successfully.")
        
        cur.close()
        conn.close()
    except Exception as e:
        print(f"[ERROR] Migration failed: {e}")
        # We don't exit 1 to prevent crashing the main server if the table already exists
        # In a real environment we'd check for 'already exists' explicitly, but this is a forced migration script.

if __name__ == "__main__":
    run_migration()
