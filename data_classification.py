# Project 2: Data Classification Using AI
# DecodeLabs - Industrial Training Kit
# Goal: Build a classification model using the Iris dataset & K-Nearest Neighbors (KNN)

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

# ---------------------------------------------------------
# STEP 1: INPUT - Load and understand the dataset
# ---------------------------------------------------------
iris = load_iris()
X = iris.data          # Features: sepal length, sepal width, petal length, petal width
y = iris.target        # Labels: 0 = Setosa, 1 = Versicolor, 2 = Virginica

print("Dataset Shape:", X.shape)          # (150, 4) -> 150 samples, 4 features
print("Classes:", iris.target_names)      # ['setosa' 'versicolor' 'virginica']
print("-" * 50)

# ---------------------------------------------------------
# STEP 2: PROCESS - Split data into training and testing sets
# ---------------------------------------------------------
# 80% data training ke liye, 20% testing ke liye
# random_state=42 taake result hamesha same aaye
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---------------------------------------------------------
# STEP 3: Scaling - sab features ko ek jaisi range mein lana
# ---------------------------------------------------------
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)   # training data se seekho aur transform karo
X_test_scaled = scaler.transform(X_test)         # test data ko sirf transform karo

# ---------------------------------------------------------
# STEP 4: Apply Classification Algorithm - KNN
# ---------------------------------------------------------
model = KNeighborsClassifier(n_neighbors=5)       # K = 5 (5 nearest neighbors dekh kar decide karega)
model.fit(X_train_scaled, y_train)                # Model ko train karo (seekhne do)

# Predictions on test data
predictions = model.predict(X_test_scaled)

# ---------------------------------------------------------
# STEP 5: OUTPUT - Validation (check karo model kitna sahi hai)
# ---------------------------------------------------------
accuracy = accuracy_score(y_test, predictions)
print("Model Accuracy:", round(accuracy * 100, 2), "%")
print("-" * 50)

print("Confusion Matrix:")
print(confusion_matrix(y_test, predictions))
print("-" * 50)

print("Classification Report (Precision, Recall, F1-Score):")
print(classification_report(y_test, predictions, target_names=iris.target_names))

# ---------------------------------------------------------
# BONUS: Naye samples test karo (yahan apne numbers daal sakte ho)
# ---------------------------------------------------------
test_flowers = [
    [5.1, 3.5, 1.4, 0.2],   # Ye normally Setosa nikalta hai
    [6.7, 3.0, 5.2, 2.3],   # Ye normally Virginica nikalta hai
    [5.9, 3.0, 4.2, 1.5],   # Ye normally Versicolor nikalta hai
]

print("\n--- Testing New Flowers ---")
for flower in test_flowers:
    flower_scaled = scaler.transform([flower])
    prediction = model.predict(flower_scaled)
    print(f"Measurements {flower} -> Predicted: {iris.target_names[prediction[0]]}")
