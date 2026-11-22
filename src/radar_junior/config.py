from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
FIGURES_DIR = ROOT / "reports" / "figures"

KAGGLE_DATASET = "chandranshbinjola/job-listings"

RAW_FILES = (
    "jobs.csv",
    "jobs_by_company.csv",
    "open_jobs_daily.csv",
    "skill_demand_daily.csv",
)
