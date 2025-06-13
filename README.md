# Deivid-POO-Python
# 🍽️ Simulador de Restaurantes en un Centro Comercial - Aplicación de Escritorio en Python

## 📌 Objetivo General

Desarrollar una aplicación de escritorio con una interfaz gráfica interactiva utilizando **Python** y **Tkinter**, que simule la experiencia de escoger un restaurante dentro de un centro comercial, permitiendo realizar pedidos desde un menú específico y registrar las opiniones de los clientes. Además, la aplicación incluye un sistema de **análisis de sentimientos** utilizando **TextBlob**, para clasificar las valoraciones como positivas, negativas o neutras, mejorando así la comprensión del nivel de satisfacción del usuario.

---

## 🎯 Objetivos Específicos

- 🖥️ Construir una interfaz gráfica **intuitiva y accesible**, que permita:
  - Seleccionar restaurantes.
  - Visualizar menús.
  - Realizar pedidos.
  - Compartir opiniones al finalizar la experiencia.

- 🧱 Estructurar el sistema aplicando **programación orientada a objetos (POO)**:
  - Cada restaurante es una subclase que hereda de una clase base `Restaurante`.

- 🛒 Implementar una funcionalidad para **gestión de pedidos**:
  - Selección de platillos.
  - Indicación de cantidad.
  - Resumen del pedido con costo total antes de confirmar.

- 💬 Incorporar una opción para que los clientes **dejen comentarios**:
  - Asociar opiniones con su restaurante correspondiente.
  - Almacenar los datos para análisis posterior.

- 🤖 Integrar análisis de sentimientos con **TextBlob**:
  - Traducir comentarios al inglés si es necesario.
  - Clasificar opiniones como **positivas**, **negativas** o **neutras**.

- 📊 Registrar y mostrar un **resumen de opiniones**:
  - Ofrecer una vista general de la satisfacción por restaurante.

- 🎮 Recrear digitalmente la experiencia típica de atención al cliente en un entorno de **comida rápida**.

---

## 📚 Diagrama de Clases (Descripción)

### 🏛️ Clase Padre: `Restaurante`

Define la estructura común para todos los restaurantes.

**Atributos:**
- `nombre`: Nombre del restaurante.
- `categoria`: Tipo de comida (ej. "Comida rápida", "Pizzería").
- `horario`: Horario de atención.
- `menu`: Diccionario con platillos y sus precios.

> La clase `Restaurante` funciona como plantilla base general.

---

### 🍔 Clases Hijas:

- `BurgerKing`
- `McDonalds`
- `PizzaHut`
- `SalvatorePizza`

**Características:**
- Heredan de la clase `Restaurante`.
- Usan `super().__init__` para definir:
  - Nombre propio.
  - Categoría.
  - Horario.
  - Menú específico.
- No redefinen métodos de la clase padre.
- Permiten reutilizar código y aplicar fácilmente cambios estructurales globales.

---

## 🛠️ Tecnologías Utilizadas

- **Python 3.x**
- **Tkinter** (Interfaz gráfica)
- **TextBlob** (Análisis de sentimientos)
- **Googletrans** (Traducción automática si es necesario)

---
