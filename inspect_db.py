from app import create_app, db  # Replace 'your_flask_app' with the actual name of your app's package
from sqlalchemy import inspect

# Create an instance of your Flask app
app = create_app()  # Ensure that this creates an app instance with the correct configuration

# Use the app context to access the database
with app.app_context():
    # Inspect the database
    inspector = inspect(db.engine)
    
    # Get table names
    tables = inspector.get_table_names()
    
    # Print table names
    print("Tables in the database:")
    for table in tables:
        print(f"- {table}")
