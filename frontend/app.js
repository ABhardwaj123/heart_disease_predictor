
async function predict(){

    const data = {
        age: parseFloat(document.getElementById('age').value),
        sex: parseFloat(document.getElementById('sex').value),
        cp: parseFloat(document.getElementById('cp').value),
        trestbps: parseFloat(document.getElementById('trestbps').value),
        chol: parseFloat(document.getElementById('chol').value),
        fbs: parseFloat(document.getElementById('fbs').value),
        restecg: parseFloat(document.getElementById('restecg').value),
        thalach: parseFloat(document.getElementById('thalach').value),
        exang: parseFloat(document.getElementById('exang').value),
        oldpeak: parseFloat(document.getElementById('oldpeak').value),
        slope: parseFloat(document.getElementById('slope').value),
        ca: parseFloat(document.getElementById('ca').value),
        thal: parseFloat(document.getElementById('thal').value)
    }

    const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers:{
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })

    if(!response.ok){
        const data = await response.json()
        const msg = document.getElementById("message")
        msg.innerText = data.detail
        msg.className = "error"
    }else{

        const container = document.getElementById('result')

        const data = await response.json()

        const prediction = data.prediction
        const probab = data.probability

        if(prediction){
            container.innerHTML += `
                <div>
                    <h2>Risk Of heart Disease: Yes</h2>
                    <h2>Probability of heart disease: ${probab}</h2>
                </div>
            `
        }else{
            container.innerHTML += `
                <div>
                    <h2>Risk Of heart Disease: No</h2>
                </div>
            `
        }
    }
}