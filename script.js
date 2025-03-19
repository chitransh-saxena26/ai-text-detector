async function predict() {
    const text = document.getElementById("textInput").value;

    if (!text) {
        alert("Please enter some text to analyze!");
        return;
    }

    try {
        // Sending request to the Flask backend
        const response = await fetch("http://127.0.0.1:5000/analyze", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text: text })
        });

        const result = await response.json();

        // Display the result
        document.getElementById("resultText").innerHTML = `Result: <strong>${result.label}</strong>`;
        document.getElementById("confidenceScore").innerText = `Confidence: ${result.confidence.toFixed(2)}%`;
        document.getElementById("resultSection").style.display = "block";

    } catch (error) {
        console.error("Error:", error);
        alert("Something went wrong. Check the console for details.");
    }
}
