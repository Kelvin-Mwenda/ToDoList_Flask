function deleteEvent(eventId){
    fetch("/delete-event",{
        method: "POST",
        body:JSON.stringify({eventId:eventId}),
    }).then((_res)=>{
        window.location.href="/home"
    });
}

document.getElementById('addTaskButton').addEventListener('click', async () => {
    const task = document.getElementById('event').value;
    const date = document.getElementById('date').value;

    if (!eventId) {
        alert('Please select an event.');
        return;
    }

    const eventData = {
        task: task,
        date: date,
    };

    try {
        const response = await fetch('/home', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(eventData)
        });

        if (response.ok) {
            console.log('Event data sent successfully...')
        } else {
            console.error('Failed to add event:', await response.text());
        }
    } catch (error) {
        console.error('Error submitting event:', error);
    }
});