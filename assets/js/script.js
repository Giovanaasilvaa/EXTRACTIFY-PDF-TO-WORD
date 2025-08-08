document.addEventListener('DOMContentLoaded', () => {
  const dropArea = document.getElementById('drop-area');
  const fileElem = document.getElementById('fileElem');
  const resultado = document.getElementById('resultado');
  const uploadBtn = document.querySelector('.upload-btn');
  
  let isProcessing = false;

  // Function to show errors
  function showError(message) {
    console.error(message);
    resultado.textContent = message;
    resultado.style.color = 'red';
  }

  // When clicking on the drop area (except the button)
  dropArea.addEventListener('click', (e) => {
    if (!e.target.classList.contains('upload-btn')) {
      fileElem.click();
    }
  });

  // When clicking the Upload button
  uploadBtn.addEventListener('click', (e) => {
    e.preventDefault();
    e.stopPropagation();
    fileElem.click();
  });

  // When a file is selected
  fileElem.addEventListener('change', () => {
    if (fileElem.files.length && !isProcessing) {
      console.log('Selected file:', fileElem.files[0].name);
      sendFile(fileElem.files[0]);
    }
  });

  // Drag and drop events
  ['dragover', 'dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, (e) => {
      e.preventDefault();
      e.stopPropagation();
    });
  });

  dropArea.addEventListener('dragover', () => {
    dropArea.classList.add('dragover');
  });

  dropArea.addEventListener('dragleave', () => {
    dropArea.classList.remove('dragover');
  });

  dropArea.addEventListener('drop', (e) => {
    dropArea.classList.remove('dragover');
    if (e.dataTransfer.files.length && !isProcessing) {
      const file = e.dataTransfer.files[0];
      console.log('Dropped file:', file.name);
      if (file.type === "application/pdf") {
        sendFile(file);
      } else {
        showError("Please upload a PDF file.");
      }
    }
  });

  // Main function to send the file
  async function sendFile(file) {
    try {
      isProcessing = true;
      uploadBtn.disabled = true;
      resultado.style.color = '';
      resultado.textContent = "Converting PDF to Word...";
      
      console.log('Starting file conversion:', file.name);

      const formData = new FormData();
      formData.append('pdf', file);

      const response = await fetch('/upload', {
        method: 'POST',
        body: formData
      });

      console.log('Server response:', response.status);

      if (!response.ok) {
        const error = await response.text();
        throw new Error(error || "Server error");
      }

      const blob = await response.blob();
      console.log('Conversion finished, downloading file...');

      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = file.name.replace('.pdf', '') + '.docx';
      document.body.appendChild(a);
      a.click();
      
      // Cleanup
      setTimeout(() => {
        window.URL.revokeObjectURL(url);
        document.body.removeChild(a);
      }, 100);

      resultado.textContent = "Conversion completed!";
      
    } catch (error) {
      console.error('Conversion error:', error);
      showError(`Error: ${error.message}`);
    } finally {
      isProcessing = false;
      uploadBtn.disabled = false;
    }
  }
});

