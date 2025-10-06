## The Continue Statement
"""
**continue** = Skip to the next iteration

**difference from break:**
- **break**
"""
# Example skip 3
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print(count)
