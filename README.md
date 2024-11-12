# CSE 366 AI Lab Tasks 

## Overview
This repository contains Python based  lab tasks for AI and file handling and so on.

### Task 1: Student Selection for Viva
A program to select students randomly for viva.

#### Instructions
1. **Load Student IDs**: Reads student IDs from `student_ids.txt`, where each ID follows the format `YYYY-N-MM-xxx`.
2. **Manage List**: Keeps track of students who haven’t been selected.
3. **Random Selection**: Picks a student for viva, removes them from the list, and repeats until all students are chosen.
4. **Reset**: Once all students are picked, the list resets to include everyone again.

#### Additional Notes
- Error handling for missing or misformatted files.
- Includes a "Viva #" counter to track the selection order.

---

### Task 2: Trading Agent for Smartphone Inventory Management
An AI-based trading agent that manages smartphone inventory based on price and stock levels.

#### Key Features
- **Percepts**: 
  - **Price**: Current price of a smartphone model.
  - **Stock Level**: Number of units available.
    
- **Decision Process**: 
  - The agent’s goal is to optimize stock levels while minimizing costs.
  - It must decide whether to order more smartphones and, if so, how many to order.
- **Decision Rules**: 
  - If the price of the smartphone drops significantly (indicating a deal or promotion),the agent considers ordering more units.

- **Threshold**: Let’s say the threshold is a 20% discount from the average price.
  - If the amount in stock falls below a certain level (e.g., 10 units), the agent prioritizes restocking.
  - Otherwise, the agent decides not to place an order.
    
- **Commands/Actions**: 
  - If the smartphone price is below the threshold (20% discount) and the stock level is not critically low, the agent orders a specific quantity (let’s call it tobuy).

#### Actions
- If conditions are met, the agent orders additional units as specified.

#### Output
The task generates a graph showing the agent’s decisions based on price and stock level changes.

---
