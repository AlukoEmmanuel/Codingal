document.getElementById("recommend-form").onsubmit = async function(event) {
    event.preventDefault();
    const movieTitle = event.target.movie_title.value;
    const response = await fetch("/recommend", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ movie_title: movieTitle })
    });
    const data = await response.json();
    document.getElementById("recommendations").innerHTML = `<h2>Recommendations:</h2><ul>${data.map(title => `<li>${title}</li>`).join("")}</ul>`;
};

document.getElementById("popular-btn").onclick = async function() {
    const response = await fetch("/popular");
    const data = await response.json();
    document.getElementById("popular-movies").innerHTML = `<h2>Popular Movies:</h2><ul>${data.map(title => `<li>${title}</li>`).join("")}</ul>`;
};
