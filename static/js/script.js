
async function scanURL(){
    console.log("NEW SCRIPT LOADED");
    const url = document.getElementById("url").value;
 
    if (!url) {
        alert("Enter a URL");
        return;
    }

document.getElementById("status").innerText = "Scanning...";

    try {
        const response = await fetch("/analyze", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                url: url
            })
        });

        const data = await response.json();
    

document.getElementById("result").classList.remove("hidden");

document.getElementById("status").innerText = "Completed";

document.getElementById("safe").innerText =
        data.result.risk + " (Score: " + data.result.score + ")";

document.getElementById("vtStatus").innerText =
    "Status: " + data.virustotal.status;

document.getElementById("vtHarmless").innerText =
    "Harmless: " + data.virustotal.harmless;

document.getElementById("vtMalicious").innerText =
    "Malicious: " + data.virustotal.malicious;

document.getElementById("vtSuspicious").innerText =
    "Suspicious: " + data.virustotal.suspicious;

    }
    catch (error) {

        document.getElementById("status").innerText = "Error";

        alert("Failed to connect to backend.");
        console.error(error);

    }
    
}
