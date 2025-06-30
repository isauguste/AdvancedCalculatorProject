# Advanced Python Calculator Project for Software Engineering

## Features 
- **Basic Operations:** Add, Subtract, Multiply, Divide
- **Plugin Support:** Modulo, Square Root, Negate (dynamically loaded)
- **REPL Interface:** Type `num1 num2 operation` or use special commands like `menu`, `clear`, `save`, `load`, `quit`
- **History Management:** Track and save calculations using Pandas DataFrames
- **Environment Config:** Supports `.env` file for:
  - `LOG_LEVEL`: DEBUG, INFO, WARNING, etc.
  - `HISTORY_FILE`: Target CSV file to store history
- **Logging:** Logs saved to `calculator.log`
- unit tests with `pytest` 

## Setup 
```bash
git clone <your-repo-url>
cd AdvancedCalculatorProject
python -m venv venv
source venv/bin/activate or venv\Scripts\activate on Windows
pip install -r requirements.txt

## Demo Video 
https://youtu.be/39HL_-leQ9U 
