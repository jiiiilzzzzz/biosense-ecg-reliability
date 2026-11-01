"""
BioSense PH / BIO 405 Integrated Pipeline
Title: Machine Learning-Based Framework for ECG Noise Classification 
       and Heart Rate Reliability Assessment Using Synthetic Physiological Data
Authors: Alexy Jillian M. Buenavista et al.
Section: BIOE-3101 / USTP Biomedical Engineering (2026)
"""

import numpy as np
import pandas as pd
import scipy.signal as signal
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, f1_score, classification_report
import matplotlib.pyplot as plt

# ==========================================
# MODULE 01: SYNTHETIC DATA GENERATOR & LOADER
# ==========================================
class BioSenseDataLoader:
    """Generates synthetic multi-channel waveforms & injects controlled physiological noise."""
    def __init__(self, fs=125):
        self.fs = fs  # Default 125 Hz matching BIDMC / BioSense specification

    def generate_synthetic_ecg(self, duration_s=60, hr_bpm=75, noise_type="clean", noise_level=0.2):
        t = np.linspace(0, duration_s, int(self.fs * duration_s), endpoint=False)
        rr_interval = 60.0 / hr_bpm
        
        # Synthetic ECG wave synthesis (P, QRS, T)
        ecg = np.zeros_like(t)
        peak_times = np.arange(0.5, duration_s, rr_interval)
        
        for p_time in peak_times:
            # QRS complex
            ecg += 1.2 * np.exp(-((t - p_time) / 0.02) ** 2)    # R-peak
            ecg -= 0.3 * np.exp(-((t - (p_time - 0.03)) / 0.015) ** 2) # Q-wave
            ecg -= 0.4 * np.exp(-((t - (p_time + 0.03)) / 0.015) ** 2) # S-wave
            # P wave & T wave
            ecg += 0.15 * np.exp(-((t - (p_time - 0.18)) / 0.04) ** 2)
            ecg += 0.25 * np.exp(-((t - (p_time + 0.22)) / 0.06) ** 2)

        # Inject controlled noise categories
        noise = np.zeros_like(t)
        if noise_type == "baseline_wander":
            noise = noise_level * np.sin(2 * np.pi * 0.2 * t)
        elif noise_type == "muscle_artifact":
            noise = noise_level * np.random.normal(0, 1, len(t))
        elif noise_type == "powerline":
            noise = noise_level * np.sin(2 * np.pi * 60.0 * t)  # 60 Hz grid noise
        elif noise_type == "motion_artifact":
            # Sudden abrupt transient shifts
            for burst in np.arange(5, duration_s, 15):
                idx = (t >= burst) & (t <= burst + 1.5)
                noise[idx] += noise_level * 2.5 * np.sin(2 * np.pi * 2 * t[idx])

        noisy_ecg = ecg + noise
        
        # Structure into Team 01 Internal Waveform Data Object
        waveform_data = {
            "record_id": f"synth_{noise_type}_hr{hr_bpm}",
            "time_s": t,
            "fs": self.fs,
            "signals": {
                "ECG": noisy_ecg,
                "PPG": noisy_ecg,  # Illustrative alignment
                "RESP": np.sin(2 * np.pi * 0.25 * t) # 15 breaths/min reference
            },
            "reference_hr": hr_bpm,
            "noise_label": noise_type
        }
        return waveform_data

# ==========================================
# MODULE 02 & 04: SIGNAL PROCESSING & PEAK DETECTION
# ==========================================
class SignalProcessor:
    """Detects R-peaks, calculates heart rate (HR), and extracts features."""
    def __init__(self, fs=125):
        self.fs = fs

    def bandpass_filter(self, sig, lowcut=0.5, highcut=40.0):
        nyq = 0.5 * self.fs
        b, a = signal.butter(1, [lowcut / nyq, highcut / nyq], btype='band')
        return signal.filtfilt(b, a, sig)

    def detect_r_peaks(self, ecg_sig):
        filtered = self.bandpass_filter(ecg_sig)
        diff = np.diff(filtered)
        squared = diff ** 2
        window_len = int(0.12 * self.fs)
        integrated = np.convolve(squared, np.ones(window_len) / window_len, mode='same')
        
        # Peak thresholding
        peaks, _ = signal.find_peaks(integrated, distance=int(0.4 * self.fs), height=np.mean(integrated) * 1.2)
        return peaks

    def estimate_hr(self, peaks):
        if len(peaks) < 2:
            return 0.0
        rr_intervals = np.diff(peaks) / self.fs
        mean_rr = np.mean(rr_intervals)
        return 60.0 / mean_rr if mean_rr > 0 else 0.0

# ==========================================
# MODULE 05 & ML: NOISE CLASSIFICATION & QUALITY
# ==========================================
class ECGNoiseClassifier:
    """Extracts features across time/frequency domains and predicts noise condition."""
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=50, random_state=42)
        self.classes = ["clean", "baseline_wander", "muscle_artifact", "powerline", "motion_artifact"]

    def extract_features(self, sig, fs=125):
        # Time domain features
        std_val = np.std(sig)
        rms_val = np.sqrt(np.mean(sig**2))
        max_diff = np.max(np.abs(np.diff(sig)))
        
        # Frequency domain features
        freqs, psd = signal.welch(sig, fs=fs, nperseg=min(len(sig), 256))
        power_low = np.sum(psd[(freqs >= 0.1) & (freqs <= 1.0)])
        power_line = np.sum(psd[(freqs >= 58.0) & (freqs <= 62.0)])
        power_high = np.sum(psd[freqs > 30.0])
        
        return [std_val, rms_val, max_diff, power_low, power_line, power_high]

    def train_mock_model(self, loader):
        """Builds dataset from synthetic generator to train internal ML classifier."""
        X, y = [], []
        for label in self.classes:
            for hr in [60, 75, 90]:
                for lvl in [0.2, 0.4, 0.6]:
                    data = loader.generate_synthetic_ecg(duration_s=30, hr_bpm=hr, noise_type=label, noise_level=lvl)
                    feats = self.extract_features(data["signals"]["ECG"], fs=data["fs"])
                    X.append(feats)
                    y.append(label)
        self.model.fit(X, y)

    def predict_noise(self, sig, fs=125):
        feats = self.extract_features(sig, fs=fs)
        return self.model.predict([feats])[0]

# ==========================================
# MODULE 06 & 08: INTEGRATION & RELIABILITY FUSION
# ==========================================
class BioSenseIntegrator:
    """Combines signal processing, ML predictions, and evaluates measurement reliability."""
    def __init__(self, tolerance_bpm=5.0):
        self.processor = SignalProcessor()
        self.classifier = ECGNoiseClassifier()
        self.loader = BioSenseDataLoader()
        self.classifier.train_mock_model(self.loader)
        self.tolerance_bpm = tolerance_bpm

    def process_window(self, waveform_data, start_s=0, window_len_s=30):
        fs = waveform_data["fs"]
        start_idx = int(start_s * fs)
        end_idx = int((start_s + window_len_s) * fs)
        
        sig_window = waveform_data["signals"]["ECG"][start_idx:end_idx]
        ref_hr = waveform_data["reference_hr"]
        
        # ML Noise Classification
        predicted_noise = self.classifier.predict_noise(sig_window, fs=fs)
        
        # R-peak detection & HR estimation
        peaks = self.processor.detect_r_peaks(sig_window)
        estimated_hr = self.processor.estimate_hr(peaks)
        
        # Error & Reliability Calculation
        abs_error = abs(estimated_hr - ref_hr) if estimated_hr > 0 else 999.0
        
        if len(peaks) < 3 or predicted_noise in ["motion_artifact", "muscle_artifact"] and abs_error > self.tolerance_bpm:
            quality_label = "LOW"
            reliability = "Unreliable"
        elif abs_error <= self.tolerance_bpm:
            quality_label = "OK"
            reliability = "High"
        else:
            quality_label = "CAUTION"
            reliability = "Moderate"

        return {
            "record_id": waveform_data["record_id"],
            "start_s": start_s,
            "end_s": start_s + window_len_s,
            "estimated_hr": round(estimated_hr, 2),
            "reference_hr": ref_hr,
            "abs_error_bpm": round(abs_error, 2),
            "predicted_noise": predicted_noise,
            "quality": quality_label,
            "reliability": reliability
        }

# ==========================================
# MAIN INTEGRATED DEMONSTRATION RUNNER
# ==========================================
if __name__ == "__main__":
    print("=" * 65)
    print(" BioSense PH: ECG Signal Quality & HR Reliability Prototype ")
    print("=" * 65)

    integrator = BioSenseIntegrator(tolerance_bpm=5.0)
    loader = BioSenseDataLoader()

    # Generate Test Scenarios (Clean, Baseline Wander, Motion Artifact)
    scenarios = [
        ("clean", 0.1, 75),
        ("baseline_wander", 0.4, 80),
        ("powerline", 0.5, 70),
        ("motion_artifact", 0.8, 85)
    ]

    feature_table_rows = []

    for noise_type, level, target_hr in scenarios:
        rec = loader.generate_synthetic_ecg(duration_s=60, hr_bpm=target_hr, noise_type=noise_type, noise_level=level)
        
        # Analyze two non-overlapping 30-second windows per record (Schema Compliance)
        for start_t in [0, 30]:
            res = integrator.process_window(rec, start_s=start_t, window_len_s=30)
            feature_table_rows.append(res)

    # Output Standardized Team 01-08 Schema Table
    df_results = pd.DataFrame(feature_table_rows)
    print("\n[REQUIRED OUTPUT] Standardized 30-Second Window Feature Table:")
    print(df_results.to_string(index=False))

    # Calculate Quantitative System Validation Metrics
    mae = df_results['abs_error_bpm'].mean()
    print("\n" + "=" * 65)
    print(f" Quantitative Performance Summary:")
    print(f"  • Total Evaluated Windows : {len(df_results)}")
    print(f"  • Mean Absolute Error (MAE): {mae:.2f} bpm")
    print("=" * 65)

    # Generate Verification Plot (Team 02 / Team 07 Output)
    sample_rec = loader.generate_synthetic_ecg(duration_s=10, hr_bpm=75, noise_type="motion_artifact", noise_level=0.5)
    processor = SignalProcessor()
    peaks = processor.detect_r_peaks(sample_rec["signals"]["ECG"])

    plt.figure(figsize=(10, 4))
    plt.plot(sample_rec["time_s"], sample_rec["signals"]["ECG"], label="Noisy ECG (Motion Artifact)", color='navy')
    plt.plot(sample_rec["time_s"][peaks], sample_rec["signals"]["ECG"][peaks], 'ro', label="Detected R-peaks")
    plt.title("BioSense PH - Waveform & R-Peak Verification Trace")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude (mV)")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(loc="upper right")
    plt.tight_layout()
    plt.savefig("ecg_verification_trace.png")
    print("\n[SUCCESS] Verification plot exported as 'ecg_verification_trace.png'.")