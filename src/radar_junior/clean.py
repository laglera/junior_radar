from radar_junior.config import RAW_DIR, PROCESSED_DIR
import duckdb

con = duckdb.connect()

con.sql(f"""
    CREATE OR REPLACE TABLE jobs AS
    SELECT * FROM read_csv('{RAW_DIR / 'jobs.csv'}', types = {{'posted': 'VARCHAR'}})
""")

filas = con.sql("SELECT count(*) FROM jobs").fetchall()[0][0]
print(f"Filas leídas: {filas:,}")

con_18 = con.sql("SELECT count(*) FROM jobs WHERE years_experience = 18").fetchall()[0][0]
print(f"Filas con 18 antes: {con_18:,}")
con_nan = con.sql("SELECT count(*) FROM jobs WHERE location = 'Nan, Nan, Nan'").fetchall()[0][0]
print(f"Filas con Nan antes: {con_nan:,}")

con.sql("""
    UPDATE jobs
    SET years_experience = NULL
    WHERE years_experience = 18
""")

con.sql("""
    UPDATE jobs
    SET location = NULL
    WHERE location = 'Nan, Nan, Nan'
""")

con_18 = con.sql("SELECT count(*) FROM jobs WHERE years_experience = 18").fetchall()[0][0]
print(f"Filas con 18 después: {con_18:,}")
con_nan = con.sql("SELECT count(*) FROM jobs WHERE location = 'Nan, Nan, Nan'").fetchall()[0][0]
print(f"Filas con Nan después: {con_nan:,}")
