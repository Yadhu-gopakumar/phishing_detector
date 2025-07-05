async function checkPhishingStatus() {
  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  const url = tab.url;

  const response = await fetch("http://localhost:5000/check", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ url: url })
  });

  const data = await response.json();
  document.getElementById("result").innerText = `Result: ${data.result}`;
}

// Bind to button
document.getElementById("checkBtn").onclick = checkPhishingStatus;

