function Calculadora() {
  this.display = document.querySelector(".display");
  this.btnClear = document.querySelector(".btn-clear");

  this.inicia = function () {
    this.cliqueBotoes();
    this.pressionaEnter();
  };

  this.cliqueBotoes = function () {
    document.addEventListener("click", (e) => {
      const el = e.target;

      if (el.classList.contains("btn-num")) this.btnParaDisplay(el.innerText);
      if (el.classList.contains("btn-clear")) this.clearDisplay();
      if (el.classList.contains("btn-del")) this.apagaUm();
      if (el.classList.contains("btn-eq")) this.realizaConta();
    });
  };

  this.pressionaEnter = function () {
    document.addEventListener("keyup", (e) => {
      if (e.key === "enter") this.realizaConta();
    });
  };

  this.btnParaDisplay = (valor) => {
    this.display.value += valor;
  };

  this.clearDisplay = () => (this.display.value = "");

  this.apagaUm = () => (this.display.value = this.display.value.slice(0, -1));

  this.realizaConta = function () {
    let total = this.display.value;

    try {
      total = eval(total);

      if (typeof total !== "number") {
        throw "Erro";
      }
      this.display.value = total;
    } catch (err) {
      alert("Hove um erro!");
    }
  };
}

const calculadora = new Calculadora();
calculadora.inicia();
