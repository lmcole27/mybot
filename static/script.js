
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
        
        console.log(responseContainer.innerText);

        fetch('http://127.0.0.1:5001/api/endpoint', {
            method: 'POST', // HTTP method
            headers: {
                'Content-Type': 'application/json' // Tells the server you're sending JSON
            },
            body: JSON.stringify({ message: responseContainer.innerText  }) // The data to send
        })
        .then(response => response.json()) // Convert response to JSON
        .then(data => console.log('Success:', data)) // Handle success
        .catch(error => console.error('Error:', error)); // Handle errors



    });
});