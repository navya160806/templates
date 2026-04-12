from flask  import Flask, render_template
app = Flask(__name__)
joblib.dump(new_model, repaired_model_path)
print(f"Repaired model saved.")
return {
"success": True,
"model_path": repaired_model_path,
"data_path": clean_data_path,
"message": "Outliers removed, Bias corrected, Model Retrained."
