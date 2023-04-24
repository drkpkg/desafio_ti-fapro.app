# Reto técnico para FAPRO

## Descripción

Este proyecto consiste en un crawler para obtener información de la Unidad de fomento https://www.sii.cl/valores_y_fechas/uf/uf2023.htm

Esta desarrollado en python con FastAPI, usa beautifulsoup para obtener la información y sirve como api rest.

## Instalación

### Ejecución en local

```shell
pip install -r requirements.txt
python main.py
```

### Ejecución con docker

```shell
docker build -t fapro:lastest .
docker run -d -p 8000:80 -d fapro:lastest 
```

