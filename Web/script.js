function toggleChatbot() {
    const chatbot = document.getElementById('chatbot');
    const isHidden = chatbot.classList.contains('hidden');
    if (isHidden) {
        chatbot.classList.remove('hidden');
    } else {
        chatbot.classList.add('hidden');
    }
}
