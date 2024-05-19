# Lane Detection Camera

## Descripción General

Este repositorio contiene todos los scripts y archivos necesarios para detectar carriles utilizando una cámara y controlar el movimiento de un motor en función de la curva detectada. Está implementado en Python y utiliza la biblioteca OpenCV para el procesamiento de imágenes.

## Índice

- [Estructura del Repositorio](#estructura-del-repositorio)
- [Pasos para la Detección](#pasos-para-la-detección)
- [Uso](#uso)
- [Notas Adicionales](#notas-adicionales)

## Estructura del Repositorio

1. **`MainRobot.py`**: 
   - Descripción: Archivo principal que inicializa el módulo del motor y llama a la función `camera` para obtener el valor de la curva detectada.
   - Funcionalidad Principal: 
     - Inicializa el motor con los pines correspondientes.
     - Obtiene el valor de la curva detectada por la cámara.
     - Ajusta el movimiento del motor en función del valor de la curva.

2. **`LaneDetectionModule.py`**: 
   - Descripción: Módulo encargado de la detección de carriles mediante el procesamiento de imágenes capturadas por la cámara.
   - Funcionalidad Principal:
     - Procesa los fotogramas de video para detectar carriles.
     - Utiliza funciones de utilidad para umbralizar la imagen, realizar una transformación de perspectiva y calcular histogramas.
     - Calcula el valor de la curva basado en la posición del carril.

3. **`WebcamModule.py`**: 
   - Descripción: Módulo que captura imágenes de la cámara web y las redimensiona.
   - Funcionalidad Principal:
     - Captura imágenes de la cámara web.
     - Redimensiona las imágenes capturadas.
     - Muestra las imágenes capturadas si se especifica.

4. **`ColorPicker.py**`:
   - Descripción: Este script proporciona una interfaz para seleccionar y calibrar colores específicos en la imagen capturada.
   - Funcionalidad Principal:
       - Permite al usuario seleccionar y calibrar colores para mejorar la detección de carriles.
       - Ayuda en el ajuste de parámetros de umbralización basados en colores específicos.
    
5. **`MotorModule.py**`:
   - Descripción: Módulo que controla el motor en función de los comandos recibidos.
   - Funcionalidad Principal:
       - Inicializa los pines del motor.
       - Proporciona funciones para mover el motor hacia adelante, atrás y realizar giros.
       - Ajusta la velocidad y dirección del motor basado en los comandos de control.

6. **`utlis.py**`:
   - Descripción: Módulo de utilidades que contiene varias funciones auxiliares usadas en la detección de carriles.
   - Funcionalidad Principal:
       - Contiene funciones para la umbralización de imágenes (thresholding).
       - Proporciona funciones para la transformación de perspectiva (warpImg).
       - Incluye funciones para calcular histogramas y puntos medios para la detección de carriles.
       -  Maneja la inicialización y actualización de los trackbars usados para calibración.




## Pasos para la Detección

1. **Preparación de Datos**:
   - Asegúrate de que la cámara esté conectada y funcionando correctamente.
   
2. **Inicialización del Sistema**:
   - Ejecuta el script principal `MainRobot.py`:
     ```bash
     python Lane Detection/MainRobot.py
     ```

3. **Captura y Procesamiento de Imágenes**:
   - La cámara capturará imágenes en tiempo real.
   - El módulo `LaneDetectionModule.py` procesará las imágenes para detectar los carriles y calcular la curva.
   
4. **Control del Motor**:
   - Basado en el valor de la curva detectada, el motor ajustará su movimiento para seguir el carril.

## Uso

Para utilizar este repositorio, sigue los pasos en la sección [Pasos para la Detección](#pasos-para-la-detección). Asegúrate de tener Python y OpenCV instalados en tu entorno.

## Notas Adicionales

- Asegúrate de que la cámara esté correctamente configurada y posicionada para capturar el carril de manera óptima.
- Puedes ajustar la sensibilidad y la velocidad máxima del motor modificando los parámetros en el script `MainRobot.py`.
- Si encuentras algún problema o tienes alguna pregunta, no dudes en abrir una issue en el repositorio.

