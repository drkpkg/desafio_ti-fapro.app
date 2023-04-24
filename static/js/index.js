document.addEventListener('DOMContentLoaded', () => {
    document.getElementById("formData").addEventListener("submit", (e) => {
        e.preventDefault();
        // string to date
        let dateSelect = new Date(document.getElementById('dateSelect').value);
        let year = dateSelect.getFullYear();
        let month = dateSelect.getMonth();
        let day = dateSelect.getDate();
        let fullData = document.getElementById('getAll').checked;
        fetch(`/api/v1/scrapper?month=${month}&day=${day}&year=${year}&full=${fullData}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        })
            .then(response => response.json())
            .then(data => {
                if (data.detail) {
                    let result = document.getElementById('result');
                    let div = document.createElement('div');
                    let p = document.createElement('p');
                    p.innerHTML = `Error: ${data.detail}`;
                    div.appendChild(p);
                    result.appendChild(div);
                } else {
                    let result = document.getElementById('result');
                    result.innerHTML = '';
                    let year = data.year;
                    let month = data.month;
                    let day = data.day;
                    let dataArr = data.data;
                    if (dataArr.length === 2) {
                        let div = document.createElement('div');
                        let p = document.createElement('p');
                        p.innerHTML = `Date: ${year}-${month}-${day} - ${dataArr[1]}`;
                        div.appendChild(p);
                        result.appendChild(div);
                    } else {
                        dataArr.forEach((item) => {
                            let div = document.createElement('div');
                            let p = document.createElement('p');
                            p.innerHTML = `Date: ${year}-${month}-${day} - ${item[1]}`;
                            div.appendChild(p);
                            result.appendChild(div);
                        });
                    }
                }
            });
    });
});