import pickle
import pandas as pd

# Lade alte Datei
with open('/media/sz/Data/Connected_Lecturers/Opal/processed/keywords/keyword_list_.p', 'rb') as f:
    old_df = pickle.load(f)

# Lade neue Datei
with open('/media/sz/Data/Connected_Lecturers/Opal/processed/keywords/keyword_list.p', 'rb') as f:
    new_df = pickle.load(f)

print("=== ALTE DATEI (keyword_list_.p) ===")
print(f"Shape: {old_df.shape}")
print(f"Spalten: {list(old_df.columns)}")
print(f"\nDatentypen:")
print(old_df.dtypes)
print(f"\nErste 3 Zeilen:")
print(old_df.head(3))

print("\n\n=== NEUE DATEI (keyword_list.p) ===")
print(f"Shape: {new_df.shape}")
print(f"Spalten: {list(new_df.columns)}")
print(f"\nDatentypen:")
print(new_df.dtypes)
print(f"\nErste 3 Zeilen:")
print(new_df.head(3))

print("\n\n=== UNTERSCHIEDE ===")
old_cols = set(old_df.columns)
new_cols = set(new_df.columns)
print(f"Nur in alter Datei: {old_cols - new_cols}")
print(f"Nur in neuer Datei: {new_cols - old_cols}")
print(f"Zeilen alt: {len(old_df)}, Zeilen neu: {len(new_df)}")
print(f"Gemeinsame Spalten: {old_cols & new_cols}")
