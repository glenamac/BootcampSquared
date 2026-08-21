## **Example minimum viable context pack**

### **Research task**

A PhD student wants to use an LLM to help with a **literature review** by extracting key study details from article abstracts into a structured format.

---

### **1\. Task statement**

Read a research abstract and extract the core study information into a structured record that can be added to a literature review table. Focus only on information explicitly stated in the text. If something is unclear or missing, mark it as `"not stated"` rather than guessing.

---

### **2\. Sample input**

**Abstract:**  
 This study examined the relationship between social support and academic persistence among first-generation college students at a large public university in the United States. Using survey data from 412 undergraduate students, the authors conducted multiple regression analyses to assess whether perceived support from family, peers, and faculty predicted students’ intention to remain enrolled. Results indicated that faculty support and peer support were significant positive predictors of persistence, while family support was not statistically significant. The findings suggest that university-based support systems may play an important role in retaining first-generation students.

---

### **3\. Ideal output example**

{  
 "topic": "social support and academic persistence among first-generation college students",  
 "population": "412 undergraduate first-generation college students at a large public university in the United States",  
 "study\_type": "survey study",  
 "method": "multiple regression",  
 "key\_variables": \[  
   "family support",  
   "peer support",  
   "faculty support",  
   "academic persistence"  
 \],  
 "main\_finding": "Faculty support and peer support were significant positive predictors of persistence, while family support was not statistically significant.",  
 "implication": "University-based support systems may play an important role in retaining first-generation students.",  
 "limitations\_or\_missing\_info": "not stated"  
}  
---

### **4\. Schema / structure**

You could give participants a simple schema like this:

{  
 "topic": "string",  
 "population": "string",  
 "study\_type": "string",  
 "method": "string",  
 "key\_variables": \["string"\],  
 "main\_finding": "string",  
 "implication": "string",  
 "limitations\_or\_missing\_info": "string"  
}  
---

### **5\. One caution or guardrail**

Do not invent information that is not explicitly stated in the abstract. If the method, population details, or limitations are missing, return `"not stated"` rather than inferring.

