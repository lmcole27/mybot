// const converter = new showdown.Converter();

// function convertMarkdownToHTML(markdown) {
//     return converter.makeHtml(markdown);
// }


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


        //Do I Need This?
        const reader = response.body.getReader();
        const decoder = new TextDecoder();
        let buffer = '';
        
        while (true) {
            const { done, value } = await reader.read();
            if (done) break;
            buffer += decoder.decode(value);
        }

// Trying different code
            // Split the buffer into paragraphs at periods followed by a space or end of string
            let splitPattern = /(\d\.\s|\. )/g;
            let parts = buffer.split(splitPattern);

            // Process each part and append to the response container
            for (let i = 0; i < parts.length - 1; i += 2) {
                const paragraphText = parts[i] + (parts[i + 1] || '');
                const paragraph = document.createElement('p');
                paragraph.textContent = paragraphText.trim();
                responseContainer.appendChild(paragraph);
            }

            // Keep the last part in the buffer if it doesn't end with a period
            buffer = parts[parts.length - 1];
        }

    });
});



//OG

        //     let lastPeriodIndex = buffer.lastIndexOf('.');
        //     if (lastPeriodIndex !== -1) {
        //         const paragraphText = buffer.slice(0, lastPeriodIndex + 1);
        //         buffer = buffer.slice(lastPeriodIndex + 1);

        //         const paragraph = document.createElement('p');
        //         paragraph.textContent = paragraphText.trim();
        //         responseContainer.appendChild(paragraph);
        //     }
        // }

        // if (buffer.trim()) {
        //     const paragraph = document.createElement('p');
        //     paragraph.textContent = buffer.trim();
        //     responseContainer.appendChild(paragraph);
        // }
//     });
// });