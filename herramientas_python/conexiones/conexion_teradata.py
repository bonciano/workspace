from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base, DeferredReflection
from sqlalchemy.orm import scoped_session, sessionmaker

[...]

# Connect
engine = create_engine('teradata://' + user + ':' + password + '@' + host + ':22/' + database)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
db_session.execute('SET SESSION CHARACTERISTICS AS TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;')  # To avoid locking tables when doing select on tables
db_session.commit()

Base = declarative_base(cls=DeferredReflection)
Base.query = db_session.query_property()