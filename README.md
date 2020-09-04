# EEGPlotter
A GUI tool to visualise biosignals sent from microcontroller over serial port.

## Requirements
| Name                                                        | Version  |
|:------------------------------------------------------------|----------|
| [Python](https://www.python.org/)                           | 3.x.x    |
| [Numpy](https://github.com/numpy/numpy)                     | 1.19.1   |
| [PyQt5](https://riverbankcomputing.com/software/pyqt/intro) | 5.15.0   |
| [PyQtGraph](https://github.com/pyqtgraph/pyqtgraph)         | 0.11.0   |
| [pySerial](https://github.com/pyserial/pyserial)            | 3.4      |
| [SciPy](https://github.com/scipy/scipy)                     | 1.5.2    |

## Instructions
1. Clone this repo:
  `git clone https://github.com/a1varo-costa/EEGPlotter.git`

2. Inside the cloned 'EEGPlotter' directory create a new [Python virtual environment](https://docs.python.org/3/tutorial/venv.html) and **activate it**:
    - MacOS/Linux 
    ```bash
    cd EEGPlotter/
    python3 -m venv venv
    source venv/bin/activate
    ```
    - Windows
    ```cmd
    cd EEGPlotter\
    python -m venv venv
    venv\Scripts\activate.bat
    ```
3. Install requirements:
    ```
    pip install -r requirements.txt
    ```
4. Edit [main.py](./main.py):
    - Select the serial port: COM3, COM4, ... (Windows) | /dev/ttyUSB0 (Linux), for example
    - Select the sampling frequency (Hz)

5. Run [main.py](./main.py):
    ```
    python3 main.py
    ```

## Licence
See [LICENCE](LICENSE)
