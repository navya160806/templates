from flask  import Flask, render_template
app = Flask(__name__)
joblib.dump(new_model, repaired_model_path)
print(f"Repaired model saved.")

return {
    "success": True,
    "model_path": repaired_model_path,
    "data_path": clean_data_path,
    "message": "Outliers removed, Bias corrected, Model Retrained."
    except Exception as e:

}
if not os.path.exists(LOG_FILE):
    return []
try:
    ddf = pd.read_csv(LOG_FILE)
    return df.tail(limit).to_dict(orient='records')
except Exception as e:
    return [{"error": str(e)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    