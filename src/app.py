import streamlit as st
import matplotlib.pyplot as plt
from qiskit.visualization import plot_bloch_multivector
from quantum_engine import (
    run_single_round, 
    run_tournament_simulation, 
    get_bloch_state, 
    run_classical_vs_quantum_comparison, 
    compute_angle_sweep
)

st.set_page_config(page_title="EntangleLinks - Quantum Game", page_icon="⚛️", layout="wide")

# Custom UI Styling
st.markdown("""
    <style>
    .metric-card {
        background-color: #1E293B;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        border: 2px solid #3B82F6;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    .metric-title {
        color: #94A3B8;
        font-size: 14px;
        font-weight: 600;
        margin-bottom: 8px;
        text-transform: uppercase;
    }
    .metric-value {
        color: #38BDF8;
        font-size: 36px;
        font-weight: 800;
    }
    </style>
""", unsafe_allow_html=True)

st.title("⚛️ EntangleLinks: CHSH Quantum Advantage Simulator")
st.markdown("Explore quantum entanglement and break the **75% classical speed limit** using Qiskit!")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🎮 Single Round", 
    "🏆 Tournament Mode", 
    "🌐 Bloch Sphere", 
    "⚖️ Classical vs Quantum", 
    "📈 Angle Sweep Curve"
])

# --- TAB 1: SINGLE ROUND GAME ---
with tab1:
    col_ctrl, col_res = st.columns([1, 2])
    with col_ctrl:
        st.subheader("Player Inputs")
        alice_bit = st.selectbox("Alice Input (x)", [0, 1], key="s_alice")
        bob_bit = st.selectbox("Bob Input (y)", [0, 1], key="s_bob")
        shots = st.slider("Number of Shots", 10, 1000, 100, 10, key="s_shots")
        run_btn = st.button("🚀 Run Execution", type="primary", use_container_width=True)

    with col_res:
        if run_btn:
            counts, win_rate, circuit = run_single_round(alice_bit, bob_bit, shots)
            m1, m2 = st.columns(2)
            with m1:
                st.markdown(f"""
                    <div class="metric-card">
                        <div class="metric-title">Quantum Win Rate</div>
                        <div class="metric-value">{win_rate:.1f}%</div>
                    </div>
                """, unsafe_allow_html=True)
            with m2:
                st.markdown(f"""
                    <div class="metric-card">
                        <div class="metric-title">Total Shots</div>
                        <div class="metric-value">{shots}</div>
                    </div>
                """, unsafe_allow_html=True)
            
            st.write("")
            if win_rate > 75:
                st.success("🎉 **Quantum Advantage Achieved!** Surpassed the 75% classical limit!")
            else:
                st.info("Classical region reached. Try switching input bits.")
                
            c1, c2 = st.columns(2)
            with c1:
                st.subheader("🔬 Quantum Circuit")
                fig_circ, ax_circ = plt.subplots(figsize=(5, 3))
                circuit.draw(output='mpl', ax=ax_circ)
                st.pyplot(fig_circ)
            with c2:
                st.subheader("📊 Outcome Distribution")
                st.bar_chart(counts)

# --- TAB 2: TOURNAMENT MODE ---
with tab2:
    st.subheader("🏆 Automated CHSH Tournament")
    st.write("Run all 4 input combinations simultaneously to verify overall Quantum Advantage.")
    if st.button("⚡ Execute Full Tournament", key="t_btn"):
        results, overall_win_rate = run_tournament_simulation()
        st.markdown(f"""
            <div class="metric-card" style="margin-bottom: 20px;">
                <div class="metric-title">Overall Tournament Win Rate (1000 Total Shots)</div>
                <div class="metric-value" style="color: #10B981;">{overall_win_rate:.1f}%</div>
            </div>
        """, unsafe_allow_html=True)
        st.bar_chart(results)

# --- TAB 3: BLOCH SPHERE ---
with tab3:
    st.subheader("🌐 Quantum State Visualization (Bloch Spheres)")
    st.write("Visualizing the entangled qubit statevectors before measurement.")
    x_bloch = st.radio("Alice Input (x)", [0, 1], horizontal=True, key="b_x")
    y_bloch = st.radio("Bob Input (y)", [0, 1], horizontal=True, key="b_y")
    state = get_bloch_state(x_bloch, y_bloch)
    fig_bloch = plot_bloch_multivector(state)
    st.pyplot(fig_bloch)

# --- TAB 4: CLASSICAL VS QUANTUM COMPARISON ---
with tab4:
    st.subheader("⚖️ Side-by-Side: Classical vs. Quantum Strategy")
    st.write("Compare classical limits directly against quantum entanglement performance in real time.")
    
    cq_x = st.selectbox("Input x", [0, 1], key="cq_x")
    cq_y = st.selectbox("Input y", [0, 1], key="cq_y")
    if st.button("⚖️ Run Comparison", type="primary"):
        c_rate, q_rate = run_classical_vs_quantum_comparison(cq_x, cq_y)
        
        cc1, cc2 = st.columns(2)
        with cc1:
            st.markdown(f"""
                <div class="metric-card" style="border-color: #EF4444;">
                    <div class="metric-title">Classical Strategy</div>
                    <div class="metric-value" style="color: #EF4444;">{c_rate:.1f}%</div>
                </div>
            """, unsafe_allow_html=True)
            st.caption("Capped by local realism (Max ~75%)")
        with cc2:
            st.markdown(f"""
                <div class="metric-card" style="border-color: #10B981;">
                    <div class="metric-title">Quantum Entanglement</div>
                    <div class="metric-value" style="color: #10B981;">{q_rate:.1f}%</div>
                </div>
            """, unsafe_allow_html=True)
            st.caption("Shatters classical bounds using Bell states")

# --- TAB 5: ANGLE SWEEP CURVE ---
with tab5:
    st.subheader("📈 Continuous Angle Sweep & Bell Violation Curve")
    st.write("This scientific graph plots the CHSH value ($S$) across measurement angles. Notice how it exceeds the classical threshold ($S = 2$).")
    
    if st.button("📊 Generate Violation Curve"):
        angles, violations = compute_angle_sweep()
        
        fig_angle, ax_angle = plt.subplots(figsize=(8, 4))
        ax_angle.plot(angles, violations, label="Quantum CHSH Value ($S$)", color="#38BDF8", linewidth=3)
        ax_angle.axhline(y=2.0, color="#EF4444", linestyle="--", label="Classical Limit ($S = 2$)")
        ax_angle.axhline(y=2.828, color="#10B981", linestyle=":", label="Tsirelson's Bound ($2\sqrt{2}$)")
        ax_angle.set_xlabel("Measurement Angle (Radians)")
        ax_angle.set_ylabel("CHSH Metric ($S$)")
        ax_angle.set_title("Bell's Inequality Violation Curve")
        ax_angle.legend()
        ax_angle.grid(True, alpha=0.3)
        
        st.pyplot(fig_angle)
        st.success("💡 **Judge Pitch Note**: The region above the red dashed line proves undeniable Quantum Advantage!")