# Pod Worksheet — Define the Research Task

## Pod members

- 

## 1\. Working title for the task

Give your task a short, practical name.

**Task title:** 

---

## 2\. What is the task?

Describe the specific research task you want the workflow to help with.

**Task description:**

---

## 3\. What is the input?

What material will go into this task?

**Input type:**

**Input source:**

**Approximate unit of input (e.g., 1 csv with 1000 rows):**

---

## 4\. What is the desired output?

What should come out of the task?

**Desired output:**  
1\. 

**Output format (e.g., CSV, JSON):**

---

## 5\. What would “good enough” look like?

Describe the minimum useful standard for the output.

## **Good enough means:**

---

## 6\. One likely failure mode

What is one way this could go wrong?

**Likely failure mode:**  
\[Examples: hallucinating details, inconsistent coding, missing nuance, bad formatting, overconfident output\]

---

## 7\. Human role

What part of this task should still involve human judgment?

**Human role:**  
\[Examples: reviewing uncertain outputs, refining codes, checking factual accuracy, selecting final outputs\]  
---

## 8\. Scope check

Is this task small enough to prototype in a workshop?

- [ ] Yes, this is a bounded task  
- [ ] Maybe, but we need to simplify it  
- [ ] No, this is too broad right now

If needed, simplify it here:

**Simplified version:**

1. 

# EXAMPLE Pod Worksheet — Define the Research Task

## Pod members

- Name: Aisha  
- Name: Marco  
- Name: Lin

## 1\. Working title for the task

Give your task a short, practical name.

**Task title:**  
Abstract-to-literature-table extraction

---

## 2\. What is the task?

Describe the specific research task you want the workflow to help with.

**Task description:**  
We want the workflow to read research article abstracts and extract key study details so we can build a structured literature review table more quickly.

---

## 3\. What is the input?

What material will go into this task?

**Input type:**  
Article abstracts

**Input source:**  
A CSV exported from our Zotero notes / manual collection of abstracts

**Approximate unit of input:**  
One abstract at a time

---

## 4\. What is the desired output?

What should come out of the task?

**Desired output:**  
One structured record per abstract with topic, population, method, and main finding

**Output format:**  
CSV file

---

## 5\. What would “good enough” look like?

Describe the minimum useful standard for the output.

**Good enough means:**

- The workflow extracts the main study details without inventing information  
- The output is consistent enough to sort and scan in a table  
- Missing information is marked clearly instead of guessed

---

## 6\. One likely failure mode

What is one way this could go wrong?

**Likely failure mode:**  
The model may infer a method or sample characteristic that is not explicitly stated in the abstract.

---

## 7\. Human role

What part of this task should still involve human judgment?

**Human role:**  
A human should review a sample of outputs for accuracy and should check any outputs with unclear or missing details before using them in the literature review.

---

## 8\. Scope check

Is this task small enough to prototype in a workshop?

- [x] Yes, this is a bounded task  
- [ ] Maybe, but we need to simplify it  
- [ ] No, this is too broad right now

If needed, simplify it here:

**Simplified version:**  
N/A  
