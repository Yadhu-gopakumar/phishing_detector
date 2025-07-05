chrome.tabs.onUpdated.addListener(async (tabId, changeInfo, tab) => {
  if (changeInfo.status === 'complete' && tab.url.startsWith('http')) {
    try {
      const response = await fetch("http://127.0.0.1:5000/check", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url: tab.url })
      });

      const data = await response.json();
      if (data.result === "Phishing") {
        chrome.tabs.update(tabId, { url: chrome.runtime.getURL("blocked.html") });
      }

    } catch (err) {
      console.error("Phishing check failed:", err);
    }
  }
});

