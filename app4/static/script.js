function uploadFile() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];
    const formData = new FormData();
    formData.append('file', file);
    uploadInput = document.getElementById('fileInput');
    uploadBtn = document.getElementById('uploadBtn');
    uploadInput.style.display = 'none';
    uploadBtn.style.display = 'none';
    fetch('/upload/', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerHTML =
            `File ${data.filename} uploaded (${data.size} bytes)`;
    })
    .catch(error => console.error('Error:', error));
    uploadInput.style.display = 'flex';
    uploadBtn.style.display = 'flex';
}
