import isEmail from "validator/lib/isEmail";
const SHOW_ERROR_MESSAGES = "show-error-message";

const form = document.querySelector(".form") as HTMLFormElement;
const email = document.querySelector(".email") as HTMLInputElement;
const password = document.querySelector(".password") as HTMLInputElement;
const password2 = document.querySelector(".password2") as HTMLInputElement;

form.addEventListener("submit", function (event) {
  event.preventDefault();
  hideErrorMessages(this);
  checkForEmptyFields();
  checkEmail(email);
  checkPassword(password, password2);
});

function hideErrorMessages(form: HTMLFormElement): void {
  form
    .querySelectorAll("." + SHOW_ERROR_MESSAGES)
    .forEach((item) => item.classList.remove(SHOW_ERROR_MESSAGES));
}

function showErrorMessage(input: HTMLInputElement, msg: string): void {
  let formFields = input.parentElement as HTMLDivElement;
  /*
   * Por mais que este while não pareça necessario na maioria das ocasioes
   * ele foi necessario pois existe casos de usuarios que usam extenções de gerenciadores de senhas
   * e nestes casos o pai do input e uma div gerada pela extenção
   * fazendo assim com que a variavel errorMessage seja undefined e por fim quebrando o codigo
   */

  while (!formFields.classList.contains("form-fields")) {
    formFields = formFields.parentElement as HTMLDivElement;
  }
  const errorMessage = formFields.querySelector(
    ".error-message",
  ) as HTMLSpanElement;
  errorMessage.innerText = msg;
  formFields.classList.add(SHOW_ERROR_MESSAGES);
}

function checkForEmptyFields(): void {
  document.querySelectorAll("input").forEach((item) => {
    if (item.value === "") {
      showErrorMessage(item, `O campo ${item.name} não pode ficar vazio.`);
    }
  });
}

function checkEmail(email: HTMLInputElement): void {
  if (!isEmail(email.value)) {
    showErrorMessage(email, "Email invalido");
  }
}

function checkPassword(
  password: HTMLInputElement,
  password2: HTMLInputElement,
): void {
  if (password.value !== password2.value) {
    showErrorMessage(password, "As senhas não conhecidem");
    showErrorMessage(password2, "As senhas não conhecidem");
  }
}
