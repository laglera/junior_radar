# 🎯 Radar Junior

> El mercado real del primer empleo: qué sectores y empresas contratan de verdad a perfiles junior, cuántas ofertas "junior" piden 3+ años, cuántas son fantasma y qué skills te faltan.

🚧 **En construcción.** [Ver roadmap](#roadmap)

<!-- Cuando esté desplegado: enlace a la demo + GIF de la app aquí -->

## La pregunta

Buscar el primer trabajo es frustrante: ofertas "junior" que piden 3 años de experiencia, ofertas que llevan abiertas un año y nadie cubre, y no saber qué skills aprender. Este proyecto analiza **más de 11 millones de ofertas reales** de **340.000 empresas** para responder con datos:

1. ¿Qué sectores y empresas contratan de verdad a gente con 0-2 años de experiencia?
2. ¿Cuánto se "infla" el puesto junior?
3. ¿Cuántas ofertas son fantasma, y en qué sectores?
4. ¿Cuánto se cobra según puesto, nivel y skills?
5. Dadas mis skills, ¿qué me falta para el puesto que quiero?

## Hallazgos

_Pendiente (Fase 2)._

## Datos

[Job Listings: Open Jobs in Every Field (Daily)](https://www.kaggle.com/datasets/chandranshbinjola/job-listings), de Chandransh Binjola. Las ofertas se recogen a diario de las páginas de empleo de cada empresa (Workday, Greenhouse, Lever…).

| Fichero | Contenido |
|---|---|
| `jobs.csv` | Una fila por oferta (~11,4M filas, ~2,9 GB) |
| `jobs_by_company.csv` | Una fila por empresa con 5+ ofertas abiertas |
| `open_jobs_daily.csv` | Ofertas abiertas por día |
| `skill_demand_daily.csv` | Demanda diaria de cada skill |

Los datos **no se suben al repositorio**: se descargan con el script de abajo.

## Cómo ejecutarlo

Requisitos: [uv](https://docs.astral.sh/uv/) y una cuenta de [Kaggle](https://www.kaggle.com).

```bash
uv sync                                         # crea el entorno (Python 3.12)
uv run kaggle auth login                        # solo la primera vez
uv run python -m radar_junior.download          # descarga el dataset en data/raw/
```

## Estructura

```
├── app/                 # App de Streamlit (Fase 5)
├── data/
│   ├── raw/             # CSV originales de Kaggle (ignorados por git)
│   └── processed/       # Parquet y agregados (ignorados por git)
├── notebooks/           # Exploración y análisis
├── reports/figures/     # Gráficos exportados
└── src/radar_junior/    # Código reutilizable (descarga, limpieza, modelos)
```

## Stack

DuckDB · Polars · pandas · Plotly · scikit-learn · LightGBM · SHAP · Streamlit

## Roadmap

- [x] **Fase 0:** estructura del proyecto, entorno y script de descarga
- [ ] **Fase 1:** ingesta CSV → Parquet con DuckDB y perfilado de los datos
- [ ] **Fase 2:** análisis exploratorio con conclusiones
- [ ] **Fase 3:** modelo de salario (Pipeline + LightGBM + SHAP)
- [ ] **Fase 4:** skill gap
- [ ] **Fase 5:** app en Streamlit y despliegue
- [ ] **Fase 6:** presentación final

## Limitaciones

_Pendiente: sesgo de salarios publicados (sobre todo EE. UU.), monedas mezcladas, campos inferidos por reglas (nivel, sector, `ghost_score`)._
