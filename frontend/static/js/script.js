// DOM Elements - Selectors
const uploadForm = document.getElementById("uploadForm");
const resumeInput = document.getElementById("resume");
const csvInput = document.getElementById("csv");
const resumeFileName = document.getElementById("resume-file-name");
const csvFileName = document.getElementById("csv-file-name");

const uploadDeck = document.getElementById("upload-deck");
const processing = document.getElementById("processing");
const dashboard = document.getElementById("dashboard");
const progressBar = document.getElementById("progress-bar");
const stepItems = document.querySelectorAll("#steps .step-item");

const btnReset = document.getElementById("btn-reset");
const btnDownloadJson = document.getElementById("btn-download-json");

// State for active candidate data
let activeCandidate = null;

// ==========================================
// File Input Selection Event Listeners
// ==========================================
resumeInput.addEventListener("change", function() {
    if (resumeInput.files && resumeInput.files[0]) {
        const span = resumeFileName.querySelector("span");
        span.textContent = resumeInput.files[0].name;
        resumeFileName.classList.add("visible");
    } else {
        resumeFileName.classList.remove("visible");
    }
});

csvInput.addEventListener("change", function() {
    if (csvInput.files && csvInput.files[0]) {
        const span = csvFileName.querySelector("span");
        span.textContent = csvInput.files[0].name;
        csvFileName.classList.add("visible");
    } else {
        csvFileName.classList.remove("visible");
    }
});

// ==========================================
// Pipeline Loader & Animation Rules
// ==========================================
function runPipelineAnimations(onComplete) {
    let currentStep = 0;
    progressBar.style.width = "0%";

    // Reset pipeline steps visual state
    stepItems.forEach(step => {
        step.className = "step-item";
    });

    // 1. Progress Bar filler timer
    let progress = 0;
    const progressInterval = setInterval(() => {
        progress += 1.5;
        if (progress >= 100) {
            progress = 100;
            clearInterval(progressInterval);
        }
        progressBar.style.width = progress + "%";
    }, 90);

    // 2. Sequential pipeline step highlighter timer
    const stepInterval = setInterval(() => {
        // Mark previous step as completed
        if (currentStep > 0) {
            stepItems[currentStep - 1].classList.remove("active");
            stepItems[currentStep - 1].classList.add("completed");
            // Replace loading/empty icon with a checkmark
            const icon = stepItems[currentStep - 1].querySelector("i");
            icon.className = "fa-solid fa-circle-check";
        }

        if (currentStep < stepItems.length) {
            const item = stepItems[currentStep];
            item.classList.add("active");
            const icon = item.querySelector("i");
            icon.className = "fa-solid fa-spinner fa-spin";
            currentStep++;
        } else {
            clearInterval(stepInterval);
            setTimeout(onComplete, 600); // Small buffer after finishing all steps
        }
    }, 950);
}

// ==========================================
// Number Counter Ingestion Animation
// ==========================================
function animateCounter(elementId, target, suffix = "") {
    const el = document.getElementById(elementId);
    if (!el) return;
    
    let current = 0;
    const duration = 800; // ms
    const stepTime = 16;  // ~60fps
    const steps = duration / stepTime;
    const increment = target / steps;
    
    const timer = setInterval(() => {
        current += increment;
        if (current >= target) {
            current = target;
            clearInterval(timer);
        }
        el.textContent = Math.floor(current) + suffix;
    }, stepTime);
}

// ==========================================
// Load and Populate Candidate Profile
// ==========================================
function loadDashboard(candidate) {
    // 1. Base Identity Info
    document.getElementById("name").textContent = candidate.name || "N/A";
    document.getElementById("designation").textContent = candidate.designation || "Unspecified Role";
    document.getElementById("company").textContent = candidate.company || "Unspecified Company";

    // 2. Core Contact Info
    document.getElementById("email").textContent = candidate.email || "N/A";
    document.getElementById("phone").textContent = candidate.phone || "N/A";
    document.getElementById("location").textContent = candidate.location || "N/A";

    // 3. Validation Badge
    const badgeContainer = document.getElementById("validation-badge-container");
    badgeContainer.innerHTML = "";
    
    const isValid = candidate.validation && candidate.validation.is_valid;
    const badge = document.createElement("span");
    if (isValid) {
        badge.className = "badge-verified";
        badge.innerHTML = `<i class="fa-solid fa-circle-check"></i> Profile Validated`;
    } else {
        badge.className = "badge-invalid";
        badge.innerHTML = `<i class="fa-solid fa-circle-exclamation"></i> Profile Errors`;
    }
    badgeContainer.appendChild(badge);

    // 4. Score metrics animations
    const qualityScore = candidate.data_quality ? candidate.data_quality.overall_score : 0;
    const trustScore = candidate.profile_health ? candidate.profile_health.trust_score : 0;
    const completionPercent = candidate.profile_health ? candidate.profile_health.completion : 0;
    const confidencePercent = candidate.overall_confidence ? Math.round(candidate.overall_confidence * 100) : 0;
    const grade = candidate.data_quality ? candidate.data_quality.grade : "D";

    document.getElementById("grade").textContent = grade;
    animateCounter("confidence", confidencePercent, "%");
    animateCounter("trust", trustScore);
    animateCounter("completion", completionPercent, "%");

    // 5. Skills Grid builder
    const skillsContainer = document.getElementById("skills-container");
    skillsContainer.innerHTML = "";
    if (candidate.skills && candidate.skills.length > 0) {
        candidate.skills.forEach(skill => {
            const pill = document.createElement("span");
            pill.className = "skill-pill";
            pill.innerHTML = `<i class="fa-solid fa-check"></i> ${skill}`;
            skillsContainer.appendChild(pill);
        });
    } else {
        skillsContainer.innerHTML = `<span class="text-muted">No technical skills detected</span>`;
    }

    // 6. Experience List builder
    const experienceList = document.getElementById("experience-list");
    experienceList.innerHTML = "";
    if (candidate.experience && candidate.experience.length > 0) {
        candidate.experience.forEach(exp => {
            const item = document.createElement("div");
            item.className = "detail-item";
            item.textContent = exp;
            experienceList.appendChild(item);
        });
    } else {
        experienceList.innerHTML = `<div class="detail-item text-muted">No employment history parsed</div>`;
    }

    // 7. Education List builder
    const educationList = document.getElementById("education-list");
    educationList.innerHTML = "";
    if (candidate.education && candidate.education.length > 0) {
        candidate.education.forEach(edu => {
            const item = document.createElement("div");
            item.className = "detail-item";
            item.textContent = edu;
            educationList.appendChild(item);
        });
    } else {
        educationList.innerHTML = `<div class="detail-item text-muted">No educational records parsed</div>`;
    }

    // 8. Conflicts Table builder
    const conflictTbody = document.getElementById("conflict-tbody");
    const conflictStatusEl = document.getElementById("conflict-status");
    conflictTbody.innerHTML = "";

    if (candidate.conflicts && candidate.conflicts.length > 0) {
        conflictStatusEl.textContent = `${candidate.conflicts.length} fields resolved`;
        conflictStatusEl.style.color = "var(--accent-amber)";
        
        candidate.conflicts.forEach(conflict => {
            const tr = document.createElement("tr");
            
            // Format winner display badge
            const isCSV = conflict.winner && conflict.winner.toLowerCase().includes("csv");
            const winnerBadge = `<span class="badge-conflict-winner ${isCSV ? 'csv' : 'resume'}">${conflict.winner}</span>`;
            
            tr.innerHTML = `
                <td class="conflict-field">${conflict.field}</td>
                <td>${conflict.resume_value || '<span class="text-muted">Empty</span>'}</td>
                <td>${conflict.csv_value || '<span class="text-muted">Empty</span>'}</td>
                <td>${winnerBadge}</td>
                <td class="conflict-reason">${conflict.reason}</td>
            `;
            conflictTbody.appendChild(tr);
        });
    } else {
        conflictStatusEl.textContent = "No conflicts detected";
        conflictStatusEl.style.color = "var(--accent-emerald)";
        
        // Show empty notification row inside table
        conflictTbody.innerHTML = `
            <tr>
                <td colspan="5">
                    <div class="no-conflicts-notice">
                        <i class="fa-solid fa-circle-check"></i>
                        <span>No conflicts detected. Resume and Recruiter data match.</span>
                    </div>
                </td>
            </tr>
        `;
    }

    // 9. Business Rules Evaluator list
    const rulesList = document.getElementById("rules-list");
    rulesList.innerHTML = "";

    // The backend evaluates 5 core rules. Let's build them by matching failed rules
    const coreRules = [
        { id: "name", label: "Name is required", check: () => !!candidate.name },
        { id: "email", label: "Email is required", check: () => !!candidate.email },
        { id: "phone", label: "Phone is required", check: () => !!candidate.phone },
        { id: "skills", label: "At least 3 skills required", check: () => candidate.skills && candidate.skills.length >= 3 },
        { id: "confidence", label: "Confidence must be >= 0.80", check: () => candidate.overall_confidence >= 0.80 }
    ];

    const failedRulesList = (candidate.rule_engine && candidate.rule_engine.failed_rules) || [];

    coreRules.forEach(rule => {
        const item = document.createElement("div");
        // Rule fails if its label exists in the failed rules list or if its validation logic fails
        const isFailed = failedRulesList.some(r => r.toLowerCase().includes(rule.id)) || !rule.check();
        
        if (isFailed) {
            item.className = "eval-item failed";
            item.innerHTML = `<i class="fa-solid fa-circle-xmark"></i> <span>${rule.label}</span>`;
        } else {
            item.className = "eval-item passed";
            item.innerHTML = `<i class="fa-solid fa-circle-check"></i> <span>${rule.label}</span>`;
        }
        rulesList.appendChild(item);
    });

    // 10. Profile Validation Errors list
    const validationList = document.getElementById("validation-list");
    validationList.innerHTML = "";
    
    const errors = (candidate.validation && candidate.validation.errors) || [];
    if (errors.length > 0) {
        errors.forEach(err => {
            const item = document.createElement("div");
            item.className = "eval-item failed";
            item.innerHTML = `<i class="fa-solid fa-triangle-exclamation"></i> <span>${err}</span>`;
            validationList.appendChild(item);
        });
    } else {
        const item = document.createElement("div");
        item.className = "eval-item passed";
        item.innerHTML = `<i class="fa-solid fa-circle-check"></i> <span>No format validation errors found</span>`;
        validationList.appendChild(item);
    }
}

// ==========================================
// Form Submission & Request
// ==========================================
uploadForm.addEventListener("submit", async function(e) {
    e.preventDefault();

    if (!resumeInput.files[0] || !csvInput.files[0]) {
        alert("Please select both files.");
        return;
    }

    // Toggle view states
    uploadDeck.style.display = "none";
    processing.style.display = "block";
    dashboard.style.display = "none";

    const formData = new FormData();
    formData.append("resume", resumeInput.files[0]);
    formData.append("csv", csvInput.files[0]);

    // Fire network request and run animations in parallel
    let responseData = null;
    let requestError = null;

    const requestPromise = fetch("/transform", {
        method: "POST",
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        responseData = data;
    })
    .catch(err => {
        requestError = err;
    });

    // Wait for the pipeline animations to finish
    runPipelineAnimations(async () => {
        // Wait for request to fully resolve if it's slower than the animation (highly unlikely)
        await requestPromise;

        if (requestError) {
            alert("Connection error: Unable to process files.");
            resetSession();
            return;
        }

        if (!responseData || !responseData.success) {
            alert(responseData ? responseData.message : "Error: Pipeline execution failed.");
            resetSession();
            return;
        }

        // Cache candidate data in state
        activeCandidate = responseData.candidate;

        // Render dashboard and toggle screens
        loadDashboard(activeCandidate);
        processing.style.display = "none";
        dashboard.style.display = "block";
    });
});

// ==========================================
// Session Reset & Clear Functionality
// ==========================================
function resetSession() {
    uploadForm.reset();
    resumeFileName.classList.remove("visible");
    csvFileName.classList.remove("visible");
    resumeFileName.querySelector("span").textContent = "No file chosen";
    csvFileName.querySelector("span").textContent = "No file chosen";
    
    activeCandidate = null;
    
    dashboard.style.display = "none";
    processing.style.display = "none";
    uploadDeck.style.display = "block";
}

btnReset.addEventListener("click", resetSession);

// ==========================================
// JSON Profile Download Generator
// ==========================================
btnDownloadJson.addEventListener("click", function() {
    if (!activeCandidate) return;

    const candidateName = (activeCandidate.name || "candidate").toLowerCase().replace(/\s+/g, "_");
    const fileName = `${candidateName}_profile.json`;
    const jsonString = JSON.stringify(activeCandidate, null, 4);
    
    const blob = new Blob([jsonString], { type: "application/json" });
    const url = URL.createObjectURL(blob);
    
    const link = document.createElement("a");
    link.href = url;
    link.download = fileName;
    
    document.body.appendChild(link);
    link.click();
    
    // Clean up
    document.body.removeChild(link);
    URL.revokeObjectURL(url);
});