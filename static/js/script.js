document.getElementById('image-upload').addEventListener('change', function(event) {
    const fileName = event.target.files[0].name;
    document.getElementById('file-name').textContent = fileName;

    // Display the uploaded image
    const reader = new FileReader();
    reader.onload = function(e) {
        document.getElementById('uploaded-image').src = e.target.result;
    };
    reader.readAsDataURL(event.target.files[0]);
});

document.getElementById('predict-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const fileInput = document.getElementById('image-upload');
    if (!fileInput.files[0]) {
        alert('Please select an image to upload.');
        return;
    }

    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    const predictButton = document.getElementById('predict-button');
    const loader = document.getElementById('loader');
    const resultDiv = document.getElementById('result');
    const diseaseName = document.getElementById('disease-name');

    predictButton.disabled = true;
    loader.style.display = 'block';
    resultDiv.style.display = 'none';

    fetch('/predict', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.predicted_disease) {
            diseaseName.textContent = `Predicted Disease: ${data.predicted_disease}`;
        } else {
            diseaseName.textContent = 'Error: Could not predict disease';
        }
    })
    .catch(error => {
        diseaseName.textContent = 'Error: Could not predict disease';
    })
    .finally(() => {
        predictButton.disabled = false;
        loader.style.display = 'none';
        resultDiv.style.display = 'block';
    });
});