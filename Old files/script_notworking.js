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

            let numberPeriodPattern = /\d\./g;
            let match;
            while ((match = numberPeriodPattern.exec(buffer)) !== null) {
                const paragraphText = buffer.slice(0, match.index).trim();
                if (paragraphText) {
                    const paragraph = document.createElement('p');
                    paragraph.textContent = paragraphText;
                    responseContainer.appendChild(paragraph);
                }
                buffer = buffer.slice(match.index);
                numberPeriodPattern.lastIndex = 0; // Reset regex index for new buffer
            }
        }

        // Append any remaining text in the buffer as the last paragraph
        if (buffer.trim()) {
            const paragraph = document.createElement('p');
            paragraph.textContent = buffer.trim();
            responseContainer.appendChild(paragraph);
        }
    });
});