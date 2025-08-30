
## 🛳️ Musical Lifeboat Problem – Custom Elimination Logic

### 📌 Problem Overview

A group of $n$ people is stranded on a boat, and only one lifeboat is available. To determine who survives, the captain initiates a brutal game with custom rules of elimination. People are numbered from **1 to $n$**, and in each round, specific patterns are followed to eliminate participants.

---

### 🔄 Elimination Rules

The game proceeds in **alternating rounds** as follows:

1. **Round 1** – Remove all **even-numbered** people.
2. **Round 2** – Remove any person who is **adjacent (in the current list)** to someone with an **odd number**.
3. **Round 3** – Again eliminate those adjacent to odd numbers.

🔁 This alternation continues **until only one person remains** — the one who gets the **lifeboat**.

---

### 🧠 Objective

To determine, for any given number of people $n$, **which person survives** based on the above rules.

This problem explores a **rule-based elimination system**, different from the classic Josephus problem, and demonstrates how structured elimination affects survival patterns.

---

### 💡 Features

* Custom elimination logic (not uniform step size)
* Pattern recognition through simulation
* Efficient computation of the final survivor
* Useful for understanding recursive thinking and list manipulation

---

### 💻 Technologies Used

* **Python**
* Basic control flow and list operations
* Optional: Can be extended with GUI or animation for visualization

* **OpenAI**
* Optimisation Of Code
* Simplification Of Code
