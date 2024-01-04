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

function tabuada() {
  const fim = 10;
  let inicio = 1;

  while (inicio <= fim) {
    console.log(`${inicio}x${fim} = ${inicio * fim}`);
    inicio++;
  }
}

function multiplicaComSoma() {
  let fim = 10;
  let inicio = 5;
  let resultado = 0;

  while (fim > 0) {
    resultado += inicio;
    fim--;
  }
  console.log(resultado);
}

function divideComSubtracao() {
  let dividendo = 10;
  let divisor = 2;
  let quociente = 0;
  let resto = dividendo;

  while (resto >= divisor) {
    resto -= divisor;
    quociente += 1;
  }
  console.log('sou o quociente', quociente);
  console.log('sou o resto', resto);
}

// imprimirImpares()
// dezPrimeirosMultiplosDeTres();
// tabuada()
// multiplicaComSoma()
// divideComSubtracao()