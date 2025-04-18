document.addEventListener("DOMContentLoaded", function () {
  const uploadBox = document.getElementById("uploadBox");
  const fileInput = document.getElementById("fileInput");
  const uploadStatus = document.getElementById("uploadStatus");
  const analysisSection = document.getElementById("analysisSection");
  const qaContainer = document.getElementById("qaContainer");
  const userQuery = document.getElementById("userQuery");
  const sendQuery = document.getElementById("sendQuery");

  // Handle drag and drop
  uploadBox.addEventListener("dragover", (e) => {
    e.preventDefault();
    uploadBox.classList.add("dragover");
  });

  uploadBox.addEventListener("dragleave", () => {
    uploadBox.classList.remove("dragover");
  });

  uploadBox.addEventListener("drop", (e) => {
    e.preventDefault();
    uploadBox.classList.remove("dragover");
    if (e.dataTransfer.files.length) {
      fileInput.files = e.dataTransfer.files;
      handleFileUpload();
    }
  });

  uploadBox.addEventListener("click", () => {
    fileInput.click();
  });

  fileInput.addEventListener("change", handleFileUpload);

  function handleFileUpload() {
    const file = fileInput.files[0];
    if (!file) return;

    if (!file.name.toLowerCase().endsWith(".pdf")) {
      showUploadStatus("Please upload a PDF file", "error");
      return;
    }

    showUploadStatus("Processing medical report...", "loading");

    const formData = new FormData();
    formData.append("file", file);

    fetch("/upload", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.error) {
          showUploadStatus(data.error, "error");
        } else {
          showUploadStatus("Medical report processed successfully!", "success");
          analysisSection.style.display = "block";
          // Scroll to analysis section
          analysisSection.scrollIntoView({ behavior: "smooth" });
        }
      })
      .catch((error) => {
        showUploadStatus("Error uploading file", "error");
        console.error("Error:", error);
      });
  }

  function showUploadStatus(message, type) {
    uploadStatus.textContent = message;
    uploadStatus.className = "upload-status " + type;
  }

  sendQuery.addEventListener("click", sendMessage);
  userQuery.addEventListener("keypress", (e) => {
    if (e.key === "Enter") sendMessage();
  });

  function sendMessage() {
    const query = userQuery.value.trim();
    if (!query) return;

    // Clear previous Q&A
    qaContainer.innerHTML = "";

    // Add question
    const questionDiv = document.createElement("div");
    questionDiv.className = "question-box";
    questionDiv.innerHTML = `
                    <strong><i class="fas fa-user"></i> Your Question:</strong>
                    <p>${query}</p>
                `;
    qaContainer.appendChild(questionDiv);

    // Add loading answer box
    const answerDiv = document.createElement("div");
    answerDiv.className = "answer-box";
    answerDiv.innerHTML = `
                    <strong><i class="fas fa-robot"></i> AI Analysis:</strong>
                    <div class="button-spinner" style="margin: 10px auto;"></div>
                `;
    qaContainer.appendChild(answerDiv);
    answerDiv.style.display = "block";

    userQuery.value = "";
    sendQuery.disabled = true;
    sendQuery.innerHTML = '<div class="button-spinner"></div>';

    fetch("/analyze", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ query: query }),
    })
      .then((response) => response.json())
      .then((data) => {
        sendQuery.disabled = false;
        sendQuery.innerHTML = '<i class="fas fa-paper-plane"></i>';

        if (data.error) {
          answerDiv.innerHTML = `
                            <strong><i class="fas fa-robot"></i> AI Analysis:</strong>
                            <p>Sorry, there was an error processing your query.</p>
                        `;
        } else {
          answerDiv.innerHTML = `
                            <strong><i class="fas fa-robot"></i> AI Analysis:</strong>
                            <p>${data.response}</p>
                        `;
        }
        // Scroll to answer
        answerDiv.scrollIntoView({ behavior: "smooth", block: "nearest" });
      })
      .catch((error) => {
        sendQuery.disabled = false;
        sendQuery.innerHTML = '<i class="fas fa-paper-plane"></i>';

        answerDiv.innerHTML = `
                        <strong><i class="fas fa-robot"></i> AI Analysis:</strong>
                        <p>Sorry, there was an error processing your query.</p>
                    `;
        console.error("Error:", error);
      });
  }
});
