document.getElementById('imageUpload').addEventListener('change', function(e) {
    const fileName = document.getElementById('fileName');
    const previewContainer = document.getElementById('previewContainer');
    const imagePreview = document.getElementById('imagePreview');
    
    if (this.files.length > 0) {
        fileName.textContent = this.files[0].name;
        fileName.style.color = '#10b981';
        
        // Show preview
        const reader = new FileReader();
        reader.onload = function(event) {
            imagePreview.src = event.target.result;
            previewContainer.style.display = 'block';
        }
        reader.readAsDataURL(this.files[0]);
    } else {
        fileName.textContent = 'No file chosen';
        fileName.style.color = '#6b7280';
        previewContainer.style.display = 'none';
    }
});

document.getElementById('diagnosisForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const formData = new FormData(this);
    const analyzeBtn = document.getElementById('analyzeBtn');
    const btnText = document.getElementById('btnText');
    const spinner = document.getElementById('spinner');
    const resultBox = document.getElementById('resultBox');
    const diagnosisResult = document.getElementById('diagnosisResult');
    
    // Show loading state
    analyzeBtn.disabled = true;
    btnText.textContent = 'Analyzing...';
    spinner.style.display = 'inline-block';
    resultBox.style.display = 'none';
    
    fetch('/ai-image-diagnosis', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Show results
        diagnosisResult.innerHTML = data.result.replace(/\n/g, '<br>');
        resultBox.style.display = 'block';
    })
    .catch(error => {
        diagnosisResult.textContent = 'Error occurred during analysis. Please try again.';
        resultBox.style.display = 'block';
    })
    .finally(() => {
        // Reset button state
        analyzeBtn.disabled = false;
        btnText.textContent = 'Analyze Image';
        spinner.style.display = 'none';
    });
});