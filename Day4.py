"""
Day 4 Exercise: Input-Process-Output (IPO) Model

REFLECTION:
- What did I learn from this?
  I learned how to deliberately structure code into distinct Input, Process, and
  Output phases. I also learned how to encapsulate this pattern within a reusable
  function and execute it safely using Python's idiomatic main-guard.

- Why is it important for the course?
  Understanding the IPO pattern is a fundamental building block for procedural
  and functional programming. It teaches "separation of concerns," which is critical 
  for writing loosely coupled code that is easier to debug and audit.

- What will it help me with in the future?
  In future projects, this mental model will prevent me from writing "spaghetti code."
  By strictly separating data ingestion (Input), business logic (Process), and 
  data presentation (Output), I can build modular applications that are highly 
  scalable, easily testable, and maintainable in professional environments.
"""

def calculate_net_income():
    """
    Executes an IPO pipeline to calculate net income based on multiple financial inputs.
    
    This function collects gross salary, bonus, and tax rate from the user (Input),
    calculates the total deductions and final net income (Process), and displays 
    a formatted financial summary (Output).
    """
    
    # ==========================================
    # 1. INPUT PHASE
    # ==========================================
    print("=== Enterprise Salary Calculator ===")
    try:
        # Extension: Gathering multiple inputs from the user
        gross_salary = float(input("Enter base gross salary ($): "))
        bonus = float(input("Enter annual bonus ($): "))
        tax_percentage = float(input("Enter tax rate (e.g., 20 for 20%): "))
    except ValueError:
        print("[Error] Invalid input. Please enter numerical values.")
        return

    # ==========================================
    # 2. PROCESS PHASE
    # ==========================================
    # Extension: Adding custom business logic / arithmetic processing
    
    # Step A: Normalize the tax percentage to a decimal format for calculation
    tax_rate = tax_percentage / 100.0
    
    # Step B: Aggregate total gross income
    total_gross = gross_salary + bonus
    
    # Step C: Calculate tax deduction amount based on the total gross
    tax_deduction = total_gross * tax_rate
    
    # Step D: Determine final net income after deductions
    net_income = total_gross - tax_deduction

    # ==========================================
    # 3. OUTPUT PHASE
    # ==========================================
    # Extension: Updating the output to match the complex processing variables
    
    # Using f-strings to format the output with 2 decimal places and comma separators
    print("\n=== Financial Breakdown ===")
    print(f"Total Gross Income : ${total_gross:,.2f} (Base: ${gross_salary:,.2f} + Bonus: ${bonus:,.2f})")
    print(f"Tax Deducted       : ${tax_deduction:,.2f} (at {tax_percentage}%)")
    print(f"Net Income         : ${net_income:,.2f}")
    print("===========================\n")


# Python specific: Call the function from behind a main-guard/entrypoint
if __name__ == "__main__":
    calculate_net_income()
