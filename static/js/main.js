document.addEventListener("DOMContentLoaded", () => {
  const chatForm = document.getElementById("chat-form");
  const chatInput = document.getElementById("chat-input");
  const chatMessages = document.getElementById("chat-messages");
  const endpoint = chatForm?.dataset?.endpoint || "/api/ask-twin";

  if (!chatForm || !chatInput || !chatMessages) {
    console.warn("Chat elements not found; Digital Twin chat will be disabled.");
    return;
  }

  function addMessage(sender, text) {
    const bubble = document.createElement("div");
    bubble.classList.add("chat-bubble");

    if (sender === "user") {
      bubble.classList.add("chat-bubble-user");
    } else {
      bubble.classList.add("chat-bubble-twin");
    }

    bubble.textContent = text;
    chatMessages.appendChild(bubble);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  function addLoading() {
    const bubble = document.createElement("div");
    bubble.classList.add("chat-bubble", "chat-bubble-twin");
    bubble.dataset.loading = "true";
    bubble.textContent = "Thinking...";
    chatMessages.appendChild(bubble);
    chatMessages.scrollTop = chatMessages.scrollHeight;
    return bubble;
  }

  async function sendToTwin(message) {
    addMessage("user", message);
    const loadingBubble = addLoading();

    try {
      const response = await fetch(endpoint, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ question: message })
      });

      loadingBubble.remove();

      if (!response.ok) {
        addMessage("twin", "Sorry, there was an error contacting the digital twin.");
        return;
      }

      const data = await response.json();

      if (data.answer) {
        addMessage("twin", data.answer);
      } else if (data.error) {
        addMessage("twin", "Error: " + data.error);
      } else {
        addMessage("twin", "Sorry, I did not understand the response.");
      }
    } catch (err) {
      loadingBubble.remove();
      console.error(err);
      addMessage("twin", "Network error while talking to the digital twin.");
    }
  }

  chatForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const message = chatInput.value.trim();
    if (!message) {
      return;
    }

    chatInput.value = "";
    chatInput.focus();

    const submitButton = chatForm.querySelector("button[type='submit']");
    if (submitButton) {
      submitButton.disabled = true;
    }

    sendToTwin(message).finally(() => {
      if (submitButton) {
        submitButton.disabled = false;
      }
    });
  });
});
