function addMessage(text, sender) {
    let box = document.getElementById("chat-box");
    let div = document.createElement("div");
    div.className = "message " + sender;

    let time = new Date().toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'});

    if (sender === "agent" && typeof text === "object") {
        div.innerHTML = `
            <div class="agent-json">${JSON.stringify(text, null, 2)}</div>
            <div style="font-size:12px; color:#666; margin-top:4px;">${time}</div>
        `;
    } else {
        div.innerHTML = `
            ${text}
            <div style="font-size:12px; color:#eee; margin-top:4px;">${time}</div>
        `;
    }

    box.appendChild(div);
    box.scrollTop = box.scrollHeight;
}

function sendMessage() {
    let input = document.getElementById("user-input").value;

    if (input.trim() === "") return;

    addMessage(input, "user");

    let typing = document.getElementById("typing");
    typing.innerText = "AI Agent is typing…";

    fetch("http://127.0.0.1:8000/agent", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: input })
    })
    .then(response => response.json())
    .then(data => {
        typing.innerText = "";
        addMessage(data.output, "agent");
    });

    document.getElementById("user-input").value = "";
}

document.getElementById("user-input").addEventListener("keydown", function(e) {
    if (e.key === "Enter") {
        sendMessage();
    }
});

document.getElementById("user-input").focus();

function clearChat() {
    document.getElementById("chat-box").innerHTML = "";
}
