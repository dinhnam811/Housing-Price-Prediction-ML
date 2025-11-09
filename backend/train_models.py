"""
Script to pre-train all models and save them to .pkl files
Run this locally before deploying to Vercel
"""

from LiveableAreaModel import LiveableAreaModel
from SuburbModel import SuburbModel

print("Training LiveableAreaModel...")
liveable_model = LiveableAreaModel()
liveable_model.train()
print("✓ LiveableAreaModel trained and saved")

print("\nTraining SuburbModel...")
suburb_model = SuburbModel()
suburb_model.train()
print("✓ SuburbModel trained and saved")

print("\nAll models trained successfully!")
print("The following files were created:")
print("  - liveable_area_model.pkl")
print("  - scaler.pkl")
print("  - label_encoder.pkl")
print("  - original_data.pkl")
print("  - cluster_model.pkl")
