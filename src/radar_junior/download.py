from kaggle.api.kaggle_api_extended import KaggleApi

from radar_junior.config import KAGGLE_DATASET, RAW_DIR, RAW_FILES

api = KaggleApi()
api.authenticate()

for nombre in RAW_FILES:
    ruta = RAW_DIR / nombre
    if ruta.exists():
        print("Ya existe:", ruta)
    else:
        print("Falta:", ruta)
        api.dataset_download_file(KAGGLE_DATASET, nombre, path=RAW_DIR)
