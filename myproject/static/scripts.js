async function convertUTM() {
    const utmX = parseFloat(document.getElementById('utm_x').value);
    const utmY = parseFloat(document.getElementById('utm_y').value);
    const zoneNumber = parseInt(document.getElementById('zone_number').value);
    const hemisphere = document.getElementById('hemisphere').value;

    const response = await fetch('/convert_utm/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: JSON.stringify({ utmX, utmY, zoneNumber, hemisphere })
    });

    const data = await response.json();
    if (response.ok) {
        document.getElementById('latitude').value = data.latitude;
        document.getElementById('longitude').value = data.longitude;
    } else {
        alert(data.error);
    }
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
