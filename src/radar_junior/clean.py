import duckdb

from radar_junior.config import RAW_DIR, PROCESSED_DIR

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

antiguas = con.sql("""
    SELECT count(*) FROM jobs
    WHERE source = 'shard' AND first_seen < '2026-01-01'
""").fetchall()[0][0]
print(f"Filas antiguas de shard antes: {antiguas:,}")

con.sql("""
    DELETE FROM jobs
    WHERE source = 'shard' AND first_seen < '2026-01-01'
""")

antiguas = con.sql("""
    SELECT count(*) FROM jobs
    WHERE source = 'shard' AND first_seen < '2026-01-01'
""").fetchall()[0][0]
print(f"Filas antiguas de shard después: {antiguas:,}")

filas = con.sql("SELECT count(*) FROM jobs").fetchall()[0][0]
print(f"Filas que quedan: {filas:,}")

shard_antes = con.sql("SELECT count(*) FROM jobs WHERE source = 'shard'").fetchall()[0][0]
print(f"Filas de shard antes de deduplicar: {shard_antes:,}")

con.sql("""
    CREATE OR REPLACE TABLE jobs AS
    SELECT * FROM jobs WHERE source <> 'shard'
    UNION ALL
    SELECT * EXCLUDE (rn) FROM (
        SELECT *,
               row_number() OVER (PARTITION BY company, title, location
                                  ORDER BY first_seen) AS rn
        FROM jobs
        WHERE source = 'shard'
    )
    WHERE rn = 1
""")

shard_despues = con.sql("SELECT count(*) FROM jobs WHERE source = 'shard'").fetchall()[0][0]
print(f"Filas de shard después de deduplicar: {shard_despues:,}")

filas = con.sql("SELECT count(*) FROM jobs").fetchall()[0][0]
print(f"Filas tras limpiar: {filas:,}")

salida = PROCESSED_DIR / "jobs_clean.parquet"
con.sql(f"COPY jobs TO '{salida}' (FORMAT parquet)")

filas_parquet = con.sql(f"SELECT count(*) FROM read_parquet('{salida}')").fetchall()[0][0]
print(f"Filas en {salida.name}: {filas_parquet:,}")
