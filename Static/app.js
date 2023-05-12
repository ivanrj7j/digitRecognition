const side = 28;
const canvasScale = 20;
const size = `${side * canvasScale}px`;
// initialising the canvas properties 

let pencilWidth = 2;

// general constants and variables

const prediction = document.querySelector('.prediction');
// prediction display element 



let canvas = document.createElement('canvas');
let context = canvas.getContext('2d');

canvas.setAttribute('width', size);
canvas.setAttribute('height', size);

function setupCanvas() {
    context.fillStyle = `black`;
    context.fillRect(0, 0, canvasScale * side, canvasScale * side);
}

setupCanvas();

// setting up the canvas



let isDrawing = false;

function registerDraw(x, y, width) {
    const fillColor = 255;


    context.fillStyle = `rgb( ${fillColor}, ${fillColor}, ${fillColor})`;
    context.fillRect(x * canvasScale, y * canvasScale, width, width);
}

function draw(e) {
    let x = Math.floor(e.clientX / canvasScale)
    let y = Math.floor(e.clientY / canvasScale);

    registerDraw(x, y, 30);

}

// functions for drawing the image 


canvas.addEventListener('mousedown', e => {
    isDrawing = true;
    draw(e);
});


canvas.addEventListener('mousemove', e => {
    if (isDrawing) {
        draw(e);
    }
});

// drawing when the mouse is pressed and moving 

function cancelDraw() {
    isDrawing = false;
    predict();
}

canvas.addEventListener('mouseup', () => {
    cancelDraw();
});

canvas.addEventListener('mouseout', () => {
    cancelDraw();
});

// stopping the drawing 

document.querySelector('.canvas').appendChild(canvas);

// canvas code 

let slider = document.createElement('input');
slider.setAttribute('type', 'range');
slider.setAttribute('min', 1);
slider.setAttribute('max', 3);
slider.setAttribute('value', 2);

canvas.parentElement.appendChild(document.createElement('br'));
canvas.parentElement.appendChild(slider);

slider.addEventListener('input', () => {
    pencilWidth = slider.value;
});
// slider code 

let resetButton = document.createElement('button');
resetButton.innerText = 'Reset';
resetButton.addEventListener('click', () => {
    colors = Array.from({ length: side }, () => Array.from({ length: side }).fill(0));
    context.fillStyle = 'white';
    context.fillRect(0, 0, side * canvasScale, side * canvasScale);
    setupCanvas();
});

canvas.parentElement.appendChild(document.createElement('br'));
canvas.parentElement.appendChild(resetButton);
// reset button code


function predict() {
    const image = canvas.toDataURL().replace('data:image/png;base64,', '');
    // getting the image base64 

    let formdata = new FormData();
    formdata.append('image', image);
    let request = fetch('/predictCOlor', {
        method: 'POST',
        body: formdata
    });
    // sending the request to server 

    request.then(response => {
        response.json().then(predictions => {
            let predictionString = `Prediction: ${predictions[0][0]}`;
            for (let index = 0; index < predictions.length; index++) {
                const element = predictions[index];
                predictionString += `<br>${element[0]} : ${Math.round(element[1])}%`;
            }
            prediction.innerHTML = predictionString;
        });
    });
    // handling the response and updating the predictions 
}
// sends a request to the server and show the predictions 