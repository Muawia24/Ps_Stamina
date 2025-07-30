# 📊 Group Totals

**Problem Statement**

Implement the function `GroupTotals(strArr)` that takes a list of strings where each string represents a key-value pair in the format `key:value`. Your task is to return a single string containing key-value pairs where:
- Each key appears only once,
- Values are summed for duplicate keys,
- Keys with a total value of `0` are excluded,
- Keys are sorted alphabetically in the final result.

---

### 🧠 Function Signature
```python
def GroupTotals(strArr: List[str]) -> str:
```

---

### 🔍 Examples

#### Example 1
**Input:**
```python
["B:-1", "A:1", "B:3", "A:5"]
```
**Output:**
```
A:6,B:2
```

#### Example 2
**Input:**
```python
["X:-1", "Y:1", "X:-4", "B:3", "X: 5"]
```
**Output:**
```
B:3,Y:1
```

#### Example 3
**Input:**
```python
["Z:0", "A:-1"]
```
**Output:**
```
A:-1
```

---

### ✅ Constraints
- Input will be a list of strings, each formatted as `"Key:Value"`.
- All keys are strings with alphabetical characters.
- Values can be positive or negative integers.
- The length of each key-value string may contain whitespace after the colon (`:`), which should be stripped.
