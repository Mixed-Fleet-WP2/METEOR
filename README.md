# 🚀 model2sim

## 📝 Overview

**model2sim** is a Python-based tool for parsing, analyzing, and simulating models written in a custom modeling language. Powered by ANTLR4, it lets you define system models, parse them, and orchestrate their execution — all with easy history tracking.

---

## ✨ Features

- 🎯 **Grammar Logic Adapted to SOA Models:** Define Service-Oriented Architecture (SOA) models using a flexible, extensible grammar.
- ⚡ **ANTLR4 Parsing:** Robust parsing of model files with generated Python code.
- 🤖 **Action Orchestration:** Simulate or execute parsed actions.
- 🗂️ **History Logging:** Save parsed actions to timestamped JSON files for traceability.
- 🧩 **Extensible Workflow:** Easily add new grammars, output formats, or orchestration logic.

---

## 📁 Folder Structure

```
grammar/         # ANTLR4 grammar files & generated parser code
orchestrator/    # Orchestration logic for executing actions
history/         # Saved action histories (JSON)
run_mission.py   # Main script for parsing and running models
environment.yml  # Project dependencies
sample.mxf       # Example model file
```

---

## 🚦 Getting Started

### 1️⃣ Install Dependencies

```bash
conda env create -f environment.yml
conda activate sysmlParser 
```

### 2️⃣ Generate Parser Code (if grammar changes)

```bash
antlr4 -Dlanguage=Python3 grammar/Action.g4 grammar/Part.g4 grammar/CommonLexer.g4 -o grammar/
or (recomended)
antlr4 -Dlanguage=Python3 -visitor Action.g4
```

### 3️⃣ Run a Model

```bash
 python3  run_mission.py sample.mxf
```

Parsed actions will be saved in the `history/` folder.

---

## 🛠️ Extending

- ➕ Add new grammar rules in `grammar/*.g4`
- 🔄 Update orchestration logic in `orchestrator/orchestrator.py`
- 📦 Integrate new output formats or logging as needed

---

## 📜 License

MIT License (or specify your license here).

---

## 💡 Contributing

Pull requests and suggestions are welcome! Feel free to open issues for bugs or feature requests.

---

## 🙋‍♂️ Questions?

Open an issue or contact the maintainer.

