import os

# Paths to your image and label directories
IMG_DIR   = "data/train/images"
LBL_DIR   = "data/train/labels"

# Supported image extensions
IMG_EXTS = {".jpg", ".jpeg", ".png"}

# Collect images without corresponding labels
missing_labels = []

for fname in os.listdir(IMG_DIR):
    name, ext = os.path.splitext(fname)
    if ext.lower() not in IMG_EXTS:
        continue

    img_path = os.path.join(IMG_DIR, fname)
    lbl_path = os.path.join(LBL_DIR, f"{name}.txt")

    # Check if label exists and is non-empty
    if not os.path.isfile(lbl_path) or os.path.getsize(lbl_path) == 0:
        missing_labels.append(img_path)

# Report
print(f"Found {len(missing_labels)} images without valid labels:")
for p in missing_labels:
    print("  ", p)
print(len(missing_labels))

# Now `missing_labels` holds all image paths you may want to review.
# remove the images without labels
for img_path in missing_labels:
    try:
        os.remove(img_path)
        print(f"Removed: {img_path}")
    except Exception as e:
        print(f"Error removing {img_path}: {e}")
