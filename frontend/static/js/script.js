const form = document.getElementById("uploadForm");

form.addEventListener("submit", async function (e) {

    e.preventDefault();

    document.getElementById("processing").style.display = "block";

    const formData = new FormData();

    formData.append(
        "resume",
        document.getElementById("resume").files[0]
    );

    formData.append(
        "csv",
        document.getElementById("csv").files[0]
    );

    const response = await fetch("/transform", {
        method: "POST",
        body: formData
    });

    const result = await response.json();

    console.log(result);

    if (!result.success) {

        alert(result.message);
        return;

    }

    const c = result.candidate;

    document.getElementById("processing").style.display = "none";
    document.getElementById("dashboard").style.display = "block";

    document.getElementById("name").textContent = c.name;
    document.getElementById("email").textContent = c.email;
    document.getElementById("phone").textContent = c.phone;
    document.getElementById("company").textContent = c.company;
    document.getElementById("designation").textContent = c.designation;
    document.getElementById("location").textContent = c.location;
    document.getElementById("confidence").textContent = c.overall_confidence;
    document.getElementById("trust").textContent = c.profile_health.trust_score;

    const skills = document.getElementById("skills");

    skills.innerHTML = "";

    c.skills.forEach(skill => {

        skills.innerHTML += `<span class="skill">${skill}</span>`;

    });

});