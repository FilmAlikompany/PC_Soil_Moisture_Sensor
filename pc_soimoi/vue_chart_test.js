window.onload = Main;

const base_url = "https://api.thingspeak.com/channels/1269853/feeds.json";
const api_key = "E5OIDR5LOLR1QP22";

let app;

function Main() {
    app = new Vue({
        el: "#app",
        data: {

            labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],   // x軸のラベル
            datasets: [  // グラフごとにオブジェクトを定義する
                {
                    label: "humidity",
                    data: [],
                    borderWidth: 1,    // 線の太さ
                    borderColor: "#00B7FF",
                    fill: false,   // 線の下の領域塗り潰しなし
                    backgroundColor: "#00B7FF"
                }
            ]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        suggestedMax: 1100,
                        suggestedMin: 200
                    }
                }]
            },
            responsive: true,
            maintainAspectRatio: false //これを追加
        },
        mounted: function() {
            updateData();
            setInterval(updateData, 15000);
        }
    });
}

function updateData() {
    const result_num = 10
    let url = base_url +
            "?api_key=" +
            api_key +
            "&timezone=Asia/Tokyo" +
            "&results=" +
            result_num;
    fetch(url, { method: 'GET' })
    .then(function(response) {
        return response.json();
    })
    .then(function(res) {
        // console.log(res.feeds);
        let humidity = []
        res.feeds.forEach(elm => {
            humidity.push(elm.field1);
        });
        app.datasets[0].data = humidity;

        console.log(app.datasets[0].data);

        updateGraph();
    });
}

function updateGraph() {
    let ctx = document.getElementById("myChart")
    let myChart = new Chart(ctx, {
        type: "line",
        data: {
            labels: app.labels,    // x軸のラベル
            datasets: app.datasets
        },
        options: {
            responsive: true
        }
    });
}