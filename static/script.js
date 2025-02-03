document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('question-form');
    const responseContainer = document.getElementById('response');

    form.addEventListener('submit', async function(event) {
        event.preventDefault();
        const formData = new FormData(form);
        responseContainer.innerHTML = '';
        const response = await fetch('/generate', {
            method: 'POST',
            body: formData
        });

        let question = document.getElementById('question').value;
        document.getElementById('question').value = '';
        document.getElementById('questionAsked').innerText = question;
        document.getElementById('questionAskedHeader').style.display = "block";
        document.getElementById('responseHeader').style.display = "block";
        const reader = response.body.getReader();
        const decoder = new TextDecoder();
        let buffer = '';

        while (true) {
            const { done, value } = await reader.read();
            if (done) break;
            buffer += decoder.decode(value);
            responseContainer.innerHTML = buffer;
            //responseContainer.innerHTML = convertMarkdownToHTML(buffer);
        }
    });
});