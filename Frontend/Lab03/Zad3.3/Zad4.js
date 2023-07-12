fetch('https://jsonplaceholder.typicode.com/posts')
    .then(response => {
        if (response.status === 200) {
            return response.json();
        } else {
            console.error('Błąd żądania: ', response.status);
        }
    })
    .then(data => {
        data.forEach(({ title, body }) => {
            console.log(`Tytuł: ${title}\nTreść: ${body}\n`);
        });
    })
    .catch(error => console.error('Błąd: ', error));
