# ⚛️ EntangleLinks: CHSH Quantum Advantage Simulator

> **EntangleLinks** is an interactive, modular quantum simulation dashboard developed for the **Qiskit Fall Fest 2026**. It demonstrates the profound power of quantum entanglement by pitting classical strategies against quantum mechanics in the famous **Clauser-Horne-Shimony-Holt (CHSH) game**.

---

## 🚀 Project Overview

In computer science and physics, independent players cooperating without communication are strictly bounded by local realism. In the cooperative CHSH game, classical strategies hit a hard ceiling at a **75% maximum success rate**. 

**EntangleLinks** bridges the gap between complex quantum theory and intuitive design. By leveraging **IBM's Qiskit** backend and an interactive **Streamlit** frontend, our application allows users to experience, simulate, and mathematically verify how quantum entanglement shatters classical limits, achieving success rates upwards of ~85%.

---

## 🌟 Core Features & Architecture

The application is structured into 5 distinct, high-impact interactive tabs managed by a clean separation of concerns (`src/app.py` for UI, `src/quantum_engine.py` for backend logic):

1. **🎮 Single Round Game**
   * **Functionality**: Allows users to select individual input bits for Alice ($x$) and Bob ($y$), execute real Qiskit quantum circuits, and observe individual win/loss outcomes alongside generated circuit diagrams.
2. **🏆 Tournament Mode (1000 Shots)**
   * **Functionality**: Automatically runs all 4 possible input combinations ($0,0$, $0,1$, $1,0$, $1,1$) back-to-back across 1,000 total shots to verify consistent quantum performance.
3. **🌐 Bloch Sphere Visualizer**
   * **Functionality**: Renders 3D quantum statevectors dynamically in multi-dimensional space, tracking how qubit states shift under rotation parameters.
4. **⚖️ Classical vs. Quantum Comparison**
   * **Functionality**: Provides a side-by-side performance benchmark contrasting the local realism limit (capped at $\le 75\%$) directly against the quantum strategy ($\sim 85\%$).
5. **📈 Continuous Angle Sweep Curve**
   * **Functionality**: Plots a scientific visualization graph measuring the CHSH violation value ($S$) across multiple angles, explicitly highlighting **Tsirelson's Bound ($2\sqrt{2} \approx 2.828$)** versus the classical limit ($2.0$).

---

## 📂 Repository Structure

EntangleLinks/
│
├── src/
│   ├── app.py              # Streamlit Frontend UI & Interactive Dashboard
│   └── quantum_engine.py   # Qiskit Backend Logic, Circuits, & Math
│
├── README.md               # Comprehensive Project Documentation
└── requirements.txt        # Project Dependencies