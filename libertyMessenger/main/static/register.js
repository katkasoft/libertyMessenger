function confirm() {
    var username = document.getElementById('username').value;
    var email = document.getElementById('email').value;
    var pass = document.getElementById('pass').value;
    var confirmedpass = document.getElementById('confirmedPass').value;
    if (username && email && pass && confirmedpass) {
        if (email.includes('.') && email.includes('@')) {
            if (pass == confirmedpass) {
                fetch('https://example.com/api/register', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                }, body: JSON.stringify({ key1: 'value1', key2: 'value2' })})
                .then(response => response.json())
                .catch(error => alert('Ошибка отправки:', error));
            } else {
                alert('Неправильно подтвержден пароль')
            }
        } else {
            alert('Некорректно введен email')
        }
    } else {
        alert('Введите все данные')
    }
}