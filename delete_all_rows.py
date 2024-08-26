from your_application import create_app, db
from sqlalchemy import text

app = create_app()

with app.app_context():
    # Reflect the database
    meta = db.MetaData()
    meta.reflect(bind=db.engine)

    # Disable foreign key constraints temporarily (specific to SQLite)
    db.session.execute(text("PRAGMA foreign_keys = OFF"))

    # Iterate over all tables and delete all rows
    for table in reversed(meta.sorted_tables):
        db.session.execute(table.delete())
        print(f"All rows deleted from table {table.name}")

    # Re-enable foreign key constraints
    db.session.execute(text("PRAGMA foreign_keys = ON"))

    db.session.commit()
    print("All rows deleted from all tables.")
