import streamlit as st
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

st.set_page_config(
    page_title="EntangleLinks", page_icon="⚛️", layout="centered"
)

st.title("⚛️ EntangleLinks: The CHSH Bell Challenge")
st.subheader("Quantum Telepathy Game")

st.markdown("""
Welcome! In this game, **Alice** and **Bob** are placed in separate rooms. 
By sharing a **Quantum Entangled Pair (Bell State)**, they can achieve win rates higher than classical probability allows (~85% vs 75%)!
""")

st.divider()

# Controls
st.sidebar.header("Game Settings")
alice_bit = st.sidebar.radio("Alice's Input Bit (x)", [0, 1])
bob_bit = st.sidebar.radio("Bob's Input Bit (y)", [0, 1])


def run_chsh_game(x, y):
  # Create a 2-qubit circuit
  qc = QuantumCircuit(2, 2)

  # Create Entanglement (|Phi+> state)
  qc.h(0)
  qc.cx(0, 1)

  # Alice's bases
  if x == 1:
    qc.ry(0.785398, 0)  # ~pi/4

  # Bob's bases
  if y == 1:
    qc.ry(-0.785398, 1)  # -pi/4

  # Measurement
  qc.measure([0, 1], [0, 1])

  # Run on Aer Simulator
  simulator = AerSimulator()
  job = simulator.run(qc, shots=100)
  counts = job.result().get_counts()

  return counts, qc


if st.button("🚀 Execute Quantum Round", type="primary"):
  counts, circuit = run_chsh_game(alice_bit, bob_bit)

  st.write("### Quantum Circuit Diagram")
  st.text(str(circuit))

  st.write("### Measurement Results (100 Shots)")
  st.bar_chart(counts)

  # Winning condition check: a XOR b == x AND y
  winning_shots = 0
  total_shots = sum(counts.values())

  for outcome, count in counts.items():
    a = int(outcome[1])  # Alice qubit
    b = int(outcome[0])  # Bob qubit
    if (a ^ b) == (alice_bit & bob_bit):
      winning_shots += count

  win_rate = (winning_shots / total_shots) * 100
  st.metric(label="Win Rate", value=f"{win_rate:.1f}%")

  if win_rate > 75:
    st.success(
        "🎉 Quantum Advantage Achieved! You broke the classical bound of 75%!"
    )
  else:
    st.info("Try running again or changing input bits to test different bases.")