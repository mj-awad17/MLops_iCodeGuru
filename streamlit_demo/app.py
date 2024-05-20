import streamlit as st
from sklearn.datasets import load_iris
from sklear.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklear.metrics import accuracy_score

# load the Iris dataset
iris = load_iris()
x = iris.data
y = iris.target

# train the model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_ratio =42)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# define streamlit app

st.title("Iris FLower Classification")

#sidebar for input parameter
st.sidebar.header("Input Parameters")
sepal_len = st.sidebar.slider("Sepal length", float(iris.data[:,0].min()), float(iris.data[:,0]).max())
sepal_wid = st.sidebar.slider("Sepal length", float(iris.data[:,1].min()), float(iris.data[:,1]).max())
petal_len = st.sidebar.slider("Sepal length", float(iris.data[:,2].min()), float(iris.data[:,2]).max())
petal_wid = st.sidebar.slider("Sepal length", float(iris.data[:,3].min()), float(iris.data[:,3]).max())

# predict function
def predict(sepal_len, sepal_wid, petal_len, petal_wid):
    data = [[sepal_len, sepal_wid, petal_len, petal_wid]]
    prediction = model.predict(data)
    return prediction

# display prediction
if st.button("Predict"):
    prediction = predict(sepal_len, sepal_wid, petal_len, petal_wid)
    species = iris.target_names[prediction[0]]
    st.write(f"The predicted speices is: ", species)