# Division Service API

API REST para realizar divisiones de dos números no negativos en base 10.

## 📋 Requisitos

- Python 3.8+
- pip
- Postman (para pruebas manuales)

## 🚀 Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/udistrital23/divisionservice.git
cd divisionservice
```

2. **Crear entorno virtual (opcional pero recomendado)**
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

## ▶️ Ejecutar la aplicación

```bash
uvicorn app.main:app --reload
```

La API estará disponible en `http://localhost:8000`

### Documentación interactiva
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 📝 Endpoints

### POST /division

Realiza la división entera de dos números no negativos.

**URL**: `http://localhost:8000/division`

**Método**: `POST`

**Headers requeridos**:
```
Content-Type: application/json
```

**Body (JSON)**:
```json
{
  "numero_a": 10,
  "numero_b": 5
}
```

**Respuesta exitosa (200 OK)**:
```json
{
  "resultado": 2
}
```

## 🧪 Pruebas en Postman

### 1. División exitosa

- **Método**: POST
- **URL**: `http://localhost:8000/division`
- **Body (raw, JSON)**:
  ```json
  {
    "numero_a": 10,
    "numero_b": 5
  }
  ```
- **Resultado esperado**: `{"resultado": 2}`

### 2. División por cero

- **Método**: POST
- **URL**: `http://localhost:8000/division`
- **Body (raw, JSON)**:
  ```json
  {
    "numero_a": 10,
    "numero_b": 0
  }
  ```
- **Resultado esperado**: Error 400 - "No se puede dividir por cero"

### 3. Dividendo negativo

- **Método**: POST
- **URL**: `http://localhost:8000/division`
- **Body (raw, JSON)**:
  ```json
  {
    "numero_a": -10,
    "numero_b": 5
  }
  ```
- **Resultado esperado**: Error 400 - "Los numeros deben ser positivos"

### 4. Divisor negativo

- **Método**: POST
- **URL**: `http://localhost:8000/division`
- **Body (raw, JSON)**:
  ```json
  {
    "numero_a": 10,
    "numero_b": -5
  }
  ```
- **Resultado esperado**: Error 400 - "Los numeros deben ser positivos"

### 5. Más ejemplos de divisiones

**División con resultado decimal (truncado)**:
```json
{
  "numero_a": 10,
  "numero_b": 3
}
```
Resultado esperado: `{"resultado": 3}`

**División con cero como dividendo**:
```json
{
  "numero_a": 0,
  "numero_b": 5
}
```
Resultado esperado: `{"resultado": 0}`

## 🧬 Pruebas unitarias

Ejecutar todas las pruebas:
```bash
pytest tests/
```

Ejecutar con cobertura:
```bash
pytest tests/ --cov=app
```

Ejecutar tests específicos:
```bash
pytest tests/test_validator.py -v
```

## 🥒 Pruebas BDD con Behave

Ejecutar escenarios:
```bash
behave
```

Ejecutar con verbosidad:
```bash
behave -v
```

## 📁 Estructura del proyecto

```
divisionservice/
├── app/
│   ├── __init__.py
│   ├── main.py           # Aplicación FastAPI
│   └── validator.py      # Lógica de división
├── features/
│   ├── validacion.feature # Escenarios BDD en español
│   ├── environment.py    # Configuración Behave
│   └── steps/
│       └── steps.py      # Implementación de pasos
├── tests/
│   ├── test_validator.py # Tests unitarios
│   └── __pycache__/
├── Dockerfile            # Configuración Docker
├── Makefile             # Comandos útiles
├── requirements.txt     # Dependencias Python
└── README.md            # Este archivo
```

## 🐳 Ejecutar con Docker

```bash
docker build -t divisionservice .
docker run -p 8000:8000 divisionservice
```

## 📦 Dependencias

Ver `requirements.txt` para la lista completa de dependencias.

## 🔧 Hacer cambios

1. Modificar el código
2. Ejecutar pruebas: `pytest` y `behave`
3. Commit y push

## 📄 Licencia

Este proyecto es parte del curso de Maestría en Ingeniería de Software.

## 👨‍💻 Autor

Maximiliano Valencia Medina
