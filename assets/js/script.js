const dropArea = document.getElementById('drop-area');
const fileElem = document.getElementById('fileElem');
const resultado = document.getElementById('resultado');
const uploadBtn = document.querySelector('.upload-btn');  // novo: botão upload

// Ao clicar na área de drop, abrir seletor de arquivo
dropArea.addEventListener('click', () => fileElem.click());

// Ao clicar no botão "Faça Upload", também abre seletor de arquivo
uploadBtn.addEventListener('click', (e) => {
  e.preventDefault(); // evita qualquer comportamento padrão
  fileElem.click();
});

// Quando o arquivo for selecionado via seletor, envia o arquivo
fileElem.addEventListener('change', (e) => {
  if (fileElem.files.length) {
    enviarArquivo(fileElem.files[0]);
  }
});

// Eventos para drag and drop
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
      enviarArquivo(file);
    } else {
      alert("Por favor, envie um arquivo PDF.");
    }
  }
});

// Função para enviar arquivo ao backend e iniciar download
function enviarArquivo(file) {
  resultado.textContent = "Extraindo texto e gerando arquivo Word...";

  const formData = new FormData();
  formData.append('pdf', file);

  fetch('/upload', {
    method: 'POST',
    body: formData
  })
  .then(response => {
    if (!response.ok) {
      throw new Error("Erro no servidor");
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
    resultado.textContent = "Download concluído!";
  })
  .catch(err => {
    resultado.textContent = "Erro ao processar o arquivo.";
    console.error(err);
  });
}
