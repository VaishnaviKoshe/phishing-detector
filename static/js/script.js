
async function scanURL(){    
    const scanLoader = document.getElementById("scanLoader");
    const status = document.getElementById("status")
    const url = document.getElementById("url").value.trim();
 
    /* Validate URL input first */
    if (!url) {
    scanLoader.classList.add("hidden");
        status.innerText = "";
        alert("Enter a URL");
        return;
    }

    /* Start scanning state */
scanLoader.classList.remove("hidden");
    status.innerText = "";
    status.className = "";

document.getElementById("result").classList.add("hidden");

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

        /* Risk */

        const risk = document.getElementById("risk");
        
        risk.innerText = data.result.risk;

        risk.className = "";

        if(data.result.risk==="SAFE")
            risk.classList.add("badge","safe");

        else if(data.result.risk==="SUSPICIOUS")
            risk.classList.add("badge","suspicious");

        else
            risk.classList.add("badge","phishing");

document.getElementById("score").innerText =
    data.result.score + " / 100";

        /* URL */

document.getElementById("domain").innerText =
    data.basic_info.domain;

document.getElementById("scheme").innerText =
    data.basic_info.scheme.toUpperCase();

document.getElementById("path").innerText =
    data.basic_info.path || "/";

document.getElementById("length").innerText =
    data.checks.url_length;

document.getElementById("dns").innerText =
    data.checks.dns_status;

document.getElementById("age").innerText =
    data.checks.domain_age + " days";

        /* SSL */

document.getElementById("sslStatus").innerText =
    data.ssl.status;

document.getElementById("sslIssuer").innerText =
    data.ssl.issuer;

document.getElementById("sslExpiry").innerText =
    data.ssl.expiry;

document.getElementById("sslDays").innerText =
    data.ssl.days_left;

        /* VirusTotal */

document.getElementById("vtStatus").innerText =
    data.virustotal.status;

document.getElementById("vtHarmless").innerText =
    data.virustotal.harmless;

document.getElementById("vtMalicious").innerText =
    data.virustotal.malicious;

document.getElementById("vtSuspicious").innerText =
    data.virustotal.suspicious;

        /* Detection Reasons */

const reasonList = document.getElementById("reasons");

reasonList.innerHTML = "";

data.result.reasons.forEach(reason => {

    const li = document.createElement("li");

    li.innerHTML = "🟢 " + reason;

    reasonList.appendChild(li);

});

        /* Show Download Buttons */

document.getElementById("pdfBtn").classList.remove("hidden");

document.getElementById("jsonBtn").classList.remove("hidden");

status.innerHTML = '<i class="fa-solid fa-circle-check"></i> Analysis Complete';
status.className = "scan-status-success";

    }
    catch (error) {

        status.innerHTML = '<i class="fa-solid fa-circle-xmark"></i> Analysis Failed';
        status.className = "scan-status-error";

        alert("Failed to connect to backend.");
        console.error(error);

    }
    finally {
        scanLoader.classList.add("hidden");
    }
}

function downloadPDF() {

    window.location = "/download/pdf";

}

function downloadJSON() {

    window.location = "/download/json";

}
