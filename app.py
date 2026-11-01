import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from biosense_pipeline import BioSenseDataLoader, BioSenseIntegrator, SignalProcessor

st.set_page_config(page_title="BioSense PH Dashboard", layout="wide")

st.title("BioSense PH: Biomedical Monitoring & HR Reliability Demonstrator")
st.caption("BIO 405 / BIOE-3101 Research Prototype | Batangas City Community Healthcare Application")

# Sidebar Controls
st.sidebar.header("Simulation Settings")
noise_choice = st.sidebar.selectbox("Select ECG Noise Condition", ["clean", "baseline_wander", "muscle_artifact", "powerline", "motion_artifact"])
ref_hr = st.sidebar.slider("Reference Heart Rate (bpm)", 50, 120, 75)
noise_lvl = st.sidebar.slider("Noise Amplitude/Severity", 0.0, 1.0, 0.4)

# Execute Integrated Pipeline
loader = BioSenseDataLoader()
integrator = BioSenseIntegrator()
processor = SignalProcessor()

waveform_data = loader.generate_synthetic_ecg(duration_s=30, hr_bpm=ref_hr, noise_type=noise_choice, noise_level=noise_lvl)
result = integrator.process_window(waveform_data, start_s=0, window_len_s=30)

# Dashboard Summary Metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("Estimated Heart Rate", f"{result['estimated_hr']} bpm")
col2.metric("Reference Heart Rate", f"{result['reference_hr']} bpm")
col3.metric("Predicted Noise Type", result['predicted_noise'])
col4.metric("Reliability Assessment", result['reliability'], delta_color="normal" if result['reliability'] == "High" else "inverse")

# Signal Plotting
st.subheader("ECG Waveform & Detected Cardiac Peaks")
sig = waveform_data["signals"]["ECG"]
t = waveform_data["time_s"]
peaks = processor.detect_r_peaks(sig)

fig, ax = plt.subplots(figsize=(12, 4))
ax.plot(t, sig, label="Input ECG Waveform", color='#1f77b4')
ax.plot(t[peaks], sig[peaks], "x", label="Detected R-peaks", color='red', markersize=10, markeredgewidth=2)
ax.set_xlabel("Time (seconds)")
ax.set_ylabel("Amplitude (mV)")
ax.grid(True, alpha=0.3)
ax.legend()
st.pyplot(fig)

# Standardized Exportable Table
st.subheader("Standardized Feature Table Output (Team 01-08 Data Schema)")
df = pd.DataFrame([result])
st.dataframe(df)