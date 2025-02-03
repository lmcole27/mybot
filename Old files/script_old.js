//const responseDiv = document.getElementById('response');
//const eventSource = new EventSource('/stream'); // Connect to the Flask stream endpoint

//eventSource.onmessage = function(event) {
//    responseDiv.textContent += event.data; // Append new data
//};

//eventSource.onerror = function() {
//    console.error("Error in event source.");
//    eventSource.close();
//};



//THIS WORKED ISH
// document.addEventListener('DOMContentLoaded', function() {
//     const form = document.getElementById('question-form');
//     const responseContainer = document.getElementById('response');

//     form.addEventListener('submit', async function(event) {
//         event.preventDefault();
//         const formData = new FormData(form);
//         responseContainer.innerHTML = '';

//         const response = await fetch('/generate', {
//             method: 'POST',
//             body: formData
//         });

//         const reader = response.body.getReader();
//         const decoder = new TextDecoder();
//         while (true) {
//             const { done, value } = await reader.read();
//             if (done) break;
//             responseContainer.innerHTML += decoder.decode(value);
//         }
//     });
// });

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

        const reader = response.body.getReader();
        const decoder = new TextDecoder();
        let buffer = '';
        
        while (true) {
            const { done, value } = await reader.read();
            if (done) break;
            buffer += decoder.decode(value);

            let lastPeriodIndex = buffer.lastIndexOf('.');
            if (lastPeriodIndex !== -1) {
                const paragraphText = buffer.slice(0, lastPeriodIndex + 1);
                buffer = buffer.slice(lastPeriodIndex + 1);

                const paragraph = document.createElement('p');
                paragraph.textContent = paragraphText.trim();
                responseContainer.appendChild(paragraph);
            }
        }

        //     const chunk = decoder.decode(value);
        //     const paragraph = document.createElement('p');
        //     paragraph.textContent = chunk;
        //     responseContainer.appendChild(paragraph);
        //    // responseContainer.innerHTML += decoder.decode(value);
        if (buffer.trim()) {
            const paragraph = document.createElement('p');
            paragraph.textContent = buffer.trim();
            responseContainer.appendChild(paragraph);
        }
    });
});