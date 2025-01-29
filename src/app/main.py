# src/app/main.py

from database import init_db, DB_SES_MAKER
from models import RunescapeAccount
import logging

def main():
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        filename='app.log',
        filemode='a',
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    # Initialize the database (create tables if they don't exist)
    init_db()

    # Create a new session
    db = DB_SES_MAKER()

    try:
        # Perform database operations
        account = RunescapeAccount(rsn="5ig",account_type="Regular",tracking=True)
        db.add(account)
        db.commit()
        db.refresh(account)
        logging.info(f"User '{account.rsn}' created with ID {account.id}")
    except Exception as e:
        db.rollback()
        logging.error(f"Error occurred: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    main()