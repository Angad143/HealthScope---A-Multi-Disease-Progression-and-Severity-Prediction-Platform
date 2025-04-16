document.addEventListener("DOMContentLoaded", function () {
    const voiceButton = document.getElementById("voice-button");
    const statusDiv = document.getElementById("status");
    const soundWave = document.getElementById("sound-wave");
    const micIcon = document.querySelector(".mic-icon");
    const activeMicIcon = document.querySelector(".active-mic-icon");
    const synth = window.speechSynthesis;
  
    let speechDetected = false;
    let timeoutId = null;
    const SPEECH_TIMEOUT = 3000; // 3 seconds
  
    if (!("webkitSpeechRecognition" in window)) {
      statusDiv.innerHTML =
        '<p style="color:#EA4335">Voice commands not supported in your browser. Please use Chrome.</p>';
      voiceButton.disabled = true;
      return;
    }
  
    const recognition = new webkitSpeechRecognition();
    recognition.continuous = false;
    recognition.interimResults = false;
    recognition.lang = "en-US";
  
    // Ripple effect
    voiceButton.addEventListener("click", function (e) {
      const rect = voiceButton.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
  
      const ripple = document.createElement("span");
      ripple.classList.add("ripple");
      ripple.style.left = `${x}px`;
      ripple.style.top = `${y}px`;
  
      voiceButton.appendChild(ripple);
      setTimeout(() => ripple.remove(), 600);
    });
  
    // Start and Stop listeners
    const listenEvents = ["mousedown", "touchstart"];
    const stopEvents = ["mouseup", "touchend", "mouseleave", "touchcancel"];
  
    listenEvents.forEach((event) =>
      voiceButton.addEventListener(event, startListening)
    );
    stopEvents.forEach((event) =>
      voiceButton.addEventListener(event, stopListening)
    );
  
    function startListening() {
      // ✅ Cancel speech if speaking
      if (synth.speaking) {
        synth.cancel();
        statusDiv.textContent = "Speech stopped. Tap the mic to ask something else.";
        statusDiv.style.color = "#EA4335";
        return;
      }
  
      if (recognition.running) return;
  
      speechDetected = false;
      micIcon.style.display = "none";
      activeMicIcon.style.display = "block";
      voiceButton.classList.add("listening");
      soundWave.classList.add("listening");
  
      statusDiv.textContent = "Listening...";
      statusDiv.style.color = "#202124";
  
      timeoutId = setTimeout(() => {
        if (!speechDetected) handleNoSpeech();
      }, SPEECH_TIMEOUT);
  
      recognition.start();
    }
  
    function stopListening() {
      clearTimeout(timeoutId);
      micIcon.style.display = "block";
      activeMicIcon.style.display = "none";
      voiceButton.classList.remove("listening");
      soundWave.classList.remove("listening");
  
      try {
        recognition.stop();
      } catch (e) {
        console.log("Recognition already stopped.");
      }
  
      if (!speechDetected && statusDiv.textContent === "Listening...") {
        resetStatus();
      }
    }
  
    function handleNoSpeech() {
      statusDiv.textContent = "Hmm... I didn’t hear anything. Please try again.";
      statusDiv.style.color = "#EA4335";
      stopListening();
  
      setTimeout(resetStatus, 3000);
    }
  
    function resetStatus() {
      statusDiv.textContent = "Tap the microphone to ask a health-related question.";
      statusDiv.style.color = "#5f6368";
    }
  
    function speakResponse(text) {
      if (synth.speaking) synth.cancel();
  
      const utterance = new SpeechSynthesisUtterance(text);
      utterance.rate = 1;
      utterance.pitch = 1;
      utterance.volume = 1;
  
      utterance.onstart = () => {
        statusDiv.textContent = "Assistant is speaking...";
        statusDiv.style.color = "#4285F4";
      };
  
      // ✅ Updated message when speech ends
      utterance.onend = function () {
        statusDiv.textContent = "Tap the microphone to ask another health-related question.";
        statusDiv.style.color = "#5f6368";
      };
  
      synth.speak(utterance);
    }
  
    recognition.onresult = function (event) {
      speechDetected = true;
      clearTimeout(timeoutId);
  
      const transcript = event.results[0][0].transcript;
      statusDiv.textContent = `You asked: "${transcript}"`;
  
      fetch("/ask", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: `user_input=${encodeURIComponent(transcript)}`,
      })
        .then((res) => res.json())
        .then((data) => speakResponse(data.response))
        .catch((err) => {
          console.error("Error:", err);
          speakResponse("Sorry, something went wrong. Please try again.");
        });
    };
  
    recognition.onerror = function (event) {
      if (event.error === "no-speech") {
        handleNoSpeech();
      } else {
        console.error("Speech recognition error:", event.error);
        statusDiv.textContent = "Error: " + event.error;
        statusDiv.style.color = "#EA4335";
        stopListening();
      }
    };
  
    recognition.onspeechend = function () {
      if (!speechDetected) handleNoSpeech();
      stopListening();
    };
  });
  