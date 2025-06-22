const dropArea = document.getElementById('drop-area');
const fileElem = document.getElementById('fileElem');
const resultado = document.getElementById('resultado');
const uploadBtn = document.querySelector('.upload-btn');  // new: upload button

// When clicking on the drop area, open the file selector
dropArea.addEventListener('click', () => fileElem.click());

// When clicking the "Upload" button, also open the file selector
uploadBtn.addEventListener('click', (e) => {
  e.preventDefault(); // prevent default behavior
  fileElem.click();
});

// When a file is selected via the file selector, send the file
fileElem.addEventListener('change', (e) => {
  if (fileElem.files.length) {
    sendFile(fileElem.files[0]);
  }
});

// Events for drag and drop
dropArea.addEventListener('dragover', (e) => {
  e.preventDefault();
  dropArea.classList.add('dragover');
});

dropArea.addEventListener('dragleave', () => {
  dropArea.classList.remove('dragover');
});

dropArea.addEventListener('drop', (e) => {
  e.preventDefault();
  dropArea.classList.remove('dragover');
  if (e.dataTransfer.files.length) {
    const file = e.dataTransfer.files[0];
    if(file.type === "application/pdf"){
      sendFile(file);
    } else {
      alert("Please upload a PDF file.");
    }
  }
});

// Function to send file to backend and start download
function sendFile(file) {
  resultado.textContent = "Extracting text and generating Word file...";

  const formData = new FormData();
  formData.append('pdf', file);

  fetch('/upload', {
    method: 'POST',
    body: formData
  })
  .then(response => {
    if (!response.ok) {
      throw new Error("Server error");
    }
    return response.blob();
  })
  .then(blob => {
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'saida.docx';
    document.body.appendChild(a);
    a.click();
    a.remove();
    resultado.textContent = "Download complete!";
  })
  .catch(err => {
    resultado.textContent = "Error processing the file.";
    console.error(err);
  });
}

