# TICK MOVEMENT PIPELINE

---
###Summary: 
I built an end-to-end workflow to quantify tick movement behavior from standardized arena recordings. Videos are processed using idtracker.ai to extract coordinate trajectories, which are then scaled using a reference square and summarized into movement metrics such as total distance and average speed. The pipeline generates visual outputs to compare behavior across species and sex. This project combines field/lab protocol design with reproducible data processing and visualization in Python.



---

## Overview

**Workflow**
1. Install `idtrackerai` locally (PyTorch environment)
2. Record and label videos using a standardized protocol
3. Track individuals with `idtrackerai` to export coordinate/trajectory data
4. Compute pixel → cm scaling using `TickScalingfinder.py`
5. Generate summary metrics + plots using `tick_tracking_summarydata.py`

---

## Installation (Local) — idtracker.ai + PyTorch

This project assumes you have Python installed and are using a virtual environment (recommended: Conda).

### 1) Create a Conda environment
```bash
conda create -n idtrackerai python=3.10
conda activate idtrackerai
```
---

### 2) 
Install PyTorch using the official instructions based on your system:

https://pytorch.org/get-started/locally/

(GPU acceleration is recommended if you have an NVIDIA GPU, but CPU is supported.)

---

### 3) Install idtracker.ai / idtrackerai

Follow the official idtracker.ai installation guide:

https://idtracker.ai/latest/install/installation.html

Older manual versions also document conda + PyTorch setups and GUI vs CLI options:

https://idtracker.ai/4.0.12/how_to_install.html

---

### 4) Confirm installation

Once installed, you should be able to run:

idtrackerai --help

Video Input Protocol (Recording Standard)

This pipeline assumes videos are recorded consistently to produce reliable tracking output.

### Setup

Individuals should be wearing appropriate lab attire.

Before being placed in the arena, ticks should be stored with moisture to keep them alive.

Tripod height should be ~50 cm above the arena.

Arena: 9” x 7” plastic board with a double-sided tape border.

Use overhead full-spectrum lighting.

The recorded arena area must include a 5 cm x 5 cm reference square (paper or other material) for scaling/resolution.

Maintain collection metadata for each video using the official lab tracking sheet.

The video label placed in the upper-right corner of the arena should include:


### Equipment Needed

Plastic cutting board (arena)

Tripod

Sticky tape / double-sided tape

Reference scale paper (5x5 cm)

Full spectrum light + stand

Camera/Phone: iPhone 13

2x zoom for nymphs

1x zoom for adults

### Filming Procedure

Confirm the correct vial before opening.
Record one tick at a time.

Adults: confirm species under microscope quickly (target: ~1 minute).
Record adults using 1x zoom

Nymphs: do not require morphological ID before recording.
Record nymph videos using 2x zoom

After recording, store the nymph in a flat-bottom eppendorf tube and number it to match the video tick number

Do not start identifying additional ticks until the current tick is returned to its original vial.

Once a vial is opened, all ticks inside must be filmed before ending the session or switching vials.

Transfer tick to the arena center and record for two consecutive minutes.

Track time-to-activation on a separate timer

If the tick reaches the tape border in under 30 seconds:
stop the recording
reset tick to center
record a second take

## Second Take Rules

If a second take is required:
mark as "T2" / "Take 2" on the paper label and filename
if it reaches the border in under 30 seconds again, stop and return tick to vial


Using This Repo: Data Path + Scripts
### 1) Put tracking coordinate files in one folder

After running idtrackerai tracking, ensure that all coordinate/trajectory outputs (CSV or exported arrays) are placed in a single directory.

Example:

data/
  video_01/
    trajectories.csv
  video_02/
    trajectories.csv

### 2) Find scaling from the reference square

Run:

python TickScalingfinder.py

This script outputs the scale factor (pixels → cm) based on the 5x5 cm reference object in the recorded arena.


### 3) Generate summary metrics + plots

Use the scaling output from TickScalingfinder.py as the input for the scaling section inside:

python tick_tracking_summarydata.py

This step produces summary tables and plots such as trajectory visualization

### Notes/Troubleshooting
If idtracker.ai fails to detect GPU, ensure PyTorch is installed correctly for your platform and try reinstalling your environment.

For official troubleshooting guidance:
https://idtracker.ai/latest/install/installation_troubleshooting.html

---

### AUTHOR
### Daniel Ejakov
### Michigan State University
### Email: ejakovda@msu.edu



