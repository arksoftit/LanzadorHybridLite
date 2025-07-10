# MultiLanzadorHB - HybridLite

Selector universal de empresas y módulos para sistemas HybridLite.

## Funcionalidades

- Selecciona la empresa a ejecutar.
- Selecciona entre los módulos disponibles:
  - Módulo Administrativo
  - Módulo de Facturación
- Lanza el `.exe` correspondiente desde su propia carpeta, asegurando el acceso a archivos `.ini`, bases de datos, reportes, etc.

## Requisitos

- Python 3.10+  
- Librerías: Ninguna (usa solo módulos estándar)

## Cómo usarlo

1. Configura las empresas en `empresas.json`.
2. Ejecuta:
   ```bash
   python MultiLanzadorHB.py# LanzadorHybridLite