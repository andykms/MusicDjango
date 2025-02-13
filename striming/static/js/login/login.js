function getRandomInt(min, max) {
  min = Math.ceil(min); // Округляем минимальное значение вверх
  max = Math.floor(max); // Округляем максимальное значение вниз
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

const loginBackground = document.querySelector('.login__background');

// Пример использования:
const randomNumber = getRandomInt(1, 4); // Случайное число от 1 до 10

loginBackground.src = `../../static/images/login/gramm${randomNumber}.jpg`;



