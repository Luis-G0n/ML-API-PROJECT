document.getElementById("predictionForm").addEventListener("submit", async function (e) {
    e.preventDefault();
  
    const formData = new FormData(this);
    const data = {};
  
    for (const [key, value] of formData.entries()) {
      data[key] = isNaN(Number(value)) ? value : Number(value);
    }
  
    const response = await fetch("http://127.0.0.1:8000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
    });
  
    const result = await response.json();
    document.getElementById("resultado").innerText = `Preço estimado: US$ ${result.preco_estimado}`;
  });
  