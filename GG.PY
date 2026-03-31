print("AGENT: Starting Auto-Repair...")
ref_path = os.path.join(MODELS_DIR, 'reference_data.csv')
if not os.path.exists(ref_path):
return {"success": False, "error": "Reference data missing."}
# Step 1: Load clean reference data
df_ref = pd.read_csv(ref_path)
# Step 2: Simulate data cleaning (add small noise to represent new balanced data)
df_clean = df_ref.copy()
noise = np.random.normal(0, 0.01, size=df_clean.iloc[:, :-1].shape)
df_clean.iloc[:, :-1] += noise
