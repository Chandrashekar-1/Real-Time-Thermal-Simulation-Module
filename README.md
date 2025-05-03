The project demonstrates a thermal scanner using a regular webcam to provide a simulated object temperature display. The video recording and image processing enable a heat map-like visual representation. It does not measure temperatures but maps pixel intensity values to some specified temperature range, creating a colorful representation of what the heat would look like.

**Key Features:**
Webcam-supported: The webcam on the device records the live video.
Grayscale Conversion: The recorded frames are converted into grayscale and serve as the intensity values of thermal intensity.
Temperature Mapping: The grayscale values are normalized and tested for a temperature range (e.g., 20°C-40°C).
Thermal Color Map: A color map (cv2.COLORMAP_JET) is used for the grayscale image, resulting in an image looked at with thermal vision where color represents the levels of heat.
Simulated temperature reading: Simulated temperature reading is shown right at the middle frame.
Real-time Display: The thermal display is refreshed on a continuous basis, overlaying the simulated temperature on the video feed.
Exit Option: press "q" to quit and terminate the webcam.

**System Configuration:**
- Python 3.x
- cv2 OpenCV library, which you can quickly install with pip install opencv-python.
Procedure:
- Initialize the thermal scanner by running the script.
- Aiming the camera at various objects will enable you to observe the temperature simulation in near real-time.
- Quit with 'q'.

Yet, as it uses a proper simulation, this scanner does not replace real temperatures that a thermal camera would record using its actual sensor.

The camera on the computer is no standard for simulating the actual operation of a thermal imaging camera.

Simulated precision in temperature corresponds to the brightness of the pixel and does not correspond to any actual thermal reading.
