import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, roc_curve, auc
import seaborn as sns
import numpy as np

# Example data (replace with your model outputs)
y_true = [0,1,1,0,1,0,1,1,0,1]
y_pred = [0,1,0,0,1,0,1,1,0,1]
y_prob = [0.1,0.9,0.4,0.2,0.8,0.3,0.7,0.85,0.2,0.95]

# --- Confusion Matrix ---
cm = confusion_matrix(y_true, y_pred)

plt.figure()
sns.heatmap(cm, annot=True, fmt="d")
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.savefig("confusion_matrix.png")
plt.close()

# --- ROC Curve ---
fpr, tpr, _ = roc_curve(y_true, y_prob)
roc_auc = auc(fpr, tpr)

plt.figure()
plt.plot(fpr, tpr, label=f"AUC = {roc_auc:.2f}")
plt.plot([0,1], [0,1])
plt.title("ROC Curve")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.legend()
plt.savefig("roc_curve.png")
plt.close()

print("Graphs saved: confusion_matrix.png, roc_curve.png")
