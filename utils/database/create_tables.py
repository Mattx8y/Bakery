from utils.database import sqlite as db


class Accounts(db.Table):
    user_id = db.Column("BIGINT", nullable=False, primary_key=True)
    profile_name = db.Column("USERNAME", nullable=False)


def creation(debug: bool = False):
    failed = False

    for table in db.Table.all_tables():
        try:
            table.create()
        except Exception as e:
            print(f'Could not create {table.__tablename__}.\n\nError: {e}')
            failed = True
        else:
            if debug:
                print(f'[{table.__module__}] Created {table.__tablename__}.')


    return True if not failed else False
