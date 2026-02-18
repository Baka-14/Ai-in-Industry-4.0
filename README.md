# AI in Industry (AI4104)

A collection of assignments from the **AI in Industry * course, covering IoT (Raspberry Pi + sensors + Firebase), real-time communication (Socket.IO), CPU scheduling, computer vision (YOLO, ResNet), time-series forecasting (SARIMA), and predictive maintenance (NASA RUL). Each section below describes what was done, the tech stack used, and how to run it.

---


## Repository structure

```
.
├── README.md
├── Raspi/                          # Raspberry Pi + sensor + Firebase
├── week-1/
│   ├── Assignment-1/               # Server–client with Socket.IO
│   │   ├── server-with-ui/         # Flask + web UI
│   │   └── server-client-cli/      # Flask server + Python client (no UI)
│   └── Assignment-2/               # YOLO object detection
├── week-2/                         # CPU process scheduling (FCFS, SJF, PS, RR)
│   └── README.md
└── week-3/                         # ML: SARIMA, ResNet, NASA RUL, Darknet notes
    └── NasaRULData/                # NASA C-MAPSS dataset (FD001)
```

---

## Assignments overview

### Raspi — Ultrasonic sensor + Firebase

**What we did:**
Integrated a **HC-SR04 ultrasonic distance sensor** with a **Raspberry Pi**. The Pi measures distance in real time and pushes each reading (with timestamp) to a **Firebase Realtime Database** under a `Status` node for monitoring or dashboards.

**Tech stack / things used**

- **Hardware:** Raspberry Pi, HC-SR04 (TRIG on GPIO 18, ECHO on GPIO 24)
- **Language:** Python 3
- **Libraries:** `RPi.GPIO`, `pyrebase`
- **Backend:** Firebase (Realtime Database)

**How to run**

```bash
cd Raspi
python3 main.py
```

Configure your Firebase project and set the config in `main.py` (apiKey, authDomain, databaseURL, etc.) before running.

---

### Week 1 — Assignment 1: Server–client with Socket.IO

**What we did:** Built a **real-time client–server** setup using **Socket.IO** in two variants:

1. **With UI:** A Flask app serving an HTML page; the browser connects via Socket.IO and sends/receives messages; the server echoes back a response.
2. **Without UI:** A Flask Socket.IO server and a **Python** client that connects, sends one message, receives the server response, then disconnects.

**Tech stack / things used**

- **Backend:** Python, Flask, Flask-SocketIO
- **Client (with UI):** HTML, JavaScript, Socket.IO (CDN)
- **Client (no UI):** Python, `python-socketio` (client)

**How to run**

- **Server with web UI:** From `week-1/Assignment-1/server-with-ui/` run `python app.py`, then open the URL shown (e.g. `http://127.0.0.1:5000`) and use the input/button to send messages.
- **Server + Python client (no UI):** Start the server from `week-1/Assignment-1/server-client-cli/` with `python server.py` (listens on port 8888). In another terminal, run `python client.py` and enter a message when prompted.

---

### Week 1 — Assignment 2: YOLO object detection

**What we did:**
Used **YOLO** (YOLOv4 config and weights) with **OpenCV** in a Jupyter notebook (e.g. on Google Colab) to run **object detection** on images. The pipeline loads a pre-trained YOLO model and draws bounding boxes and labels for detected objects (e.g. COCO classes).

**Tech stack / things used**

- **Environment:** Google Colab (optional), Jupyter
- **Language:** Python
- **Libraries:** OpenCV (`cv2`), NumPy
- **Model:** YOLOv4 (`.cfg` + `.weights`), COCO class names

**How to run**

Open `week-1/Assignment-2/YOLO-Object-Detection.ipynb` in Jupyter or Colab. Ensure `yolov4.cfg`, `yolov4.weights`, and `coco.names` (and your image) are in the paths used in the notebook, then run the cells.

---

### Week 2: CPU process scheduling

**What we did:** Implemented **four CPU scheduling algorithms** and compared their average waiting time and average turnaround time:

- **FCFS** — First-Come, First-Served
- **SJF** — Shortest Job First
- **PS** — Priority Scheduling
- **RR** — Round Robin (time quantum = 4)

Inputs: process ID, arrival time, burst time, priority. Outputs: per-process waiting time and turnaround time, plus averages (and in some files, which algorithm gives the lowest averages).

**Tech stack / things used**

- **Language:** Python 3
- **Standard library:** `collections.deque` for RR queue

**Files**

- `process_scheduling_main.py` — Full FCFS, SJF, PS, RR with fixed example processes; prints comparison (lowest avg WT and TAT). **Recommended.**
- `process_scheduling_alt.py` — Same four algorithms with a different set of example processes (longer burst times).
- `processScheduling.py` — Interactive input for number of processes and their parameters; implements FCFS (and partial SJF/PS).

**How to run**

```bash
cd week-2
python process_scheduling_main.py   # or process_scheduling_alt.py for the other example
# For interactive input (FCFS-focused):
python processScheduling.py
```

---

### Week 3: Sunspots forecasting with SARIMA

**What we did:**
Time-series forecasting of **daily total sunspot number** (data from SIDC, from 1818 onward) using **SARIMA** (Seasonal ARIMA). The notebook covers loading and cleaning the data (e.g. handling missing values), exploratory analysis, and fitting a SARIMA model to forecast sunspot activity.

**Tech stack / things used**

- **Language:** Python
- **Libraries:** NumPy, Pandas, Matplotlib, **statsmodels** (SARIMA, ACF/PACF, etc.)
- **Data:** Sunspot series (e.g. daily total sunspot number; source: SIDC / Kaggle-style path in notebook)

**How to run**

Open `week-3/sunspots-forecasting-with-sarima.ipynb` in Jupyter. Adjust the data path if needed (e.g. to your `sunspot_data.csv` location), then run all cells.

---

### Week 3: ResNet cat vs dog classification

**What we did:**
Binary image classification (**cat vs dog**) using **transfer learning** with **ResNet50** (ImageNet weights). The base ResNet50 is frozen; a custom head (e.g. global average pooling + dense layer) is trained on a cat/dog dataset. Built and run in Google Colab with GPU.

**Tech stack / things used**

- **Environment:** Google Colab, GPU (e.g. T4)
- **Framework:** TensorFlow / Keras
- **Model:** ResNet50 (ImageNet, `include_top=False`), custom classification head
- **Data:** Image dataset (e.g. from drive or URL) with cat/dog classes
- **Tools:** Keras `ImageDataGenerator`, PIL, scipy

**How to run**

Open `week-3/ResNetCatvsDog.ipynb` in Colab. Mount Drive or place the dataset where the notebook expects it, then run the cells (data loading, model definition, training, evaluation).

---

### Week 3: NASA C-MAPSS RUL (remaining useful life)

**What we did:**
Worked with the **NASA C-MAPSS** turbofan engine degradation dataset (FD001). The notebook loads train/test sensor and operational data, engineers features, and builds a model to predict **remaining useful life (RUL)** of engines. The companion note `RULMetric.txt` explains why **recall** is more important than precision in this safety-critical setting (e.g. avoiding “no maintenance” when maintenance is actually needed).

**Tech stack / things used**

- **Language:** Python
- **Libraries:** NumPy, Pandas, Matplotlib, Seaborn, scikit-learn (e.g. metrics, possibly models)
- **Data:** NASA C-MAPSS FD001 (`train_FD001.txt`, `test_FD001.txt`, `RUL_FD001.txt`) in `week-3/NasaRULData/`

**How to run**

Open `week-3/NasaRUL.ipynb`. Set the data paths to point to `week-3/NasaRULData/` (or your copy of the FD001 files), then run the notebook.

---

### Week 3: Darknet and OpenCV (notes)

**What we did:**
Documented the steps to **build and use Darknet** with **OpenCV** for detection (e.g. YOLOv3/v4): cloning Darknet, building, downloading weights, enabling **CUDA** for GPU, and building OpenCV with the right options so Darknet can use it. Also described running the detector on images, webcam, or a video file.

**Tech stack / things used**

- **Tools:** Darknet (from GitHub), OpenCV (built from source), CUDA (optional)
- **Models:** YOLOv3 / YOLOv4 config and weights
- **Content:** Instructions only (see `week-3/DarkNetWorking.txt`)

---

## Quick reference — tech stacks by assignment

| Assignment           | Main tech / stack                                        |
| -------------------- | -------------------------------------------------------- |
| Raspi                | Raspberry Pi, Python, RPi.GPIO, Pyrebase, Firebase       |
| Week 1.1 (Socket.IO) | Flask, Flask-SocketIO, HTML/JS or Python socketio client |
| Week 1.2 (YOLO)      | Python, OpenCV, YOLOv4, Colab                            |
| Week 2 (scheduling)  | Python 3, standard library                               |
| Week 3 (SARIMA)      | Python, Pandas, statsmodels, Matplotlib                  |
| Week 3 (ResNet)      | TensorFlow/Keras, ResNet50, Colab GPU                    |
| Week 3 (NASA RUL)    | Python, Pandas, scikit-learn, Matplotlib/Seaborn         |
| Week 3 (Darknet)     | Darknet, OpenCV, CUDA (optional) — documentation only   |

---

## License and use

Course assignments — use for reference and learning. Ensure you have the right to use any external datasets (e.g. NASA C-MAPSS, sunspot data) and models (YOLO, ResNet) according to their respective licenses.
