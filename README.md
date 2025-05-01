# Church Band Scheduler

A simple Python script to schedule a church band for a 12-week period, ensuring each week has 1 drummer, 1 bassist, 1 guitarist, and 2 vocalists, while accounting for musicians' availability and multiple roles.

## Features
- Generates a band with random musician names, roles, and weeks off
- Schedules musicians based on availability and role requirements
- Handles musicians with multiple roles
- Includes basic unit tests for reliability

## Requirements
- Python 3.x
- `faker` library (`pip install faker`)

## Usage
1. Clone the repository or download the scripts
2. Install dependencies:
   ```bash
   pip install faker
   ```
3. Run the main script:
   ```bash
   python band_scheduler.py
   ```
4. View the generated 12-week schedule in the console

## Files
- `band_scheduler.py`: Main script for scheduling the band
- `utils.py`: Utility functions for generating band data
- `test_utils.py`: Unit tests for utility functions
- `test_band_scheduler.py`: Unit tests for the scheduler

## Example Output
```
Week 1
Drummer: John
Bassist: Alice
Vocalists: Bob, Carol
Guitarist: Dave

Week 2
...
```

## Notes
- The script randomly assigns 1–4 weeks off per musician
- If not enough musicians are available for a week, it outputs a message indicating the shortage
- Musicians with multiple roles are assigned based on availability and role needs