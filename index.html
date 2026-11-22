<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>ECG Noise Classification & Heart Rate Reliability Assessment</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    body {
      font-family: 'Inter', sans-serif;
      background-color: #f8fafc;
      color: #0f172a;
    }
    .mono {
      font-family: 'JetBrains Mono', monospace;
    }
    canvas {
      display: block;
      width: 100%;
      height: 100%;
    }
    input[type="range"] {
      accent-color: #0284c7;
    }
  </style>
</head>
<body class="min-h-screen flex flex-col">

  <!-- Top Clinical Header -->
  <header class="bg-slate-900 text-white border-b border-slate-800 sticky top-0 z-30 shadow-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3.5 flex flex-col sm:flex-row sm:items-center sm:justify-between gap-2">
      <div>
        <div class="flex items-center gap-2.5">
          <span class="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-sky-500/20 text-sky-400 border border-sky-500/30">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" d="M3 12h4l3-9 4 18 3-9h4" />
            </svg>
          </span>
          <h1 class="text-base sm:text-lg font-bold tracking-tight">
            ECG Noise Classification &amp; HR Reliability Gate
          </h1>
        </div>
        <p class="text-xs text-slate-400 mt-0.5">
          Buenavista, Dimafelix &amp; Landicho &bull; Dept. of Electronics Engineering (BS Biomedical Engineering), Batangas State University
        </p>
      </div>
      <div class="flex items-center gap-2 self-start sm:self-center">
        <span id="model-status-badge" class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-medium bg-amber-500/15 text-amber-300 border border-amber-500/30">
          <span class="w-2 h-2 rounded-full bg-amber-400 animate-pulse"></span>
          Training Random Forests...
        </span>
      </div>
    </div>
  </header>

  <!-- Main Workspace -->
  <main class="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-6">
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">

      <!-- LEFT SIDEBAR: PhysioNet Upload, Scrubber, Noise Stress-Test & Thresholds -->
      <aside class="lg:col-span-4 space-y-5">

        <!-- 1. PhysioNet Record Upload Card -->
        <section class="bg-white rounded-xl border border-slate-200 shadow-sm p-5">
          <div class="flex items-center justify-between mb-3">
            <h2 class="text-sm font-semibold text-slate-800 uppercase tracking-wider">1. PhysioNet Record Input</h2>
            <span class="text-[11px] font-medium px-2 py-0.5 rounded bg-sky-50 text-sky-700 border border-sky-200">WFDB 212 / CSV / TXT</span>
          </div>

          <p class="text-xs text-slate-500 mb-3 leading-relaxed">
            Upload public PhysioNet recordings (e.g., MIT-BIH Arrhythmia <code class="mono text-slate-700">100.dat</code> + <code class="mono text-slate-700">100.hea</code>, MIT-BIH NSTDB <code class="mono text-slate-700">bw.dat</code>, <code class="mono text-slate-700">ma.dat</code>, <code class="mono text-slate-700">em.dat</code>, or CSV/TXT waveform exports).
          </p>

          <!-- Drag & Drop / File Picker -->
          <label id="drop-zone" class="flex flex-col items-center justify-center w-full p-4 border-2 border-dashed border-slate-300 rounded-xl bg-slate-50 hover:bg-sky-50/50 hover:border-sky-400 transition cursor-pointer text-center">
            <svg class="w-7 h-7 text-slate-400 mb-1.5" fill="none" stroke="currentColor" stroke-width="1.75" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
            </svg>
            <span class="text-xs font-semibold text-slate-700">Click to select or drop PhysioNet file(s)</span>
            <span class="text-[11px] text-slate-400 mt-0.5">Select <code class="mono">.dat</code> (with optional <code class="mono">.hea</code>) or <code class="mono">.csv</code> / <code class="mono">.txt</code></span>
            <input id="file-input" type="file" multiple accept=".dat,.hea,.csv,.txt,.json" class="hidden" />
          </label>

          <!-- File Status Banner -->
          <div id="file-info-box" class="mt-3 p-2.5 rounded-lg bg-slate-100 border border-slate-200 text-xs space-y-1">
            <div class="flex justify-between">
              <span class="text-slate-500">Active Record:</span>
              <span id="record-name" class="font-semibold text-slate-800 truncate max-w-[180px]">MIT-BIH Sample (Clean)</span>
            </div>
            <div class="flex justify-between">
              <span class="text-slate-500">Source Fs &rarr; Resampled:</span>
              <span id="record-fs-info" class="mono text-slate-700">360 Hz &rarr; 250 Hz</span>
            </div>
            <div class="flex justify-between">
              <span class="text-slate-500">Total Duration:</span>
              <span id="record-duration" class="mono text-slate-700">30.0 s (7,500 samples)</span>
            </div>
          </div>

          <!-- Sampling Rate & Channel Controls -->
          <div class="grid grid-cols-2 gap-2.5 mt-3">
            <div>
              <label for="input-fs" class="block text-[11px] font-medium text-slate-600 mb-1">Source Sampling (Hz)</label>
              <select id="input-fs" class="w-full rounded-lg border border-slate-300 bg-white px-2.5 py-1.5 text-xs text-slate-800 focus:outline-none focus:border-sky-500">
                <option value="360" selected>360 Hz (MIT-BIH / NSTDB)</option>
                <option value="250">250 Hz (Native Target)</option>
                <option value="500">500 Hz (PTB-XL / Clinical)</option>
                <option value="128">128 Hz (Holter / NST)</option>
                <option value="1000">1000 Hz (High-Res)</option>
              </select>
            </div>
            <div>
              <label for="input-channel" class="block text-[11px] font-medium text-slate-600 mb-1">Lead / Channel</label>
              <select id="input-channel" class="w-full rounded-lg border border-slate-300 bg-white px-2.5 py-1.5 text-xs text-slate-800 focus:outline-none focus:border-sky-500">
                <option value="0" selected>Channel 0 (Primary)</option>
                <option value="1">Channel 1 (Secondary)</option>
              </select>
            </div>
          </div>

          <!-- Built-In Sample PhysioNet-Style Presets -->
          <div class="mt-4 pt-3 border-t border-slate-100">
            <span class="block text-[11px] font-medium text-slate-500 mb-2">Quick-Load Sample PhysioNet-Style Records:</span>
            <div class="grid grid-cols-2 gap-1.5">
              <button type="button" data-preset="mit100" class="preset-btn px-2.5 py-1.5 rounded-lg text-xs font-medium bg-slate-100 hover:bg-sky-50 text-slate-700 hover:text-sky-700 border border-slate-200 transition text-left truncate">
                MIT-BIH 100 (Clean)
              </button>
              <button type="button" data-preset="nstdb_bw" class="preset-btn px-2.5 py-1.5 rounded-lg text-xs font-medium bg-slate-100 hover:bg-sky-50 text-slate-700 hover:text-sky-700 border border-slate-200 transition text-left truncate">
                NSTDB 'bw' (Baseline)
              </button>
              <button type="button" data-preset="nstdb_ma" class="preset-btn px-2.5 py-1.5 rounded-lg text-xs font-medium bg-slate-100 hover:bg-sky-50 text-slate-700 hover:text-sky-700 border border-slate-200 transition text-left truncate">
                NSTDB 'ma' (Muscle)
              </button>
              <button type="button" data-preset="nstdb_em" class="preset-btn px-2.5 py-1.5 rounded-lg text-xs font-medium bg-slate-100 hover:bg-sky-50 text-slate-700 hover:text-sky-700 border border-slate-200 transition text-left truncate">
                NSTDB 'em' (Motion)
              </button>
              <button type="button" data-preset="ph_60hz" class="preset-btn col-span-2 px-2.5 py-1.5 rounded-lg text-xs font-medium bg-amber-50 hover:bg-amber-100 text-amber-800 border border-amber-200 transition text-left truncate">
                MIT-BIH + Philippine 60 Hz Power-Line (0 dB)
              </button>
            </div>
          </div>
        </section>

        <!-- 2. 10-Second Window Scrubber & Stress-Test Mixer -->
        <section class="bg-white rounded-xl border border-slate-200 shadow-sm p-5 space-y-4">
          <div>
            <div class="flex items-center justify-between mb-1">
              <h2 class="text-sm font-semibold text-slate-800 uppercase tracking-wider">2. Window &amp; Stress Mixer</h2>
              <span id="window-time-label" class="mono text-xs font-semibold text-sky-700">0.0s &ndash; 10.0s</span>
            </div>
            <p class="text-[11px] text-slate-500 mb-2">Scrub any 10-second segment (2,500 samples @ 250 Hz) of the loaded record.</p>
            <input id="window-slider" type="range" min="0" max="20" step="0.5" value="0" class="w-full cursor-pointer" />
            <div class="flex justify-between text-[10px] text-slate-400 mono mt-0.5">
              <span>0.0s</span>
              <span id="max-time-label">30.0s</span>
            </div>
          </div>

          <!-- Optional Controlled Noise Stress-Test on Uploaded Record -->
          <div class="pt-3 border-t border-slate-100">
            <div class="flex items-center justify-between mb-2">
              <label for="stress-noise-type" class="text-xs font-semibold text-slate-700">Optional Noise Injection (Stress Test)</label>
              <span class="text-[10px] text-slate-400">Sec. 4.1 Eq. (3)</span>
            </div>
            <select id="stress-noise-type" class="w-full rounded-lg border border-slate-300 bg-white px-2.5 py-1.5 text-xs text-slate-800 mb-2.5">
              <option value="None" selected>None (Evaluate Uploaded Signal As-Is)</option>
              <option value="Baseline">Inject Baseline Wander (&lt; 0.7 Hz)</option>
              <option value="Muscle">Inject Muscle Artifact (EMG 20–100 Hz)</option>
              <option value="Power line">Inject Philippine 60 Hz Grid Interference</option>
              <option value="Motion">Inject Electrode Motion Transient</option>
            </select>

            <div id="snr-control-wrap" class="opacity-40 pointer-events-none transition-opacity">
              <div class="flex justify-between text-xs mb-1">
                <span class="text-slate-600 font-medium">Injected SNR (&rho;)</span>
                <span id="snr-val-label" class="mono font-semibold text-slate-800">6 dB</span>
              </div>
              <input id="snr-slider" type="range" min="-6" max="24" step="6" value="6" class="w-full cursor-pointer" />
              <div class="flex justify-between text-[10px] text-slate-400 mono mt-0.5">
                <span>-6 dB</span><span>0</span><span>6</span><span>12</span><span>18</span><span>24 dB</span>
              </div>
            </div>
          </div>
        </section>

        <!-- 3. Acceptance Gate Threshold Control -->
        <section class="bg-white rounded-xl border border-slate-200 shadow-sm p-5">
          <div class="flex items-center justify-between mb-1">
            <h2 class="text-sm font-semibold text-slate-800 uppercase tracking-wider">3. Acceptance Threshold (u)</h2>
            <span id="threshold-val-label" class="mono text-xs font-bold px-2 py-0.5 rounded bg-slate-100 text-slate-800">0.5000</span>
          </div>
          <p class="text-[11px] text-slate-500 mb-2.5">
            Accept heart rate if estimated reliability <span class="mono">q(x) &ge; u</span> (Error &le; 5 bpm tolerance).
          </p>
          <input id="threshold-slider" type="range" min="0" max="1" step="0.005" value="0.50" class="w-full cursor-pointer" />
          <div class="flex flex-wrap gap-1.5 mt-2.5">
            <button type="button" data-thresh="0.0314" class="thresh-preset px-2.5 py-1 rounded-md text-[11px] font-medium bg-sky-50 hover:bg-sky-100 text-sky-700 border border-sky-200 transition">
              Paper Val Threshold (0.0314)
            </button>
            <button type="button" data-thresh="0.5000" class="thresh-preset px-2.5 py-1 rounded-md text-[11px] font-medium bg-slate-100 hover:bg-slate-200 text-slate-700 border border-slate-200 transition">
              Balanced (0.50)
            </button>
            <button type="button" data-thresh="0.7500" class="thresh-preset px-2.5 py-1 rounded-md text-[11px] font-medium bg-slate-100 hover:bg-slate-200 text-slate-700 border border-slate-200 transition">
              Strict Clinical (0.75)
            </button>
          </div>
        </section>

      </aside>

      <!-- RIGHT MAIN PANEL: Decision Banner, ECG Canvas, Dual Models & PSD -->
      <div class="lg:col-span-8 space-y-5">

        <!-- Clinical Decision & Reliability Gate Banner -->
        <section id="decision-banner" class="rounded-xl border-2 p-5 shadow-sm transition-colors bg-emerald-50/80 border-emerald-500">
          <div class="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
            <div class="flex items-start gap-3.5">
              <div id="decision-icon-wrap" class="w-11 h-11 rounded-xl flex items-center justify-center shrink-0 bg-emerald-600 text-white shadow-sm">
                <svg id="decision-icon-accept" class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7" />
                </svg>
                <svg id="decision-icon-reject" class="w-6 h-6 hidden" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
                </svg>
              </div>
              <div>
                <div class="flex items-center gap-2 flex-wrap">
                  <span id="decision-badge" class="px-2.5 py-0.5 rounded-md text-xs font-bold uppercase tracking-wider bg-emerald-600 text-white">
                    ACCEPT &bull; REPORT ESTIMATE
                  </span>
                  <span id="decision-subtag" class="text-xs font-medium text-emerald-800">
                    Reliability q(x) satisfies threshold u
                  </span>
                </div>
                <h3 id="decision-headline" class="text-lg sm:text-xl font-bold text-slate-900 mt-1">
                  Estimated Heart Rate: 74.8 bpm
                </h3>
                <p id="decision-explanation" class="text-xs text-slate-600 mt-0.5">
                  Primary (5–20 Hz) and secondary (8–30 Hz) detectors agree within tolerance. Safe to log in community health record.
                </p>
              </div>
            </div>

            <!-- Key Telemetry Pills -->
            <div class="grid grid-cols-3 gap-2 shrink-0 bg-white/90 p-2.5 rounded-xl border border-slate-200/80">
              <div class="px-2">
                <span class="block text-[10px] uppercase tracking-wider text-slate-400 font-semibold">Primary h&#8321;</span>
                <span id="metric-h1" class="mono text-sm sm:text-base font-bold text-slate-900">74.8</span>
                <span class="text-[10px] text-slate-500">bpm</span>
              </div>
              <div class="px-2 border-l border-slate-200">
                <span class="block text-[10px] uppercase tracking-wider text-slate-400 font-semibold">Secondary h&#8322;</span>
                <span id="metric-h2" class="mono text-sm sm:text-base font-bold text-slate-700">74.8</span>
                <span class="text-[10px] text-slate-500">bpm</span>
              </div>
              <div class="px-2 border-l border-slate-200">
                <span class="block text-[10px] uppercase tracking-wider text-slate-400 font-semibold">Disagree D</span>
                <span id="metric-disagree" class="mono text-sm sm:text-base font-bold text-sky-700">0.0</span>
                <span class="text-[10px] text-slate-500">bpm</span>
              </div>
            </div>
          </div>
        </section>

        <!-- Live Interactive 10s ECG Waveform Viewer -->
        <section class="bg-white rounded-xl border border-slate-200 shadow-sm p-5">
          <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-2 mb-3">
            <div>
              <h2 class="text-sm font-semibold text-slate-800">10-Second Analysis Window (250 Hz &bull; 2,500 Samples)</h2>
              <p class="text-[11px] text-slate-500">
                Markers show detected R-peaks (&ge; 0.35s / 0.28s separation, 0.40s boundary guard excluded).
              </p>
            </div>
            <!-- View Mode Switcher -->
            <div class="inline-flex rounded-lg bg-slate-100 p-1 border border-slate-200 self-start">
              <button type="button" data-view="raw" class="view-btn px-2.5 py-1 rounded-md text-xs font-medium bg-white text-slate-900 shadow-sm">
                Observed ECG
              </button>
              <button type="button" data-view="bp1" class="view-btn px-2.5 py-1 rounded-md text-xs font-medium text-slate-600 hover:text-slate-900">
                5–20 Hz (Det 1)
              </button>
              <button type="button" data-view="bp2" class="view-btn px-2.5 py-1 rounded-md text-xs font-medium text-slate-600 hover:text-slate-900">
                8–30 Hz (Det 2)
              </button>
            </div>
          </div>

          <div class="relative w-full h-60 sm:h-64 bg-slate-950 rounded-xl overflow-hidden border border-slate-800">
            <canvas id="ecg-canvas"></canvas>
          </div>

          <!-- Legend -->
          <div class="flex flex-wrap items-center justify-between gap-3 mt-3 text-xs text-slate-600">
            <div class="flex flex-wrap items-center gap-4">
              <span class="inline-flex items-center gap-1.5">
                <span class="w-3 h-0.5 bg-sky-400 inline-block"></span> Waveform
              </span>
              <span class="inline-flex items-center gap-1.5">
                <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 inline-block"></span> Detector 1 Peaks (5–20 Hz, 2.15&sigma;) [<strong id="n1-count" class="mono">0</strong>]
              </span>
              <span class="inline-flex items-center gap-1.5">
                <span class="w-2.5 h-2.5 rotate-45 bg-amber-400 inline-block"></span> Detector 2 Peaks (8–30 Hz, 1.6&sigma;) [<strong id="n2-count" class="mono">0</strong>]
              </span>
            </div>
            <span class="text-[11px] text-slate-400">Shaded edges: 0.4s boundary exclusion zone</span>
          </div>
        </section>

        <!-- Dual Random Forest Outputs: Explanatory Noise vs Task Reliability -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-5">

          <!-- Model 1: Explanatory Noise Classifier -->
          <section class="bg-white rounded-xl border border-slate-200 shadow-sm p-5 flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between mb-1">
                <h2 class="text-sm font-semibold text-slate-800">Model 1: Noise Classifier</h2>
                <span class="text-[11px] font-medium px-2 py-0.5 rounded bg-slate-100 text-slate-600">10 Features</span>
              </div>
              <p class="text-[11px] text-slate-500 mb-4">
                Explanatory diagnosis of disturbance mechanism (does not directly gate heart rate).
              </p>

              <div id="noise-bars-container" class="space-y-2.5">
                <!-- Populated dynamically by JS -->
              </div>
            </div>

            <div class="mt-4 pt-3 border-t border-slate-100 flex items-center justify-between text-xs">
              <span class="text-slate-500">Dominant Disturbance:</span>
              <span id="dominant-noise-badge" class="font-bold text-slate-800 px-2 py-0.5 rounded bg-slate-100">Clean</span>
            </div>
          </section>

          <!-- Model 2: Task Reliability Estimator & Spectral Features -->
          <section class="bg-white rounded-xl border border-slate-200 shadow-sm p-5 flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between mb-1">
                <h2 class="text-sm font-semibold text-slate-800">Model 2: Task Reliability Gate</h2>
                <span class="text-[11px] font-medium px-2 py-0.5 rounded bg-sky-50 text-sky-700">15 Features</span>
              </div>
              <p class="text-[11px] text-slate-500 mb-3">
                Estimates <span class="mono">q(x) = P(|h&#8321; &minus; h*| &le; 5 bpm)</span> using spectral context + detector disagreement.
              </p>

              <!-- Reliability Gauge Bar -->
              <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200 mb-4">
                <div class="flex justify-between items-baseline mb-1.5">
                  <span class="text-xs font-semibold text-slate-700">Reliability Probability q(x)</span>
                  <span id="q-prob-display" class="mono text-lg font-bold text-emerald-600">0.960</span>
                </div>
                <div class="relative w-full h-4 bg-slate-200 rounded-full overflow-hidden">
                  <div id="q-prob-bar" class="h-full bg-emerald-500 transition-all duration-300" style="width: 96%;"></div>
                  <!-- Threshold Marker -->
                  <div id="u-thresh-marker" class="absolute top-0 bottom-0 w-0.5 bg-slate-900 z-10" style="left: 50%;"></div>
                </div>
                <div class="flex justify-between text-[10px] text-slate-500 mono mt-1">
                  <span>0.00 (Unreliable)</span>
                  <span id="u-marker-label">Threshold u = 0.50</span>
                  <span>1.00</span>
                </div>
              </div>

              <!-- Key Extracted Features Table -->
              <div class="grid grid-cols-2 gap-2 text-xs">
                <div class="p-2 rounded-lg bg-slate-50 border border-slate-100">
                  <span class="block text-[10px] text-slate-400">60 Hz Band [58–62 Hz]</span>
                  <span id="feat-60hz" class="mono font-semibold text-slate-800">0.2%</span>
                </div>
                <div class="p-2 rounded-lg bg-slate-50 border border-slate-100">
                  <span class="block text-[10px] text-slate-400">QRS Band [5–20 Hz]</span>
                  <span id="feat-qrs" class="mono font-semibold text-slate-800">48.5%</span>
                </div>
                <div class="p-2 rounded-lg bg-slate-50 border border-slate-100">
                  <span class="block text-[10px] text-slate-400">Baseline [0–0.7 Hz]</span>
                  <span id="feat-bw" class="mono font-semibold text-slate-800">4.1%</span>
                </div>
                <div class="p-2 rounded-lg bg-slate-50 border border-slate-100">
                  <span class="block text-[10px] text-slate-400">Fisher Kurtosis</span>
                  <span id="feat-kurt" class="mono font-semibold text-slate-800">12.40</span>
                </div>
              </div>
            </div>

            <div class="mt-4 pt-3 border-t border-slate-100 text-[11px] text-slate-500">
              Note: Narrowband 60 Hz interference is attenuated by the 5–20 Hz filter, preserving reliability even when noise is present.
            </div>
          </section>

        </div>

        <!-- Welch Power Spectral Density (PSD) Chart -->
        <section class="bg-white rounded-xl border border-slate-200 shadow-sm p-5">
          <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-1 mb-3">
            <div>
              <h2 class="text-sm font-semibold text-slate-800">Welch Power Spectral Density (0 – 125 Hz)</h2>
              <p class="text-[11px] text-slate-500">1,000-sample Hann segments &bull; Highlights QRS passband (5–20 Hz) &amp; Philippine Grid band (58–62 Hz)</p>
            </div>
            <div class="flex items-center gap-3 text-[11px]">
              <span class="inline-flex items-center gap-1 text-emerald-700 font-medium">
                <span class="w-2.5 h-2.5 rounded-sm bg-emerald-500/25 border border-emerald-500"></span> 5–20 Hz QRS
              </span>
              <span class="inline-flex items-center gap-1 text-amber-700 font-medium">
                <span class="w-2.5 h-2.5 rounded-sm bg-amber-500/30 border border-amber-500"></span> 58–62 Hz (PH Grid)
              </span>
            </div>
          </div>
          <div class="relative w-full h-44 bg-slate-950 rounded-xl overflow-hidden border border-slate-800">
            <canvas id="psd-canvas"></canvas>
          </div>
        </section>

      </div>
    </div>
  </main>

  <!-- Toast / Non-Blocking Message Notification -->
  <div id="toast-box" class="fixed bottom-4 right-4 z-50 hidden max-w-sm bg-slate-900 text-white text-xs px-4 py-3 rounded-xl shadow-lg border border-slate-700"></div>

  <script>
    // =========================================================================
    // 1. CONSTANTS & STATE
    // =========================================================================
    const TARGET_FS = 250;
    const WIN_SEC = 10.0;
    const WIN_SAMPLES = TARGET_FS * WIN_SEC; // 2,500 samples
    const NOISE_CLASSES = ["Clean", "Baseline", "Muscle", "Power line", "Motion"];

    const state = {
      recordName: "MIT-BIH Sample (Clean)",
      sourceFs: 360,
      channelsData: [[], []], // Raw channels at sourceFs
      selectedChannel: 0,
      resampledSignal: [],    // Full recording resampled to 250 Hz
      windowStartSec: 0,
      stressNoiseType: "None",
      stressSnrDb: 6,
      thresholdU: 0.50,
      viewMode: "raw",        // 'raw' | 'bp1' | 'bp2'
      noiseRF: null,
      relRF: null,
      lastAnalysis: null
    };

    function showToast(msg) {
      const box = document.getElementById("toast-box");
      box.textContent = msg;
      box.classList.remove("hidden");
      clearTimeout(window._toastTimer);
      window._toastTimer = setTimeout(() => box.classList.add("hidden"), 4200);
    }

    // Deterministic PRNG for reproducible training & noise injection
    function mulberry32(seed) {
      return function() {
        let t = seed += 0x6D2B79F5;
        t = Math.imul(t ^ t >>> 15, t | 1);
        t ^= t + Math.imul(t ^ t >>> 7, t | 61);
        return ((t ^ t >>> 14) >>> 0) / 4294967296;
      };
    }

    function randNormal(rng) {
      const u1 = Math.max(1e-12, rng());
      const u2 = rng();
      return Math.sqrt(-2.0 * Math.log(u1)) * Math.cos(2.0 * Math.PI * u2);
    }

    // =========================================================================
    // 2. SYNTHETIC PQRST & NOISE GENERATOR (Section 4.1)
    // =========================================================================
    const WAVES = [
      { a: 0.12,  d: -0.190, w: 0.045 }, // P
      { a: -0.16, d: -0.035, w: 0.012 }, // Q
      { a: 1.00,  d: 0.000,  w: 0.014 }, // R
      { a: -0.24, d: 0.035,  w: 0.014 }, // S
      { a: 0.28,  d: 0.250,  w: 0.070 }  // T
    ];

    function generateCleanECG(hrBpm, durationSec, fs, rng) {
      const nSamples = Math.floor(durationSec * fs);
      const ampScale = WAVES.map(() => 0.8 + 0.4 * rng());
      const widScale = WAVES.map(() => 0.85 + 0.3 * rng());

      const taus = [];
      let tCurr = -0.5;
      while (tCurr <= durationSec + 0.5) {
        taus.push(tCurr);
        const eps = 0.025 * randNormal(rng);
        const dt = Math.max(0.32, (60.0 / hrBpm) * (1.0 + eps));
        tCurr += dt;
      }

      const inWin = taus.filter(t => t >= 0 && t <= durationSec);
      let hRef = hrBpm;
      if (inWin.length >= 2) {
        let sumDt = 0;
        for (let i = 0; i < inWin.length - 1; i++) sumDt += (inWin[i + 1] - inWin[i]);
        hRef = 60.0 / (sumDt / (inWin.length - 1));
      }

      const sig = new Float64Array(nSamples);
      for (let i = 0; i < nSamples; i++) {
        const t = i / fs;
        let val = 0.0;
        for (let b = 0; b < taus.length; b++) {
          const tau = taus[b];
          if (Math.abs(t - tau) > 0.6) continue;
          for (let m = 0; m < 5; m++) {
            const z = (t - tau - WAVES[m].d) / (WAVES[m].w * widScale[m]);
            if (Math.abs(z) < 5.0) {
              val += (WAVES[m].a * ampScale[m]) * Math.exp(-0.5 * z * z);
            }
          }
        }
        sig[i] = val;
      }
      return { sig, hRef };
    }

    function generateNoise(noiseType, nSamples, fs, rng) {
      const raw = new Float64Array(nSamples);
      if (noiseType === "Clean" || noiseType === "None") return raw;

      if (noiseType === "Power line") {
        // Philippine 60 Hz supply frequency: f0 ~ U(59.8, 60.2) Hz
        const f0 = 59.8 + 0.4 * rng();
        const phi = 2.0 * Math.PI * rng();
        for (let i = 0; i < nSamples; i++) {
          raw[i] = Math.sin(2.0 * Math.PI * f0 * (i / fs) + phi);
        }
      } else if (noiseType === "Baseline") {
        // Low-frequency wander (< 0.7 Hz) modeling MIT-BIH 'bw'
        const f1 = 0.12 + 0.23 * rng();
        const f2 = 0.40 + 0.28 * rng();
        const p1 = 6.28 * rng(), p2 = 6.28 * rng();
        for (let i = 0; i < nSamples; i++) {
          const t = i / fs;
          raw[i] = Math.sin(2 * Math.PI * f1 * t + p1) + 0.6 * Math.sin(2 * Math.PI * f2 * t + p2);
        }
      } else if (noiseType === "Muscle") {
        // High-frequency broadband EMG artifact modeling MIT-BIH 'ma'
        const center = 1.0 + (nSamples / fs - 2.0) * rng();
        const width = 1.5 + 2.5 * rng();
        let prev = 0.0;
        for (let i = 0; i < nSamples; i++) {
          const t = i / fs;
          const env = 0.4 + 0.8 * Math.exp(-0.5 * Math.pow((t - center) / width, 2));
          const w = randNormal(rng);
          const hp = w - 0.65 * prev;
          prev = w;
          raw[i] = env * hp;
        }
      } else if (noiseType === "Motion") {
        // Electrode motion transients & QRS-band artifacts modeling MIT-BIH 'em'
        const b1 = 0.6 + 2.0 * rng();
        const p1 = 6.28 * rng();
        const dur = nSamples / fs;
        const s1 = 0.2 * dur + 0.3 * dur * rng();
        const s2 = 0.55 * dur + 0.3 * dur * rng();
        for (let i = 0; i < nSamples; i++) {
          const t = i / fs;
          let val = Math.sin(2 * Math.PI * b1 * t + p1);
          if (Math.abs(t - s1) < 0.65) {
            val += 2.3 * Math.sin(2 * Math.PI * 6.5 * t) * Math.exp(-4.0 * Math.pow(t - s1, 2));
          }
          if (Math.abs(t - s2) < 0.65) {
            val -= 2.6 * Math.sin(2 * Math.PI * 8.2 * t) * Math.exp(-4.0 * Math.pow(t - s2, 2));
          }
          raw[i] = val;
        }
      }

      // Center noise (zero mean)
      let mean = 0;
      for (let i = 0; i < nSamples; i++) mean += raw[i];
      mean /= nSamples;
      for (let i = 0; i < nSamples; i++) raw[i] -= mean;
      return raw;
    }

    function injectNoise(cleanSig, noiseSig, noiseType, snrDb) {
      const n = cleanSig.length;
      const out = new Float64Array(n);
      if (noiseType === "Clean" || noiseType === "None") {
        out.set(cleanSig);
        return out;
      }
      let pS = 0, pN = 0;
      for (let i = 0; i < n; i++) {
        pS += cleanSig[i] * cleanSig[i];
        pN += noiseSig[i] * noiseSig[i];
      }
      pS /= n;
      pN /= n;
      if (pN < 1e-12) {
        out.set(cleanSig);
        return out;
      }
      const alpha = Math.sqrt(pS / (pN * Math.pow(10.0, snrDb / 10.0)));
      for (let i = 0; i < n; i++) {
        out[i] = cleanSig[i] + alpha * noiseSig[i];
      }
      return out;
    }

    // =========================================================================
    // 3. PHYSIONET WFDB FORMAT 212 & CSV/TXT PARSER + RESAMPLER (Section 3.2)
    // =========================================================================
    function decodeWFDB212(arrayBuffer) {
      const bytes = new Uint8Array(arrayBuffer);
      const numTriplets = Math.floor(bytes.length / 3);
      const ch0 = new Float64Array(numTriplets);
      const ch1 = new Float64Array(numTriplets);

      for (let i = 0; i < numTriplets; i++) {
        const b0 = bytes[i * 3];
        const b1 = bytes[i * 3 + 1];
        const b2 = bytes[i * 3 + 2];

        let s0 = b0 | ((b1 & 0x0F) << 8);
        if (s0 & 0x800) s0 -= 0x1000;

        let s1 = b2 | ((b1 & 0xF0) << 4);
        if (s1 & 0x800) s1 -= 0x1000;

        ch0[i] = s0 / 200.0;
        ch1[i] = s1 / 200.0;
      }
      return [ch0, ch1];
    }

    function parseHeaderFile(text) {
      const lines = text.split(/\r?\n/).map(l => l.trim()).filter(l => l && !l.startsWith("#"));
      if (lines.length === 0) return null;
      const parts = lines[0].split(/\s+/);
      const fs = parts.length >= 3 ? parseFloat(parts[2]) : NaN;
      return !isNaN(fs) && fs > 0 ? { fs } : null;
    }

    function parseTextECG(text) {
      const lines = text.split(/\r?\n/).map(l => l.trim()).filter(l => l && !l.startsWith("#"));
      const ch0 = [];
      const ch1 = [];
      for (const line of lines) {
        const cols = line.split(/[\s,;]+/).map(Number).filter(v => !isNaN(v));
        if (cols.length === 0) continue;
        if (cols.length >= 3) {
          ch0.push(cols[1]);
          ch1.push(cols[2]);
        } else if (cols.length === 2) {
          ch0.push(cols[1]);
          ch1.push(cols[0]);
        } else {
          ch0.push(cols[0]);
          ch1.push(cols[0]);
        }
      }
      return [new Float64Array(ch0), new Float64Array(ch1)];
    }

    function resampleTo250Hz(signal, sourceFs) {
      if (sourceFs === TARGET_FS) return Float64Array.from(signal);
      const ratio = sourceFs / TARGET_FS;
      const outLen = Math.floor(signal.length / ratio);
      const out = new Float64Array(outLen);
      for (let i = 0; i < outLen; i++) {
        const srcIdx = i * ratio;
        const idx0 = Math.floor(srcIdx);
        const idx1 = Math.min(signal.length - 1, idx0 + 1);
        const frac = srcIdx - idx0;
        out[i] = signal[idx0] * (1.0 - frac) + signal[idx1] * frac;
      }
      return out;
    }

    // =========================================================================
    // 4. SIGNAL PROCESSING & FEATURE EXTRACTION (Section 4.2 & 4.3)
    // =========================================================================
    function designBiquadBP(fLow, fHigh, fs) {
      const f0 = Math.sqrt(fLow * fHigh);
      const bw = fHigh - fLow;
      const w0 = 2.0 * Math.PI * f0 / fs;
      const q = f0 / bw;
      const alpha = Math.sin(w0) / (2.0 * q);

      const b0 = alpha, b1 = 0.0, b2 = -alpha;
      const a0 = 1.0 + alpha, a1 = -2.0 * Math.cos(w0), a2 = 1.0 - alpha;
      return [b0 / a0, b1 / a0, b2 / a0, a1 / a0, a2 / a0];
    }

    function applyBiquad(sig, coeffs) {
      const [b0, b1, b2, a1, a2] = coeffs;
      const out = new Float64Array(sig.length);
      let x1 = 0, x2 = 0, y1 = 0, y2 = 0;
      for (let i = 0; i < sig.length; i++) {
        const x0 = sig[i];
        const y0 = b0 * x0 + b1 * x1 + b2 * x2 - a1 * y1 - a2 * y2;
        out[i] = y0;
        x2 = x1; x1 = x0;
        y2 = y1; y1 = y0;
      }
      return out;
    }

    function filtfiltBP(sig, fLow, fHigh) {
      const coeffs = designBiquadBP(fLow, fHigh, TARGET_FS);
      let y = Float64Array.from(sig);
      for (let stage = 0; stage < 3; stage++) {
        y = applyBiquad(y, coeffs);
        y.reverse();
        y = applyBiquad(y, coeffs);
        y.reverse();
      }
      return y;
    }

    function stdDev(arr) {
      let sum = 0;
      for (let i = 0; i < arr.length; i++) sum += arr[i];
      const mean = sum / arr.length;
      let sq = 0;
      for (let i = 0; i < arr.length; i++) sq += (arr[i] - mean) * (arr[i] - mean);
      return Math.sqrt(sq / arr.length);
    }

    function median(arr) {
      if (arr.length === 0) return 0;
      const sorted = [...arr].sort((a, b) => a - b);
      const mid = Math.floor(sorted.length / 2);
      return sorted.length % 2 !== 0 ? sorted[mid] : 0.5 * (sorted[mid - 1] + sorted[mid]);
    }

    function detectPeaks(filteredSig, promMult, minDistSec = 0.28) {
      const minDist = Math.round(minDistSec * TARGET_FS);
      const margin = Math.round(0.40 * TARGET_FS);  // 100 samples
      const core = filteredSig.slice(margin, filteredSig.length - margin);
      const sd = stdDev(core);
      const promThresh = promMult * sd;
      const winHalf = Math.round(0.35 * TARGET_FS);

      const candidates = [];
      for (let i = 1; i < filteredSig.length - 1; i++) {
        if (filteredSig[i] > filteredSig[i - 1] && filteredSig[i] >= filteredSig[i + 1]) {
          let leftMin = filteredSig[i];
          for (let j = Math.max(0, i - winHalf); j < i; j++) {
            if (filteredSig[j] < leftMin) leftMin = filteredSig[j];
          }
          let rightMin = filteredSig[i];
          for (let j = i + 1; j <= Math.min(filteredSig.length - 1, i + winHalf); j++) {
            if (filteredSig[j] < rightMin) rightMin = filteredSig[j];
          }
          const prom = filteredSig[i] - Math.max(leftMin, rightMin);
          if (prom >= promThresh) {
            candidates.push({ val: filteredSig[i], idx: i });
          }
        }
      }

      candidates.sort((a, b) => b.val - a.val);
      const selected = [];
      for (const c of candidates) {
        if (selected.every(s => Math.abs(c.idx - s) >= minDist)) {
          selected.push(c.idx);
        }
      }

      const validPeaks = selected
        .filter(idx => idx >= margin && idx <= filteredSig.length - margin)
        .sort((a, b) => a - b);

      if (validPeaks.length >= 2) {
        const diffs = [];
        for (let k = 0; k < validPeaks.length - 1; k++) {
          diffs.push(validPeaks[k + 1] - validPeaks[k]);
        }
        const hrEst = (60.0 * TARGET_FS) / median(diffs);
        return { hr: hrEst, count: validPeaks.length, ok: true, peaks: validPeaks };
      }
      return { hr: 0.0, count: validPeaks.length, ok: false, peaks: validPeaks };
    }

    // Precompute Goertzel trigonometric tables for 1000-sample Welch PSD (df = 0.25 Hz)
    const SEG_LEN = 1000;
    const N_BINS = 501; // 0 to 125 Hz
    const HANN_WIN = new Float64Array(SEG_LEN);
    const COS_TABLE = new Float64Array(N_BINS);
    const SIN_TABLE = new Float64Array(N_BINS);
    for (let n = 0; n < SEG_LEN; n++) {
      HANN_WIN[n] = 0.5 * (1.0 - Math.cos(2.0 * Math.PI * n / (SEG_LEN - 1)));
    }
    for (let k = 0; k < N_BINS; k++) {
      const w = 2.0 * Math.PI * k / SEG_LEN;
      COS_TABLE[k] = Math.cos(w);
      SIN_TABLE[k] = Math.sin(w);
    }

    function computeWelchPSD(sig) {
      const starts = [0, 500, 1000, 1500];
      const psd = new Float64Array(N_BINS);
      const seg = new Float64Array(SEG_LEN);

      for (const st of starts) {
        for (let n = 0; n < SEG_LEN; n++) {
          seg[n] = sig[st + n] * HANN_WIN[n];
        }
        for (let k = 0; k < N_BINS; k++) {
          const cosW = COS_TABLE[k];
          const sinW = SIN_TABLE[k];
          const coeff = 2.0 * cosW;
          let sPrev = 0.0, sPrev2 = 0.0;
          for (let n = 0; n < SEG_LEN; n++) {
            const s = seg[n] + coeff * sPrev - sPrev2;
            sPrev2 = sPrev;
            sPrev = s;
          }
          const real = sPrev - sPrev2 * cosW;
          const imag = sPrev2 * sinW;
          psd[k] += (real * real + imag * imag);
        }
      }

      let totalPower = 1e-12;
      for (let k = 0; k < N_BINS; k++) totalPower += psd[k];

      const sumBand = (b0, b1) => {
        let s = 0;
        for (let k = b0; k < b1; k++) s += psd[k];
        return s / totalPower;
      };

      const bandPowers = [
        sumBand(0, 3),     // [0, 0.75) Hz
        sumBand(3, 20),    // [0.75, 5) Hz
        sumBand(20, 80),   // [5, 20) Hz
        sumBand(80, 180),  // [20, 45) Hz
        sumBand(232, 249), // [58, 62] Hz (Philippine 60 Hz grid)
        sumBand(180, 501)  // [45, 125) Hz
      ];

      return { psd, bandPowers, totalPower };
    }

    function extractFeatures(sig) {
      const { psd, bandPowers, totalPower } = computeWelchPSD(sig);

      let meanV = 0;
      for (let i = 0; i < sig.length; i++) meanV += sig[i];
      meanV /= sig.length;

      const sdRaw = stdDev(sig) + 1e-12;
      let m4 = 0;
      for (let i = 0; i < sig.length; i++) m4 += Math.pow(sig[i] - meanV, 4);
      m4 /= sig.length;
      const kurtosis = (m4 / Math.pow(sdRaw, 4)) - 3.0;

      const diffs = new Float64Array(sig.length - 1);
      let madSum = 0;
      for (let i = 0; i < sig.length - 1; i++) {
        const d = sig[i + 1] - sig[i];
        diffs[i] = d;
        madSum += Math.abs(d);
      }
      const sdDiff = stdDev(diffs);
      const madDiff = madSum / diffs.length;

      const noiseFeats = [...bandPowers, sdRaw, kurtosis, sdDiff, madDiff]; // 10 features

      const bp1 = filtfiltBP(sig, 5.0, 20.0);
      const bp2 = filtfiltBP(sig, 8.0, 30.0);
      const det1 = detectPeaks(bp1, 2.15, 0.35);
      const det2 = detectPeaks(bp2, 1.60, 0.28);

      const disagreement = (det1.ok && det2.ok) ? Math.abs(det1.hr - det2.hr) : 200.0;
      const relFeats = [...noiseFeats, det1.hr, det2.hr, disagreement, det1.count, det2.count]; // 15 features

      return {
        noiseFeats,
        relFeats,
        det1,
        det2,
        disagreement,
        bp1,
        bp2,
        psd,
        totalPower,
        bandPowers,
        kurtosis
      };
    }

    // =========================================================================
    // 5. RANDOM FOREST CLASSIFIER (Section 4.3)
    // =========================================================================
    class DecisionTree {
      constructor(maxDepth, minLeaf, nSubfeatures, rng) {
        this.maxDepth = maxDepth;
        this.minLeaf = minLeaf;
        this.nSubfeatures = nSubfeatures;
        this.rng = rng;
        this.root = null;
      }

      gini(y, nClasses) {
        const n = y.length;
        if (n === 0) return 0;
        const counts = new Array(nClasses).fill(0);
        for (let i = 0; i < n; i++) counts[y[i]]++;
        let sumSq = 0;
        for (let c = 0; c < nClasses; c++) {
          const p = counts[c] / n;
          sumSq += p * p;
        }
        return 1.0 - sumSq;
      }

      fit(X, y, nClasses) {
        this.nClasses = nClasses;
        this.root = this.build(X, y, 0);
      }

      build(X, y, depth) {
        const n = y.length;
        const counts = new Array(this.nClasses).fill(0);
        for (let i = 0; i < n; i++) counts[y[i]]++;
        const probs = counts.map(c => c / n);

        if (depth >= this.maxDepth || n < 2 * this.minLeaf || Math.max(...probs) === 1.0) {
          return { leaf: true, probs };
        }

        const nFeats = X[0].length;
        const indices = Array.from({ length: nFeats }, (_, i) => i);
        for (let i = nFeats - 1; i > 0; i--) {
          const j = Math.floor(this.rng() * (i + 1));
          [indices[i], indices[j]] = [indices[j], indices[i]];
        }
        const subFeats = indices.slice(0, this.nSubfeatures);

        let bestGain = 0;
        let bestSplit = null;
        const parentGini = this.gini(y, this.nClasses);

        for (const f of subFeats) {
          const vals = X.map(row => row[f]).sort((a, b) => a - b);
          const step = Math.max(1, Math.floor(vals.length / 10));
          for (let idx = 0; idx < vals.length - 1; idx += step) {
            if (vals[idx] === vals[idx + 1]) continue;
            const thresh = 0.5 * (vals[idx] + vals[idx + 1]);
            const lY = [], rY = [];
            for (let i = 0; i < n; i++) {
              if (X[i][f] <= thresh) lY.push(y[i]);
              else rY.push(y[i]);
            }
            if (lY.length < this.minLeaf || rY.length < this.minLeaf) continue;
            const wGini = (lY.length * this.gini(lY, this.nClasses) + rY.length * this.gini(rY, this.nClasses)) / n;
            const gain = parentGini - wGini;
            if (gain > bestGain) {
              bestGain = gain;
              bestSplit = { f, thresh };
            }
          }
        }

        if (!bestSplit) return { leaf: true, probs };

        const { f, thresh } = bestSplit;
        const lX = [], lY = [], rX = [], rY = [];
        for (let i = 0; i < n; i++) {
          if (X[i][f] <= thresh) { lX.push(X[i]); lY.push(y[i]); }
          else { rX.push(X[i]); rY.push(y[i]); }
        }

        return {
          leaf: false,
          f,
          thresh,
          left: this.build(lX, lY, depth + 1),
          right: this.build(rX, rY, depth + 1)
        };
      }

      predictProbaRow(row) {
        let node = this.root;
        while (!node.leaf) {
          node = row[node.f] <= node.thresh ? node.left : node.right;
        }
        return node.probs;
      }
    }

    class RandomForest {
      constructor(nTrees, maxDepth, minLeaf, seed) {
        this.nTrees = nTrees;
        this.maxDepth = maxDepth;
        this.minLeaf = minLeaf;
        this.rng = mulberry32(seed);
        this.trees = [];
      }

      fit(X, y, nClasses) {
        this.nClasses = nClasses;
        const n = X.length;
        const nSub = Math.max(1, Math.floor(Math.sqrt(X[0].length)));
        this.trees = [];
        for (let t = 0; t < this.nTrees; t++) {
          const bX = new Array(n), bY = new Array(n);
          for (let i = 0; i < n; i++) {
            const idx = Math.floor(this.rng() * n);
            bX[i] = X[idx];
            bY[i] = y[idx];
          }
          const dt = new DecisionTree(this.maxDepth, this.minLeaf, nSub, this.rng);
          dt.fit(bX, bY, nClasses);
          this.trees.push(dt);
        }
      }

      predictProba(row) {
        const avg = new Array(this.nClasses).fill(0);
        for (const dt of this.trees) {
          const p = dt.predictProbaRow(row);
          for (let c = 0; c < this.nClasses; c++) avg[c] += p[c];
        }
        return avg.map(v => v / this.nTrees);
      }
    }

    function trainFrameworkModels() {
      const rng = mulberry32(2026);
      const XNoise = [], yNoise = [];
      const XRel = [], yRel = [];
      const snrLevels = [-6, 0, 6, 12, 18, 24];

      for (let subj = 0; subj < 14; subj++) {
        const hrNom = 45.0 + 95.0 * rng();
        const { sig: cleanSig, hRef } = generateCleanECG(hrNom, WIN_SEC, TARGET_FS, rng);

        const variants = [{ nc: "Clean", snr: 99 }];
        for (let c = 1; c < NOISE_CLASSES.length; c++) {
          for (const snr of snrLevels) {
            variants.push({ nc: NOISE_CLASSES[c], snr });
          }
        }

        for (const v of variants) {
          const nSig = generateNoise(v.nc, WIN_SAMPLES, TARGET_FS, rng);
          const obs = injectNoise(cleanSig, nSig, v.nc, v.snr);
          const ext = extractFeatures(obs);

          XNoise.push(ext.noiseFeats);
          yNoise.push(NOISE_CLASSES.indexOf(v.nc));

          const isRel = (ext.det1.ok && Math.abs(ext.det1.hr - hRef) <= 5.0) ? 1 : 0;
          XRel.push(ext.relFeats);
          yRel.push(isRel);
        }
      }

      const noiseRF = new RandomForest(32, 8, 3, 405);
      noiseRF.fit(XNoise, yNoise, 5);

      const relRF = new RandomForest(32, 8, 5, 406);
      relRF.fit(XRel, yRel, 2);

      state.noiseRF = noiseRF;
      state.relRF = relRF;

      const badge = document.getElementById("model-status-badge");
      badge.className = "inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-medium bg-emerald-500/15 text-emerald-300 border border-emerald-500/30";
      badge.innerHTML = `<span class="w-2 h-2 rounded-full bg-emerald-400"></span> Dual RF Models Ready (350 Train Windows)`;
    }

    // =========================================================================
    // 6. SAMPLE PRESETS & RECORD MANAGEMENT
    // =========================================================================
    function loadSamplePreset(presetKey) {
      const rng = mulberry32(presetKey.split("").reduce((a, c) => a + c.charCodeAt(0), 100));
      const dur = 30.0;
      const fs = 360;
      const { sig: clean360 } = generateCleanECG(74.0, dur, fs, rng);

      let final360 = clean360;
      let label = "MIT-BIH Sample 100 (Clean)";

      if (presetKey === "nstdb_bw") {
        const n = generateNoise("Baseline", clean360.length, fs, rng);
        final360 = injectNoise(clean360, n, "Baseline", 0);
        label = "MIT-BIH + NSTDB 'bw' (0 dB)";
      } else if (presetKey === "nstdb_ma") {
        const n = generateNoise("Muscle", clean360.length, fs, rng);
        final360 = injectNoise(clean360, n, "Muscle", 0);
        label = "MIT-BIH + NSTDB 'ma' (0 dB)";
      } else if (presetKey === "nstdb_em") {
        const n = generateNoise("Motion", clean360.length, fs, rng);
        final360 = injectNoise(clean360, n, "Motion", 0);
        label = "MIT-BIH + NSTDB 'em' (0 dB)";
      } else if (presetKey === "ph_60hz") {
        const n = generateNoise("Power line", clean360.length, fs, rng);
        final360 = injectNoise(clean360, n, "Power line", 0);
        label = "MIT-BIH + PH 60 Hz Grid (0 dB)";
      }

      const ch1 = final360.map((v, i) => 0.75 * v + 0.03 * Math.sin(i * 0.05));
      state.recordName = label;
      state.sourceFs = fs;
      state.channelsData = [final360, ch1];
      state.selectedChannel = 0;
      document.getElementById("input-fs").value = "360";
      document.getElementById("input-channel").value = "0";
      document.getElementById("stress-noise-type").value = "None";
      state.stressNoiseType = "None";
      updateSnrControlState();
      refreshResampledSignal();
    }

    function refreshResampledSignal() {
      const rawCh = state.channelsData[state.selectedChannel] || state.channelsData[0];
      if (!rawCh || rawCh.length === 0) return;

      let resampled = resampleTo250Hz(rawCh, state.sourceFs);
      if (resampled.length < WIN_SAMPLES) {
        const padded = new Float64Array(WIN_SAMPLES);
        padded.set(resampled);
        resampled = padded;
      }

      state.resampledSignal = resampled;
      const totalSec = resampled.length / TARGET_FS;
      const maxStart = Math.max(0, Math.floor((totalSec - WIN_SEC) * 2) / 2);

      const slider = document.getElementById("window-slider");
      slider.max = maxStart.toFixed(1);
      if (state.windowStartSec > maxStart) state.windowStartSec = 0;
      slider.value = state.windowStartSec;

      document.getElementById("record-name").textContent = state.recordName;
      document.getElementById("record-fs-info").textContent = `${state.sourceFs} Hz → 250 Hz`;
      document.getElementById("record-duration").textContent = `totalSec.toFixed(1)s({resampled.length.toLocaleString()} samples)`;
      document.getElementById("max-time-label").textContent = `${totalSec.toFixed(1)}s`;

      evaluateCurrentWindow();
    }

    // =========================================================================
    // 7. WINDOW EVALUATION & UI RENDERING
    // =========================================================================
    function evaluateCurrentWindow() {
      if (!state.noiseRF || !state.relRF || state.resampledSignal.length < WIN_SAMPLES) return;

      const startIdx = Math.min(
        state.resampledSignal.length - WIN_SAMPLES,
        Math.round(state.windowStartSec * TARGET_FS)
      );
      const baseWindow = state.resampledSignal.slice(startIdx, startIdx + WIN_SAMPLES);

      let observedWindow = baseWindow;
      if (state.stressNoiseType !== "None") {
        const rng = mulberry32(Math.round(state.windowStartSec * 100) + state.stressSnrDb * 17 + 99);
        const nSig = generateNoise(state.stressNoiseType, WIN_SAMPLES, TARGET_FS, rng);
        observedWindow = injectNoise(baseWindow, nSig, state.stressNoiseType, state.stressSnrDb);
      }

      const ext = extractFeatures(observedWindow);
      const noiseProbs = state.noiseRF.predictProba(ext.noiseFeats);
      const relProbs = state.relRF.predictProba(ext.relFeats);
      const qProb = relProbs[1];

      state.lastAnalysis = {
        observedWindow,
        ext,
        noiseProbs,
        qProb
      };

      updateDashboardUI();
    }

    function updateDashboardUI() {
      const { ext, noiseProbs, qProb } = state.lastAnalysis;
      const u = state.thresholdU;
      // Engineering guard: reject if q(x) < u OR if detector disagreement exceeds 10 bpm
      const highDisagreement = ext.disagreement > 10.0;
      const accepted = (qProb >= u) && !highDisagreement;

      // Update Scrubber Labels
      document.getElementById("window-time-label").textContent =
        `${state.windowStartSec.toFixed(1)}s – ${(state.windowStartSec + WIN_SEC).toFixed(1)}s`;
      document.getElementById("threshold-val-label").textContent = u.toFixed(4);

      // Update Decision Banner
      const banner = document.getElementById("decision-banner");
      const iconWrap = document.getElementById("decision-icon-wrap");
      const iconAccept = document.getElementById("decision-icon-accept");
      const iconReject = document.getElementById("decision-icon-reject");
      const badge = document.getElementById("decision-badge");
      const subtag = document.getElementById("decision-subtag");
      const headline = document.getElementById("decision-headline");
      const explanation = document.getElementById("decision-explanation");

      if (accepted) {
        banner.className = "rounded-xl border-2 p-5 shadow-sm transition-colors bg-emerald-50/80 border-emerald-500";
        iconWrap.className = "w-11 h-11 rounded-xl flex items-center justify-center shrink-0 bg-emerald-600 text-white shadow-sm";
        iconAccept.classList.remove("hidden");
        iconReject.classList.add("hidden");
        badge.className = "px-2.5 py-0.5 rounded-md text-xs font-bold uppercase tracking-wider bg-emerald-600 text-white";
        badge.textContent = "ACCEPT • REPORT ESTIMATE";
        subtag.className = "text-xs font-medium text-emerald-800";
        subtag.textContent = `q(x) = qProb.toFixed(3)≥Thresholdu({u.toFixed(3)})`;
        headline.textContent = ext.det1.ok
          ? `Estimated Heart Rate: ${ext.det1.hr.toFixed(1)} bpm`
          : `Estimated Heart Rate: Undefined`;
        explanation.textContent =
          "Task reliability gate predicts primary rate error is within the ≤ 5 bpm engineering tolerance. Safe to retain.";
      } else {
        banner.className = "rounded-xl border-2 p-5 shadow-sm transition-colors bg-rose-50/90 border-rose-500";
        iconWrap.className = "w-11 h-11 rounded-xl flex items-center justify-center shrink-0 bg-rose-600 text-white shadow-sm";
        iconAccept.classList.add("hidden");
        iconReject.classList.remove("hidden");
        badge.className = "px-2.5 py-0.5 rounded-md text-xs font-bold uppercase tracking-wider bg-rose-600 text-white";
        badge.textContent = "REJECT • REQUEST REACQUISITION";
        subtag.className = "text-xs font-medium text-rose-800";
        subtag.textContent = highDisagreement
          ? `Detector disagreement D = ${ext.disagreement.toFixed(1)} bpm > 10 bpm limit`
          : `q(x) = qProb.toFixed(3)<Thresholdu({u.toFixed(3)})`;
        headline.textContent = ext.det1.ok
          ? `Suppressed Estimate: ${ext.det1.hr.toFixed(1)} bpm (High Error Risk)`
          : `Detector Failure: Insufficient R-Peaks Detected`;
        explanation.textContent =
          "In-band waveform corruption or detector disagreement exceeds reliability threshold. Reposition electrodes and reacquire 10s ECG.";
      }

      // Telemetry Metrics
      document.getElementById("metric-h1").textContent = ext.det1.ok ? ext.det1.hr.toFixed(1) : "ERR";
      document.getElementById("metric-h2").textContent = ext.det2.ok ? ext.det2.hr.toFixed(1) : "ERR";
      document.getElementById("metric-disagree").textContent = ext.disagreement.toFixed(1);
      document.getElementById("n1-count").textContent = ext.det1.count;
      document.getElementById("n2-count").textContent = ext.det2.count;

      // Model 1: Noise Class Probabilities
      const barsContainer = document.getElementById("noise-bars-container");
      let maxIdx = 0;
      for (let i = 1; i < 5; i++) if (noiseProbs[i] > noiseProbs[maxIdx]) maxIdx = i;

      const barColors = [
        "bg-emerald-500",
        "bg-sky-500",
        "bg-purple-500",
        "bg-amber-500",
        "bg-rose-500"
      ];

      barsContainer.innerHTML = NOISE_CLASSES.map((cls, i) => {
        const pct = (noiseProbs[i] * 100).toFixed(1);
        return `
          <div>
            <div class="flex justify-between text-xs mb-1">
              <span class="font-medium i===maxIdx?'text-slate-900font-semibold':'text-slate-600'">{cls}</span>
              <span class="mono text-slate-700">${pct}%</span>
            </div>
            <div class="w-full h-2 bg-slate-100 rounded-full overflow-hidden">
              <div class="h-full ${barColors[i]} transition-all duration-300" style="width: ${pct}%"></div>
            </div>
          </div>
        `;
      }).join("");

      document.getElementById("dominant-noise-badge").textContent =
        `NOISECLASSES[maxIdx]({(noiseProbs[maxIdx] * 100).toFixed(1)}%)`;

      // Model 2: Reliability Gauge & Feature Readouts
      const qDisplay = document.getElementById("q-prob-display");
      const qBar = document.getElementById("q-prob-bar");
      qDisplay.textContent = qProb.toFixed(4);
      qDisplay.className = `mono text-lg font-bold ${accepted ? "text-emerald-600" : "text-rose-600"}`;
      qBar.className = `h-full transition-all duration-300 ${accepted ? "bg-emerald-500" : "bg-rose-500"}`;
      qBar.style.width = `${(qProb * 100).toFixed(1)}%`;

      document.getElementById("u-thresh-marker").style.left = `${(u * 100).toFixed(1)}%`;
      document.getElementById("u-marker-label").textContent = `u = ${u.toFixed(3)}`;

      document.getElementById("feat-bw").textContent = `${(ext.bandPowers[0] * 100).toFixed(1)}%`;
      document.getElementById("feat-qrs").textContent = `${(ext.bandPowers[2] * 100).toFixed(1)}%`;
      document.getElementById("feat-60hz").textContent = `${(ext.bandPowers[4] * 100).toFixed(1)}%`;
      document.getElementById("feat-kurt").textContent = ext.kurtosis.toFixed(2);

      drawECGCanvas();
      drawPSDCanvas();
    }

    // =========================================================================
    // 8. HIGH-DPI CANVAS VISUALIZATIONS (ECG & WELCH PSD)
    // =========================================================================
    function setupCanvas(canvas) {
      const rect = canvas.parentElement.getBoundingClientRect();
      const dpr = window.devicePixelRatio || 1;
      canvas.width = rect.width * dpr;
      canvas.height = rect.height * dpr;
      const ctx = canvas.getContext("2d");
      ctx.scale(dpr, dpr);
      return { ctx, w: rect.width, h: rect.height };
    }

    function drawECGCanvas() {
      if (!state.lastAnalysis) return;
      const canvas = document.getElementById("ecg-canvas");
      const { ctx, w, h } = setupCanvas(canvas);
      const { observedWindow, ext } = state.lastAnalysis;

      const sig = state.viewMode === "bp1" ? ext.bp1
                : state.viewMode === "bp2" ? ext.bp2
                : observedWindow;

      ctx.fillStyle = "#020617";
      ctx.fillRect(0, 0, w, h);

      ctx.strokeStyle = "#0f172a";
      ctx.lineWidth = 1;
      for (let s = 0; s <= 50; s++) {
        const x = (s / 50) * w;
        ctx.beginPath();
        ctx.moveTo(x, 0);
        ctx.lineTo(x, h);
        ctx.stroke();
      }
      ctx.strokeStyle = "#1e293b";
      for (let s = 0; s <= 10; s++) {
        const x = (s / 10) * w;
        ctx.beginPath();
        ctx.moveTo(x, 0);
        ctx.lineTo(x, h);
        ctx.stroke();
      }

      const guardW = 0.04 * w;
      ctx.fillStyle = "rgba(244, 63, 94, 0.08)";
      ctx.fillRect(0, 0, guardW, h);
      ctx.fillRect(w - guardW, 0, guardW, h);

      let minV = Infinity, maxV = -Infinity;
      for (let i = 0; i < sig.length; i++) {
        if (sig[i] < minV) minV = sig[i];
        if (sig[i] > maxV) maxV = sig[i];
      }
      const span = Math.max(1e-6, maxV - minV);
      const padY = 22;
      const mapY = (v) => h - padY - ((v - minV) / span) * (h - 2 * padY);
      const mapX = (idx) => (idx / (sig.length - 1)) * w;

      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 1.6;
      ctx.beginPath();
      for (let i = 0; i < sig.length; i++) {
        const x = mapX(i);
        const y = mapY(sig[i]);
        if (i === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
      }
      ctx.stroke();

      ctx.fillStyle = "#34d399";
      for (const idx of ext.det1.peaks) {
        const x = mapX(idx);
        const y = mapY(sig[idx]);
        ctx.beginPath();
        ctx.arc(x, y, 4.5, 0, 2 * Math.PI);
        ctx.fill();
      }

      ctx.fillStyle = "#fbbf24";
      for (const idx of ext.det2.peaks) {
        const x = mapX(idx);
        const y = mapY(sig[idx]) - 8;
        ctx.beginPath();
        ctx.moveTo(x, y - 4);
        ctx.lineTo(x + 4, y);
        ctx.lineTo(x, y + 4);
        ctx.lineTo(x - 4, y);
        ctx.closePath();
        ctx.fill();
      }

      ctx.fillStyle = "#64748b";
      ctx.font = "10px 'JetBrains Mono', monospace";
      for (let s = 1; s < 10; s++) {
        ctx.fillText(`${(state.windowStartSec + s).toFixed(0)}s`, (s / 10) * w + 3, h - 6);
      }
    }

    function drawPSDCanvas() {
      if (!state.lastAnalysis) return;
      const canvas = document.getElementById("psd-canvas");
      const { ctx, w, h } = setupCanvas(canvas);
      const { psd } = state.lastAnalysis.ext;

      ctx.fillStyle = "#020617";
      ctx.fillRect(0, 0, w, h);

      const freqToX = (f) => (f / 125.0) * w;

      ctx.fillStyle = "rgba(16, 185, 129, 0.14)";
      ctx.fillRect(freqToX(5), 0, freqToX(20) - freqToX(5), h);

      ctx.fillStyle = "rgba(245, 158, 11, 0.22)";
      ctx.fillRect(freqToX(58), 0, freqToX(62) - freqToX(58), h);

      let maxP = 1e-12;
      for (let k = 0; k < psd.length; k++) if (psd[k] > maxP) maxP = psd[k];

      const dbVals = new Float64Array(psd.length);
      for (let k = 0; k < psd.length; k++) {
        const db = 10 * Math.log10((psd[k] + 1e-12) / maxP);
        dbVals[k] = Math.max(-60, db);
      }

      const padY = 18;
      const mapY = (db) => padY + ((0 - db) / 60.0) * (h - 2 * padY);

      ctx.beginPath();
      ctx.moveTo(0, h - padY);
      for (let k = 0; k < dbVals.length; k++) {
        const f = k * 0.25;
        ctx.lineTo(freqToX(f), mapY(dbVals[k]));
      }
      ctx.lineTo(w, h - padY);
      ctx.closePath();
      ctx.fillStyle = "rgba(56, 189, 248, 0.18)";
      ctx.fill();

      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      for (let k = 0; k < dbVals.length; k++) {
        const f = k * 0.25;
        const x = freqToX(f);
        const y = mapY(dbVals[k]);
        if (k === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
      }
      ctx.stroke();

      ctx.fillStyle = "#64748b";
      ctx.font = "10px 'JetBrains Mono', monospace";
      for (const f of [0, 5, 20, 45, 60, 90, 120]) {
        ctx.fillText(`${f}Hz`, freqToX(f) + 2, h - 5);
      }
    }

    // =========================================================================
    // 9. FILE UPLOAD HANDLERS & EVENT LISTENERS
    // =========================================================================
    async function handleUploadedFiles(fileList) {
      const files = Array.from(fileList);
      if (files.length === 0) return;

      let datFile = files.find(f => f.name.toLowerCase().endsWith(".dat"));
      let heaFile = files.find(f => f.name.toLowerCase().endsWith(".hea"));
      let txtFile = files.find(f => /\.(csv|txt|json)$/i.test(f.name));

      try {
        if (heaFile) {
          const heaText = await heaFile.text();
          const parsedHea = parseHeaderFile(heaText);
          if (parsedHea && parsedHea.fs) {
            state.sourceFs = parsedHea.fs;
            const fsSelect = document.getElementById("input-fs");
            const optExists = Array.from(fsSelect.options).some(o => Number(o.value) === parsedHea.fs);
            if (!optExists) {
              const opt = new Option(`${parsedHea.fs} Hz (From .hea)`, String(parsedHea.fs));
              fsSelect.add(opt);
            }
            fsSelect.value = String(parsedHea.fs);
          }
        }

        if (datFile) {
          const buf = await datFile.arrayBuffer();
          const [ch0, ch1] = decodeWFDB212(buf);
          if (ch0.length < 100) {
            showToast("Uploaded .dat file is too short to extract a valid ECG segment.");
            return;
          }
          state.recordName = datFile.name;
          state.channelsData = [ch0, ch1];
          state.windowStartSec = 0;
          showToast(`Decoded WFDB Format 212 (${datFile.name}): ${ch0.length.toLocaleString()} samples per channel.`);
          refreshResampledSignal();
        } else if (txtFile) {
          const text = await txtFile.text();
          let ch0, ch1;
          if (txtFile.name.toLowerCase().endsWith(".json")) {
            const parsed = JSON.parse(text);
            const arr = Array.isArray(parsed) ? parsed : (parsed.ecg || parsed.signal || parsed.data || []);
            ch0 = new Float64Array(arr.map(Number));
            ch1 = ch0;
          } else {
            [ch0, ch1] = parseTextECG(text);
          }
          if (ch0.length < 100) {
            showToast("Could not find enough numeric waveform samples in the uploaded text file.");
            return;
          }
          state.recordName = txtFile.name;
          state.channelsData = [ch0, ch1];
          state.windowStartSec = 0;
          showToast(`Loaded ${txtFile.name}: ${ch0.length.toLocaleString()} samples.`);
          refreshResampledSignal();
        } else if (heaFile) {
          showToast("Header (.hea) parsed. Please also select the matching .dat waveform file.");
        }
      } catch (err) {
        console.error(err);
        showToast("Error parsing uploaded PhysioNet file. Check format (WFDB 212 .dat or CSV/TXT).");
      }
    }

    function updateSnrControlState() {
      const wrap = document.getElementById("snr-control-wrap");
      if (state.stressNoiseType === "None") {
        wrap.classList.add("opacity-40", "pointer-events-none");
      } else {
        wrap.classList.remove("opacity-40", "pointer-events-none");
      }
    }

    window.addEventListener("DOMContentLoaded", () => {
      setTimeout(() => {
        trainFrameworkModels();
        loadSamplePreset("mit100");
      }, 60);

      const fileInput = document.getElementById("file-input");
      const dropZone = document.getElementById("drop-zone");

      fileInput.addEventListener("change", (e) => handleUploadedFiles(e.target.files));
      dropZone.addEventListener("dragover", (e) => {
        e.preventDefault();
        dropZone.classList.add("border-sky-500", "bg-sky-50");
      });
      dropZone.addEventListener("dragleave", () => {
        dropZone.classList.remove("border-sky-500", "bg-sky-50");
      });
      dropZone.addEventListener("drop", (e) => {
        e.preventDefault();
        dropZone.classList.remove("border-sky-500", "bg-sky-50");
        handleUploadedFiles(e.dataTransfer.files);
      });

      document.getElementById("input-fs").addEventListener("change", (e) => {
        state.sourceFs = Number(e.target.value);
        refreshResampledSignal();
      });
      document.getElementById("input-channel").addEventListener("change", (e) => {
        state.selectedChannel = Number(e.target.value);
        refreshResampledSignal();
      });

      document.querySelectorAll(".preset-btn").forEach(btn => {
        btn.addEventListener("click", () => loadSamplePreset(btn.dataset.preset));
      });

      document.getElementById("window-slider").addEventListener("input", (e) => {
        state.windowStartSec = Number(e.target.value);
        evaluateCurrentWindow();
      });

      document.getElementById("stress-noise-type").addEventListener("change", (e) => {
        state.stressNoiseType = e.target.value;
        updateSnrControlState();
        evaluateCurrentWindow();
      });
      document.getElementById("snr-slider").addEventListener("input", (e) => {
        state.stressSnrDb = Number(e.target.value);
        document.getElementById("snr-val-label").textContent = `${state.stressSnrDb} dB`;
        evaluateCurrentWindow();
      });

      document.getElementById("threshold-slider").addEventListener("input", (e) => {
        state.thresholdU = Number(e.target.value);
        updateDashboardUI();
      });
      document.querySelectorAll(".thresh-preset").forEach(btn => {
        btn.addEventListener("click", () => {
          state.thresholdU = Number(btn.dataset.thresh);
          document.getElementById("threshold-slider").value = state.thresholdU;
          updateDashboardUI();
        });
      });

      document.querySelectorAll(".view-btn").forEach(btn => {
        btn.addEventListener("click", () => {
          state.viewMode = btn.dataset.view;
          document.querySelectorAll(".view-btn").forEach(b => {
            b.className = "view-btn px-2.5 py-1 rounded-md text-xs font-medium text-slate-600 hover:text-slate-900";
          });
          btn.className = "view-btn px-2.5 py-1 rounded-md text-xs font-medium bg-white text-slate-900 shadow-sm";
          drawECGCanvas();
        });
      });

      window.addEventListener("resize", () => {
        drawECGCanvas();
        drawPSDCanvas();
      });
    });
  </script>
</body>
</html>

