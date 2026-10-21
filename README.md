# Next-AI-Gen

## Sub-group DIA7- Groupe 4
- Mary Mohanasundaram 
- Ahmet Bugday 
- Matthieu Ropiteau 
- Cameron Prunet 
- Maram Lakhal 
- Alexis Dinanga


## Environment
- **Pack**: 2026-10-18-students-1
- **Python**: 3.14
- **Kit**: `kit-td1/`

## Reproduction Instructions
1. From this repository, create and activate a virtual environment, then install `requests`:
   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   python -m pip install requests
   ```
2. Set `GROQ_API_KEY` and `OPENROUTER_API_KEY` as PowerShell environment variables. Never add keys to a file or commit them.
3. Run the local data check and the one-time API access check:
   ```powershell
   python .\kit-td1\verify-data.py
   python .\kit-td1\check_access.py | Tee-Object ready-for-td1.txt
   ```
4. Run the model comparison only after filling and independently checking `reference-td1.csv`:
   ```powershell
   python .\kit-td1\skeleton-multi-llm-en.py --run --reference .\reference-td1.csv
   ```

`verify_references.py` executes each reference query against the read-only SQLite database and cross-checks the result with an independent Python calculation. The 100 model calls require the group allocation and each operator's available quota; do not run the same model batch twice.
