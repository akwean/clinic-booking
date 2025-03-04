const text = "Hello there I am BUP Artificial Intelligence! What is Your Concern?";
    let index = 0;
    function typeEffect() {
      if (index < text.length) {
        document.getElementById("typingText").textContent += text.charAt(index);
        index++;
        setTimeout(typeEffect, 50);
      }
    }
    window.onload = typeEffect;
    
    async function sendMessage() {
      const userInput = document.getElementById("userInput").value;
      const chatBox = document.getElementById("chatBox");
      if (!userInput) return;
      
      const userMessage = document.createElement("p");
      userMessage.innerHTML = `<strong> </strong> ${userInput}`;
      userMessage.classList.add("user-message");
      chatBox.appendChild(userMessage);
      
      const processingMessage = document.createElement("p");
      processingMessage.innerHTML = `<strong>BUP AI:</strong> Processing Answer. . .`;
      processingMessage.classList.add("ai-message");
      chatBox.appendChild(processingMessage);
      document.getElementById("userInput").value = "";
      
      try {
        const response = await fetch("https://openrouter.ai/api/v1/chat/completions", {
          method: "POST",
          headers: {
            "Authorization": "Bearer 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",
            "Content-Type": "application/json"
          },
          body: JSON.stringify({ "model": "google/gemini-exp-1206:free", "messages": [{ "role": "user", "content": userInput }] })
        });
        
        const data = await response.json();
        processingMessage.remove();
        
        const aiMessage = document.createElement("p");
        aiMessage.innerHTML = `<strong>BUP AI:</strong> ${marked.parse(data.choices?.[0]?.message?.content || "Sorry, I couldn't process that request.")}`;
        aiMessage.classList.add("ai-message");
        chatBox.appendChild(aiMessage);
      
      } catch (error) {
        processingMessage.remove();
        const aiError = document.createElement("p");
        aiError.innerHTML = `<strong>BUP AI:</strong> Error: ${error.message}`;
        aiError.classList.add("ai-message");
        chatBox.appendChild(aiError);
      }
    }