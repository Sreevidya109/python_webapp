function submitSymptom() {
    const input = document.getElementById("symptomInput").value;

    fetch("/get_medicine", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ symptom: input })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("outputArea").value = data.response;
    })
    .catch(error => {
        document.getElementById("outputArea").value = "Error: " + error;
    });
}
