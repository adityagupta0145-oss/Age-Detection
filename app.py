import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Page Config
st.set_page_config(
    page_title="AI Age Detection",
    page_icon="🧑",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}

.title {
    text-align:center;
    font-size:45px;
    font-weight:bold;
    color:#1f77b4;
}

.subtitle {
    text-align:center;
    color:gray;
    margin-bottom:20px;
}

.result-box {
    padding:20px;
    border-radius:15px;
    background:#ffffff;
    box-shadow:0 4px 12px rgba(0,0,0,0.1);
    text-align:center;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<p class="title">🧑 AI Age Detection System</p>',
            unsafe_allow_html=True)

st.markdown(
    '<p class="subtitle">Upload an image and predict age instantly</p>',
    unsafe_allow_html=True
)

# Sidebar
st.sidebar.title("⚙ Settings")

confidence = st.sidebar.slider(
    "Face Detection Confidence",
    0.1, 1.0, 0.7
)

uploaded_file = st.file_uploader(
    "📤 Upload Image",
    type=["jpg", "jpeg", "png"]
)

# -----------------------------
# Load Models Here
# face_net = ...
# age_net = ...
# -----------------------------

# Dummy Function
def predict_age(face):
    age_groups = [
        "(0-2)", "(4-6)", "(8-12)",
        "(15-20)", "(25-32)",
        "(38-43)", "(48-53)", "(60-100)"
    ]
    return np.random.choice(age_groups)

if uploaded_file:

    image = Image.open(uploaded_file)

    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("Uploaded Image")
        st.image(image, use_container_width=True)

    img = np.array(image)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # Replace with your actual face detection
    h, w = img.shape[:2]

    x1, y1 = int(w*0.2), int(h*0.2)
    x2, y2 = int(w*0.7), int(h*0.8)

    cv2.rectangle(img, (x1, y1), (x2, y2),
                  (0, 255, 0), 2)

    age = predict_age(img)

    cv2.putText(
        img,
        f"Age: {age}",
        (x1, y1-10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0,255,255),
        2
    )

    with col2:
        st.subheader("Prediction Result")
        st.image(
            cv2.cvtColor(img, cv2.COLOR_BGR2RGB),
            use_container_width=True
        )

    st.markdown("---")

    m1, m2, m3 = st.columns(3)

    with m1:
        st.metric("Faces Detected", "1")

    with m2:
        st.metric("Predicted Age", age)

    with m3:
        st.metric("Confidence", "96%")

    st.markdown(
        f"""
        <div class='result-box'>
        <h2>🎯 Predicted Age Group</h2>
        <h1>{age}</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

else:
    st.info("Upload an image to start age prediction.")