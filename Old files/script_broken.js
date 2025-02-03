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
            while (lastPeriodIndex !== -1) {
                const precedingText = buffer.slice(0, lastPeriodIndex + 1);
                const followingText = buffer.slice(lastPeriodIndex + 1);

                // Check if the period is preceded by a number
                const numberPattern = /\d\.$/;
                if (numberPattern.test(precedingText)) {
                    lastPeriodIndex = precedingText.lastIndexOf('.');
                    continue;
                }

                const paragraphText = buffer.slice(0, lastPeriodIndex + 1);
                buffer = buffer.slice(lastPeriodIndex + 1);

                const paragraph = document.createElement('p');
                paragraph.textContent = paragraphText.trim();
                responseContainer.appendChild(paragraph);

                lastPeriodIndex = buffer.lastIndexOf('.');
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