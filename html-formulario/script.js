const result = document.getElementById("result");
const form = document.forms["myForm"];

form.addEventListener("submit", handlePrevent);

function handlePrevent(e) {
  e.preventDefault();
  cleanResult();

  switch (form.number.value) {
    case "1":
      imprimirImpares();
      break;
    case "2":
      imprimirDezPrimeirosMultiplosDeTres();
      break;
    default:
      alert("exercicio não encontrado");
  }
}

function imprimirImpares() {
  const fim = parseInt(prompt("Insira o valor de fim: "));
  let inicio = 0;

  while (inicio <= fim) {
    if (inicio % 2 !== 0) {
      result.innerText += `\t${inicio}`;
    }
    inicio++;
  }
}

function imprimirDezPrimeirosMultiplosDeTres() {
  let multiplos = 0;
  let inicio = 0;

  while (multiplos < 10) {
    if (inicio % 3 === 0) {
      result.innerText += `\t${inicio}`;
      multiplos++;
    }
    inicio++;
  }
}

function cleanResult() {
  result.innerText = "";
}
