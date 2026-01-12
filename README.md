# CV Tracking Workshop

A hands-on computer vision workshop demonstrating various object tracking and background subtraction techniques using OpenCV and Python.

## 📋 Prerequisites

- Python 3.x
- OpenCV (`cv2`)
- NumPy
- Matplotlib (for histogram visualization)

### Installation

```bash
pip install opencv-python numpy matplotlib
```

## 🎯 Workshop Contents

### 1. Object Tracking Algorithms

| File | Algorithm | Description |
|------|-----------|-------------|
| `track_meanShift.py` | MeanShift | Color-based object tracking using histogram back-projection |
| `track_camShift.py` | CamShift | Adaptive MeanShift that adjusts the search window size and rotation |
| `track_opticalFlow_LK.py` | Lucas-Kanade Optical Flow | Feature point tracking using sparse optical flow |

### 2. Background Subtraction

| File | Algorithm | Description |
|------|-----------|-------------|
| `substractMOG.py` | MOG | Gaussian Mixture-based Background Subtraction |
| `substractMOG2.py` | MOG2 | Improved MOG with shadow detection |
| `substractGMG.py` | GMG | Statistical background subtraction algorithm |

### 3. Utilities

| File | Description |
|------|-------------|
| `color_histogram.py` | Visualize color histograms for BGR channels |
| `morphology_cleaning.py` | Clean noisy masks using morphological operations (Opening/Closing) |

## 🚀 Usage

### Object Tracking (MeanShift / CamShift)

```bash
python track_meanShift.py
# or
python track_camShift.py
```

1. A webcam window will open
2. Select the object to track with your mouse (draw a rectangle)
3. Press **SPACE** or **ENTER** to start tracking
4. Press **Esc** to exit

### Optical Flow Tracking

```bash
python track_opticalFlow_LK.py
```

- Automatically detects feature points (corners) to track
- Press **Esc** to exit

### Background Subtraction

```bash
python substractMOG2.py
```

- Shows the original frame and foreground mask
- Press **Esc** to exit

### Color Histogram

```bash
python color_histogram.py
```

- Displays histogram of an image (`test_image.jpg`) or captures from webcam
- Close the plot window to exit

## 📖 Algorithm Comparison

### MeanShift / CamShift
| Pros | Cons |
|------|------|
| Good for tracking objects with distinct colors | Fails with drastic lighting changes |
| CamShift handles object deformation | Struggles when background has similar colors |

### Lucas-Kanade Optical Flow
| Pros | Cons |
|------|------|
| Very accurate for tracking textures/corners | Can lose points with fast motion (blur) |
| Handles movement well | Doesn't recover objects once lost |

## 🎮 Controls

- **Esc** - Exit the application
- **Space/Enter** - Confirm selection (for MeanShift/CamShift)

## 📝 Notes

- All scripts use webcam (device 0) by default
- Modify `cv2.VideoCapture(0)` to use a video file instead
- See `comments.md` for additional technical notes

## 📄 License

This project is for educational purposes.
