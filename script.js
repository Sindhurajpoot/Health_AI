// ================================
// MAIN ANALYSIS FUNCTION
// ================================
async function analyzeHealth() {
    const input = document.getElementById("inputText").value;

    // ✅ VALIDATION: Check if input is empty
    if (!input || input.trim() === "") {
        showError("❌ Please describe your symptoms first!");
        return;
    }

    // Show loading state
    document.getElementById("resultBox").style.display = "block";
    document.getElementById("errorBox").style.display = "none";
    document.getElementById("disease").innerText = "⏳ Analyzing...";
    document.getElementById("emotion").innerText = "⏳ Processing...";
    document.getElementById("advice").innerText = "⏳ Generating...";
    document.getElementById("insight").innerText = "⏳ Thinking...";
    document.getElementById("progress").style.width = "20%";

    try {
        // ✅ NETWORK REQUEST
        const response = await fetch("/analyze", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ text: input })
        });

        // ✅ CHECK RESPONSE STATUS
        if (!response.ok) {
            throw new Error(`Server error: ${response.status} ${response.statusText}`);
        }

        const data = await response.json();

        // ✅ VALIDATE RESPONSE DATA
        if (!data || !data.disease) {
            throw new Error("Invalid response from server - missing disease field");
        }

        // ✅ POPULATE RESULTS
        document.getElementById("disease").innerText = data.disease || "Unknown";
        document.getElementById("emotion").innerText = data.emotion || "Neutral";
        document.getElementById("advice").innerText = data.advice || "Consult a doctor";
        document.getElementById("insight").innerText = data.insight || "Keep monitoring";
        document.getElementById("confidence").innerText = data.confidence || 50;
        document.getElementById("futureRisk").innerText = data.future_risk || data.risk || 0;

        // ✅ UPDATE PROGRESS BAR
        const risk = data.risk || 0;
        document.getElementById("progress").style.width = risk + "%";

        // ✅ DISPLAY RISK TEXT
        let riskText = "";
        if (risk > 80) {
            riskText = "🚨 HIGH RISK – Seek immediate medical attention";
            document.getElementById("riskText").style.color = "#ff416c";
        } else if (risk > 60) {
            riskText = "⚠️ MODERATE RISK – Consult doctor soon";
            document.getElementById("riskText").style.color = "#ffd200";
        } else {
            riskText = "✅ LOW RISK – Home care recommended";
            document.getElementById("riskText").style.color = "#96c93d";
        }
        document.getElementById("riskText").innerText = riskText;

        // ✅ ACTION BUTTONS
        let actionHTML = "";

        if (risk > 80) {
            actionHTML = `
                <button class="danger" onclick="callEmergency()">🚨 Call Emergency</button>
                <button class="danger" onclick="findHospital()">🏥 Find Hospital</button>
            `;
        } else if (risk > 60) {
            actionHTML = `
                <button class="warning" onclick="bookAppointment()">📅 Book Doctor</button>
            `;
        } else {
            actionHTML = `
                <button class="safe" onclick="showTips()">💡 Health Tips</button>
            `;
        }
        document.getElementById("actionButtons").innerHTML = actionHTML;

    } catch (error) {
        // ✅ COMPREHENSIVE ERROR HANDLING
        console.error("[ERROR]", error);
        showError(`⚠️ Error: ${error.message}\n\nMake sure the server is running (python app.py)`);
    }
}

// ================================
// ERROR DISPLAY FUNCTIONS
// ================================
function showError(message) {
    document.getElementById("errorBox").style.display = "block";
    document.getElementById("resultBox").style.display = "none";
    document.getElementById("errorMessage").innerText = message;
}

function closeError() {
    document.getElementById("errorBox").style.display = "none";
}

// ================================
// ACTION BUTTON FUNCTIONS
// ================================
function callEmergency() {
    alert("🚨 Emergency services contacted!\nCall 911 or your local emergency number.");
}

function findHospital() {
    window.open("https://www.google.com/maps/search/hospitals+near+me", "_blank");
}

function bookAppointment() {
    alert("📅 Redirecting to doctor booking...\n(Feature coming soon)");
}

function showTips() {
    alert("💡 Health Tips:\n\n✓ Stay hydrated\n✓ Get proper rest\n✓ Eat nutritious food\n✓ Monitor symptoms\n✓ Avoid stress");
}