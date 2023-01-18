let getInputNumbersValue = function (input) {
  return input.value.replace(/[a-zA-Z]|\s|\,/g, '');
};
let onDataInput = function (event) {
  let input = event.target;
  let inputNumbersValue = getInputNumbersValue(input);
  let formatedInputValue = '';

  formatedInputValue = formatedInputValue + inputNumbersValue;
  input.value = formatedInputValue;
};
let dataFilds = document.querySelectorAll('input')
for (i = 0; i < dataFilds.length; i++) {
    let input = dataFilds[i];
    input.addEventListener('input', onDataInput);
  }
