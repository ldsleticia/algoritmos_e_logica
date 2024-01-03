function imprimirImpares() {
  const fim = 100;
  let inicio = 0;

  while (inicio <= fim) {
    if (inicio % 2 !== 0) {
      console.log(inicio);
    }
    inicio++;
  }
}

function dezPrimeirosMultiplosDeTres() {
  let multiplos = 0;
  let inicio = 0;

  while (multiplos < 10) {
    if (inicio % 3 === 0) {
      console.log(inicio);
      multiplos++;
    }
    inicio++;
  }
}

// imprimirImpares()
dezPrimeirosMultiplosDeTres();
