const form = document.getElementById("uploadForm");

const processing = document.getElementById("processing");

const dashboard = document.getElementById("dashboard");

const progress = document.getElementById("progress-bar");

const steps = document.querySelectorAll("#steps li");

let currentStep = 0;


/* ==========================================
   Highlight AI Steps
========================================== */

function animateSteps(){

    currentStep = 0;

    steps.forEach(step=>{

        step.style.opacity=".35";
        step.style.transform="translateX(0px)";
        step.style.background="rgba(255,255,255,.05)";
        step.style.borderLeftColor="#00e5ff";

    });

    const interval = setInterval(()=>{

        if(currentStep>0){

            steps[currentStep-1].style.opacity=".55";

        }

        if(currentStep<steps.length){

            const item=steps[currentStep];

            item.style.opacity="1";

            item.style.background="rgba(0,229,255,.15)";

            item.style.borderLeftColor="#35ff9a";

            item.style.transform="translateX(10px)";

            currentStep++;

        }

        else{

            clearInterval(interval);

        }

    },700);

}


/* ==========================================
   Counter Animation
========================================== */

function animateNumber(id,target,suffix=""){

    let value=0;

    const increment=target/60;

    const timer=setInterval(()=>{

        value+=increment;

        if(value>=target){

            value=target;

            clearInterval(timer);

        }

        document.getElementById(id).innerHTML=
        Math.floor(value)+suffix;

    },25);

}


/* ==========================================
   Progress Bar
========================================== */

function animateProgress(){

    progress.style.width="0%";

    let width=0;

    const timer=setInterval(()=>{

        width+=2;

        progress.style.width=width+"%";

        if(width>=100){

            clearInterval(timer);

        }

    },120);

}
/* ==========================================
   Upload Form
========================================== */

form.addEventListener("submit", async function(e){

    e.preventDefault();

    dashboard.style.display="none";

    processing.style.display="block";

    animateProgress();

    animateSteps();

    const formData=new FormData();

    formData.append(
        "resume",
        document.getElementById("resume").files[0]
    );

    formData.append(
        "csv",
        document.getElementById("csv").files[0]
    );

    try{

        const response=await fetch("/transform",{

            method:"POST",

            body:formData

        });

        const result=await response.json();

        if(!result.success){

            alert(result.message);

            processing.style.display="none";

            return;

        }

        setTimeout(()=>{

            processing.style.display="none";

            dashboard.style.display="block";

            loadDashboard(result.candidate);

        },6500);

    }

    catch(error){

        alert("Server Error");

        processing.style.display="none";

    }

});


/* ==========================================
   Load Candidate
========================================== */

function loadDashboard(c){

    document.getElementById("name").innerHTML=c.name;

    document.getElementById("email").innerHTML=c.email;

    document.getElementById("phone").innerHTML=c.phone;

    document.getElementById("company").innerHTML=c.company;

    document.getElementById("designation").innerHTML=c.designation;

    document.getElementById("location").innerHTML=c.location;


    animateNumber(

        "confidence",

        parseInt(c.overall_confidence*100),

        "%"

    );


    animateNumber(

        "trust",

        parseInt(c.profile_health.trust_score)

    );


    loadSkills(c.skills);

}