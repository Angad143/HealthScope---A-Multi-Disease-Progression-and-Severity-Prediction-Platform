document.addEventListener("DOMContentLoaded", function() {
    if (typeof flashedMessages !== "undefined" && flashedMessages.length > 0) {
        flashedMessages.forEach(([category, message]) => {
            if (category === "success") {
                setTimeout(function() {
                    alert(message);
                }, 500);
            }
        });
    }
});
